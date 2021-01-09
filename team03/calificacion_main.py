from storageManager import unified_mode as um
import time
#inicio = time.time()
#Area para probar funciones
print("------------------Pruebas para Bases de datos-----------------------")
print("CREAR BD:", um.createDatabase("CALIFICAION", "b"), "Esperado:",0)
print("CREAR BD:", um.createDatabase("CALIFICAION", "bplus"), "Esperado:",2)
print("ALTER BD:", um.alterDatabase("CALIFICAION", "CAMBIADO"), "Esperado:",0)
print("ALTER BD:", um.alterDatabase("CALIFICAION", "CAMBIADO"), "Esperado:",2)
print("DROP BD:", um.dropDatabase("CALIFICACION"), "Esperado:", 2)
print("DROP BD:", um.dropDatabase("CAMBIADO"), "Esperado:", 0)
print("SHOW BD:", um.showTables("CAMBIADO"), "Esperado:", None)
print("CREAR BD:", um.createDatabase("calificacion", "avl"), "Esperado:",0)

print("------------------Pruebas para Tablas-----------------------")
print("---- Create Table ----")
print("CREAR TABLA:", um.createTable("calificacion","primaria",2),"Esperado:", 0)
print("CREAR TABLA:", um.createTable("calificacion2","primaria",2),"Esperado:", 2)
print("CREAR TABLA:", um.createTable("calificacion","primaria",2),"Esperado:", 3)
print("CREAR TABLA:", um.createTable("calificacion","primarias",3),"Esperado:", 0)
print("CREAR TABLA:", um.createTable("calificacion","change",1), "Esperado:", 0)

print("\n---- Alter Table ----")
print("ALTER TABLA:", um.alterTable("calificacion","change",'hiddenPK'),"Esperado:",0)
print("ALTER TABLA:", um.alterTable("calificacion2","change",'hiddenPK'),"Esperado:",2)
print("ALTER TABLA:", um.alterTable("calificacion","change",'hiddenPK'),"Esperado:",3)
print("ALTER TABLA:", um.alterTable("calificacion","hiddenPK",'hiddenPK'),"Esperado:",4)

print("\n---- Drop Table ----")
print("DROP TABLA:", um.dropTable('calificacion','hiddenPK'), "Esperado:", 0)
print("DROP TABLA:", um.dropTable('calificacion1','hiddenPK'), "Esperado:", 2)
print("DROP TABLA:", um.dropTable('calificacion','hiddenPK'), "Esperado:", 3)
print("CREAR TABLA:", um.createTable("calificacion","hiddenPK",2),"Esperado:", 0)

print("\n---- Add PK ----")
print("ADD PK:", um.alterAddPK("calificacion", "primaria",[7]), "Esperado:", 5)
print("ADD PK:", um.alterAddPK("calificacion", "primaria",[0]), "Esperado:", 0)
print("ADD PK:", um.alterAddPK("calificacion1", "primaria",[0]), "Esperado:", 2)
print("ADD PK:", um.alterAddPK("calificacion", "primaria1",[0]), "Esperado:", 3)
print("ADD PK:", um.alterAddPK("calificacion", "primaria",[0,1]), "Esperado:", 4)
print("ADD PKS:", um.alterAddPK("calificacion", "primarias",[0,1]), "Esperado:", 0)
print("ADD PKS:", um.alterAddPK("calificacion", "primarias",[0,1,3]), "Esperado:", 4)
print("SHOW TABLA:", um.showTables("calificacion"),"Esperado:","['primaria', 'primarias', 'hiddenPK']")

print("\n---- Insertar con una llave primaria----")
print("INSERT TABLA:", um.insert("calificacion","primaria",["t1x1","Andree"]), "Esperado:",0)
print("INSERT TABLA:", um.insert("calificacion1","primaria",["t1x1","Andree"]), "Esperado:",2)
print("INSERT TABLA:", um.insert("calificacion","primaria2",["t1x1","Andree"]), "Esperado:",3)
print("INSERT TABLA:", um.insert("calificacion","primaria",["t1x1","Andree"]), "Esperado:",4)
print("INSERT TABLA:", um.insert("calificacion","primaria",["t1x2"]), "Esperado:",5)
print("INSERT TABLA:", um.insert("calificacion","primaria",["t1x2","Andree","Avalos"]), "Esperado:",5)

print("\n---- Insertar con una llave compuesta----")
print("INSERT TABLA:", um.insert("calificacion","primarias",["t1","x1","Andree"]), "Esperado:",0)
print("INSERT TABLA:", um.insert("calificacion1","primarias",["t1","x1","Andree"]), "Esperado:",2)
print("INSERT TABLA:", um.insert("calificacion","primarias1",["t1","x1","Andree"]), "Esperado:",3)
print("INSERT TABLA:", um.insert("calificacion","primarias",["t1","x1","Andree"]), "Esperado:",4)
print("INSERT TABLA:", um.insert("calificacion","primarias",["t1","x2"]), "Esperado:",5)
print("INSERT TABLA:", um.insert("calificacion","primarias",["t1","x3","Andree","Avalos"]), "Esperado:",5)

print("\n---- Insertar con hiddenPK----")
print("INSERT TABLA:", um.insert("calificacion","hiddenPK",["Carlos","Andree"]), "Esperado:", 0)
print("INSERT TABLA:", um.insert("calificacion","hiddenPK",["Carlos","Andree"]), "Esperado:", 0)
print("INSERT TABLA:", um.insert("calificacion","hiddenPK",["Andree","Avalos"]), "Esperado:", 0)
print("INSERT TABLA:", um.insert("calificacion1","hiddenPK",["Andree","Avalos"]), "Esperado:", 2)
print("INSERT TABLA:", um.insert("calificacion","hiddenPK2",["Andree","Avalos"]), "Esperado:", 3)
print("INSERT TABLA:", um.insert("calificacion","hiddenPK",["Carlos","Avalos","Soto"]), "Esperado:", 5)

print("\n---- Drop PK ----")
print("DROP PK:", um.alterDropPK('calificacion1','primaria'), 'Esperado:', 2)
print("DROP PK:", um.alterDropPK('calificacion','primaria1'), 'Esperado:', 3)
print("DROP PK:", um.alterDropPK('calificacion','primaria'), 'Esperado:', 0)
print("DROP PK:", um.alterDropPK('calificacion','primaria'), 'Esperado:', 4)
print("INSERT TABLA:", um.insert("calificacion","primaria",["t1x1","Carlos"]), "Esperado:",0)
#Esto falta

print("ADD PK:", um.alterAddPK("calificacion", "primaria",[0]), "Esperado:", -1)
print("TUPLA TABLA:", um.extractTable("calificacion","primaria"), "Esperado:", "[['t1x1', 'Andree'], ['t1x1', 'Carlos']]")
print("DELETE TUPLA:", um.delete('calificacion','primaria',[1]),"Esperado:",0)
print("ADD PK:", um.alterAddPK("calificacion", "primaria",[0]), "Esperado:", 0)
print("TUPLA TABLA:", um.extractTable("calificacion","primaria"), "Esperado:", "[['t1x1', 'Andree']]")


print("\n---- Extract Table y Add Column ----")
print("TUPLA TABLA:", um.extractTable("calificacion","primarias"),"Esperado","[['t1','x1','Andree']]")
print("ADD COLUMN:", um.alterAddColumn('calificacion','primarias',True),"Esperado:",0)
print("ADD COLUMN:", um.alterAddColumn('calificacion1','primarias',True),"Esperado:",2)
print("ADD COLUMN:", um.alterAddColumn('calificacion','primarias2',True),"Esperado:",3)
print("TUPLA TABLA:", um.extractTable("calificacion","primarias"),"Esperado","[['t1','x1','Andree',True]]")
print("\n---- Drop Column ---")
print("DROP COLUMN:", um.alterDropColumn('calificacion1',"primarias",0),"Esperado:", 2)
print("DROP COLUMN:", um.alterDropColumn('calificacion',"primarias1",0),"Esperado:", 3)
print("DROP COLUMN:", um.alterDropColumn('calificacion',"primarias",0),"Esperado:", 4)
print("DROP COLUMN:", um.alterDropColumn('calificacion',"primarias",4),"Esperado:", 5)
print("DROP COLUMN:", um.alterDropColumn('calificacion',"primarias",3),"Esperado:", 0)
print("TUPLA TABLA:", um.extractTable("calificacion","primarias"),"Esperado","[['t1','x1','Andree']]")
#Esto falta

print("\n---- Extract Range Table ----") 
print("EXTRACTRANGE TABLA:", um.extractRangeTable("calificacion",'hiddenPK',0,'Andree','Andree'),"Esperado:","['Andree', 'Avalos']")


print("\n---- Load CSV ----")
print("CREAR TABLA:", um.createTable("calificacion","loadCSV",8), "Esperado:", 0)
print("CREAR PK:", um.alterAddPK('calificacion','loadCSV',[0]), "Esperado", 0)
print("LOAD CSV:",um.loadCSV("Estudiantes.csv","calificacion","loadCSV"),"Esperado: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]")

print("\n---- Extract Row ----")
print("EXTRACT ROW:", um.extractRow('calificacion','loadCSV',[42663506]))
print("Esperado:","['42663506', 'Rebecca', 'Sanchez', '83', 'id.mollis@placerataugueSed.com', '47522796', 'Belgium', 'Straubing'] ")
print("EXTRACT ROW:", um.extractRow('calificacion','loadCSV',[1]), "Esperado: []")

print("\n---- Update ----")
print("UPDATE TUPLA:", um.update('calificacion','loadCSV',{1:"Andree", 2:"Avalos"},[8106195]),"Esperado:",0)#Aqui no encuentra la llave por concatenacion de "|"
print("UPDATE TUPLA:", um.update('calificacion1','loadCSV',{1:"Andree", 2:"Avalos"},[8106195]),"Esperado:",2)
print("UPDATE TUPLA:", um.update('calificacion','loadCSV1',{1:"Andree", 2:"Avalos"},[8106195]),"Esperado:",3)
print("UPDATE TUPLA:", um.update('calificacion','loadCSV',{1:"Andree", 2:"Avalos"},[2]),"Esperado:",4)
print("EXTRACT ROW:", um.extractRow('calificacion','loadCSV',[8106195]))
print("Esperado:","['8106195', 'Andree', 'Avalos', '26','vulputate.eu@mus.edu', '15466003', 'Sint Maarten', 'Dubuisson'] ")

print("\n---- Delete ----")
print("DELETE TUPLA:", um.delete('calificacion','loadCSV',[12471376]),"Esperado:",0)
print("DELETE TUPLA:", um.delete('calificacion1','loadCSV',[12471376]),"Esperado:",2)
print("DELETE TUPLA:", um.delete('calificacion','loadCSV1',[12471376]),"Esperado:",3)
print("DELETE TUPLA:", um.delete('calificacion','loadCSV',[12471376]),"Esperado:",4)
print("\b---- Truncate ----")
print("TRUNCATE TABLE:", um.truncate('calificacion', 'loadCSV'), "Esperado:", 0)
print("TRUNCATE TABLE:", um.truncate('calificacion1', 'loadCSV'), "Esperado:", 2)
print("TRUNCATE TABLE:", um.truncate('calificacion', 'loadCSV1'), "Esperado:", 3)
print("SHOW TABLE:", um.extractTable('calificacion','loadCSV'), "Esperado:",[])


#final = time.time()
#print("------------------------------------------------------------------")
#print("Tiempo de Ejecucion:", final-inicio, "segundos")




