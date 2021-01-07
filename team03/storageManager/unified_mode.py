from storage.avl import avl_mode as avl
from storage.b import b_mode as b
from storage.bplus import bplus_mode as bplus
from storage.dict import dict_mode as d
from storage.hash import hash_mode as ha
from storage.isam import isam_mode as isam
from storage.json import json_mode as j

import pickle
import os


def __commit(objeto, nombre):
    file = open(nombre+".bin", "wb+")
    file.write(pickle.dumps(objeto))
    file.close()


def __rollback(nombre):
    file = open(nombre+".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)


def __getDatabase(database):
    if os.path.exists("data.bin"):
        listaDB = __rollback("data")

        for db in listaDB:
            if db["nameDb"].lower() == database.lower():
                # Retorna el diccionario de la base de datos
                return db

        return False
    else:
        data = []
        __commit(data, "data")
        return False


def createDatabase(database: str, mode: str, encoding = "ascii") -> int:
    try:
        if not database.isidentifier() \
                or not mode.isidentifier() \
                or not encoding.isidentifier():
            raise Exception()

        if encoding != "utf8" or encoding != "ascii" or encoding != "iso-8859-1":
            return 4

        # Retorna el diccionario de una base de datos especifica
        dbBuscada = __getDatabase(database)
        estado = 0

        if dbBuscada is False:

            if mode == "avl":
                estado = avl.createDatabase(database)

            elif mode == "b":
                estado = b.createDatabase(database)

            elif mode == "bplus":
                estado = bplus.createDatabase(database)

            elif mode == "hash":
                estado = ha.createDatabase(database)

            elif mode == "isam":
                estado = isam.createDatabase(database)

            elif mode == "json":
                estado = j.createDatabase(database)

            elif mode == "dict":
                estado = d.createDatabase(database)

            else:
                return 3
        else:
            return 2

        if estado == 0:
            #Pedir la lista de diccionarios de base de datos
            listaDB = __rollback("data")
            listaDB.append({"nameDb": database, "mode": mode, "encoding": encoding, "tables": []})
            #Se guarda la nueva base de datos en el archivo data
            __commit(listaDB, "data")

        return estado
    except:
        return 1
