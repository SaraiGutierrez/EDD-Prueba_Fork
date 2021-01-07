import pickle
import hashlib

def __commit(objeto, nombre):
    file = open(nombre+".bin", "wb+")
    file.write(pickle.dumps(objeto))
    file.close()


def __rollback(nombre):
    file = open(nombre+".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)

 
ruta = "bd1.bin"
hasher = hashlib.md5()

registro = [1,"pedro","Guatemala"]

tablas = [{"nombre": "tb1", "registros":[]}, {"nombre": "tb2", "registros": []}]

dic1 = {"nombre": "db1", "modo": "avl", "cantidad": 10, "tablas": tablas}
dic2 = {"nombre": "db2", "modo": "avl", "cantidad": 9, "tablas": tablas}

__commit(dic1, "bd1")

with open(ruta, 'rb') as open_file:
    #content=open_file.read()
    #print(content)
    hasher.update("hola")
print(hasher.hexdigest())

#P1 67cf055394c4c054c4efdf693ae5c84a    cantidad 10
#P2 67cf055394c4c054c4efdf693ae5c84a    cantidad 10
#P3 adc829def740a24aa2afa8f7efad9146    cantidad 9
#P4 67cf055394c4c054c4efdf693ae5c84a    cantidad 10
#P5 10428de955b80b718a57e23130c16c4a    tablas,registros[]
#P6 a9427881b8866829c2d0ade046db31e3    registros tb2 3 atributos

#P7 10428de955b80b718a57e23130c16c4a
