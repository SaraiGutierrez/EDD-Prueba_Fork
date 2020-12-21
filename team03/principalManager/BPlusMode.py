# Package:      B+ Mode
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Herberth Avila

from storageManager.BPlusServer import BPlusServer

server = BPlusServer()

##################
# Databases CRUD #
##################

# CREATE a database checking their existence
def createDatabase(database: str) -> int:
    try:
        if not database.isidentifier():
            raise Exception()
        #initCheck()
        #data = read(dataPath)
        #if database in data:
            #return 2
        existe = server.existeDB(database)
        if existe:
            return 2
        server.createDB(database)
        ##data.update(new)
        ##write(dataPath, data)
        return 0
    except:
        return 1

# READ and show databases by constructing a list
def showDatabases() -> list:
    try:
        #initCheck()
        databases = []
        #data = read(dataPath)
        #for d in data:
            #databases.append(d)
        databases = server.showDB()
        return databases
    except:
        return []

# UPDATE and rename a database name by inserting new_key and deleting old_key
def alterDatabase(databaseOld: str, databaseNew) -> int:
    try:
        if not databaseOld.isidentifier() or not databaseNew.isidentifier():
            raise Exception()
        #initCheck()
        #data = read(dataPath)        
        #if not databaseOld in data:
            #return 2
        #if databaseNew in data:
            #return 3
        #data[databaseNew] = data[databaseOld]
        #data.pop(databaseOld)
        #write(dataPath, data)
        existe = server.existeDB(databaseOld)
        if existe is False:
            return 2
        existe = server.existeDB(databaseNew)
        if existe:
            return 3
        server.alterDB(databaseOld, databaseNew)
        return 0
    except:
        return 1

# DELETE a database by pop from dictionary
def dropDatabase(database: str) -> int:
    try:
        if not database.isidentifier():
            raise Exception()
        #initCheck()
        #data = read(dataPath)
        #if not database in data:
            #return 2
        #data.pop(database)
        #write(dataPath, data)
        existe = server.existeDB(database)
        if existe is False:
            return 2
        server.dropDB(database)
        return 0
    except:
        return 1    


###############
# Tables CRUD #
###############

# CREATE a table checking their existence
def createTable(database: str, table: str, numberColumns: int) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(numberColumns, int):
            raise Exception()
        #initCheck()
        #data = read(dataPath)
        #if not database in data:
            #return 2        
        #if table in data[database]:
            #return 3
        #new = {table:{"NCOL":numberColumns}}
        #data[database].update(new)
        #write(dataPath, data)
        #dataTable = {}
        #write(path+database+'-'+table, dataTable)
        existe = server.existeDB(database)
        if existe is False:
            return 2
        existe = server.existeTabla(database, table)
        if existe:
            return 3
        server.createT(database, table, numberColumns)
        return 0
    except:
        return 1

# show databases by constructing a list
def showTables(database: str) -> list:
    try:
        if not database.isidentifier():
            raise Exception()
        #initCheck()
        tables = []        
        #data = read(dataPath)
        #if not database in data:
            #return None
        #for d in data[database]:
            #tables.append(d);
        existe = server.existeDB(database)
        if existe is False:
            return None
        tables = server.showT(database)
        return tables
    except:
        return []

# extract all register of a table
def extractTable(database: str, table: str) -> list:
    try:
        #initCheck()
        rows = []
        #data = read(dataPath)
        #if not database in data:
            #return None
        #if table not in data[database]:
            #return None
        #data = read(path+database+'-'+table)
        #for d in data:
            #rows.append(data[d]);
        existe = server.existeDB(database)
        if existe is False:
            return None
        existe = server.existeTabla(database, table)
        if existe is False:
            return None
        rows = server.extractT(database, table)
        return rows
    except:
        return None


# extract a range registers of a table
def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    #initCheck()
    #rows = []
    #with open('data/json/databases') as file:
        #data = json.load(file)
        #if not database in data:
            #return rows
        #else: 
            #if table not in data[database]:
                #return rows
    #with open('data/json/'+database+'-'+table) as file:
        #data = json.load(file)
        #for d in data:
            #if (str(d)<=str(upper) and str(d)>=str(lower)):
                #rows.append(data[d])
    #return rows
    try:
        rows = []

        existe = server.existeDB(database)
        if existe is False:
            return None
        existe = server.existeTabla(database, table)
        if existe is False:
            return None
        rows = server.extractRangeT(database, table, columnNumber, lower, upper)
        return rows
    except:
        return None
'''
# Add a PK list to specific table and database
def alterAddPK(database: str, table: str, columns: list) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(columns, list):
            raise Exception()
        initCheck()
        data = read(dataPath)
        if not database in data:
            return 2
        if not table in data[database]:
            return 3
        if "PKEY" in data[database][table]:
            return 4
        maxi = max(columns)
        mini = min(columns)
        if not (mini>=0 and maxi<data[database][table]["NCOL"]):
            return 5
        new = {"PKEY":columns}
        data[database][table].update(new)
        write(dataPath, data)
        return 0
    except:
        return 1  

# Add a PK list to specific table and database
def alterDropPK(database: str, table: str) -> int:
    initCheck()
    dump = False
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            if "PKEY" not in data[database][table]:
                return 4            
            else:
                data[database][table].pop("PKEY")
                dump = True
    if dump:
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1  

'''
# Rename a table name by inserting new_key and deleting old_key
def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    try:
        if not database.isidentifier() \
        or not tableOld.isidentifier() \
        or not tableNew.isidentifier() :
            raise Exception()        
        #initCheck()
        #data = read(dataPath)
        #if not database in data:
            #return 2
        #if not tableOld in data[database]:
            #return 3
        #if tableNew in data[database]:
            #return 4            
        #data[database][tableNew] = data[database][tableOld]
        #data[database].pop(tableOld)
        #write(dataPath, data)
        existe = server.existeDB(database)
        if existe is False:
            return 2
        existe = server.existeTabla(database, tableOld)
        if existe is False:
            return 3
        existe = server.existeTabla(database, tableNew)
        if existe:
            return 4
        server.alterT(database, tableOld, tableNew)
        return 0
    except:
        return 1   

# add a column at the end of register with default value
def alterAddColumn(database: str, table: str, default: any) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier():
            raise Exception()  

        existe = server.existeDB(database)
        if existe is False:
            return 2
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3
        server.alterAddC(database, table, default)
        return 0
    except:
        return 1

    #initCheck()
    #dump = False
    #with open('data/json/databases') as file:
        #data = json.load(file)
        #if not database in data:
            #return 2
        #else:
            #if not table in data[database]:
                #return 3
            #data[database][table]['NCOL']+=1
            #dump = True
    #if dump:
        #with open('data/json/databases', 'w') as file:
            #json.dump(data, file)

        #with open('data/json/'+database+'-'+table) as file:
            #data = json.load(file)
            #for d in data:
                #data[d].append(default)
        #with open('data/json/'+database+'-'+table, 'w') as file:
            #json.dump(data, file)
        #return 0
    #else:
        #return 1  

# drop a column and its content (except primary key columns)
def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(columnNumber, int):
            raise Exception()  

        existe = server.existeDB(database)
        if existe is False:
            return 2
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3

        return server.alterDropC(database, table, columnNumber)
    except:
        return 1
      
# Delete a table name by inserting new_key and deleting old_key
def dropTable(database: str, table: str) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() :
            raise Exception()             
        #initCheck()
        #data = read(dataPath)
        #if not database in data:
            #return 2
        #if not table in data[database]:
            #return 3
        #data[database].pop(table)
        #write(dataPath,data)
        existe = server.existeDB(database)
        if existe is False:
            return 2
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3
        server.dropT(database, table)
        return 0
    except:
        return 1  

##################
# Registers CRUD #
##################

# CREATE or insert a register 
def insert(database: str, table: str, register: list) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(register, list):
            raise Exception()        
        #initCheck()
        #hide = False
        #ncol = None
        #pkey = None
        #pk = ""
        #data = read(dataPath)
        #if not database in data:
            #return 2
        #if table not in data[database]:
            #return 3
        #if len(register)!=data[database][table]["NCOL"]:
            #return 5
        #if "PKEY" not in data[database][table]:
            # hidden pk
            #hide = True
        #else:
            # defined pk
            #pkey = data[database][table]["PKEY"]
            #ncol = data[database][table]["NCOL"]
        #data = read(path+database+'-'+table)
        #if hide:
            #pk = len(data)
        #else:
            #for i in pkey:
                #pk += str(register[i])+'|'
        #if pk in data:
            #return 4
        #new = {pk:register}
        #data.update(new)
        #write(path+database+'-'+table, data)
        existe = server.existeDB(database)
        if existe is False:
            return 2
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3

        return server.insert(database, table, register)
    except:
        return 1

# READ or load a CSV file to a table
def loadCSV(filepath: str, database: str, table: str) -> list:
    try:
        res = []
        #import csv
        #with open(filepath, 'r') as file:
            #reader = csv.reader(file, delimiter = ',')
            #for row in reader:
                #res.append(insert(database,table,row))
        res = server.cargarCSV(filepath, database, table)
        return res
    except:
        return []

# READ or extract a register
def extractRow(database: str, table: str, columns: list) -> list:
    try:
        res = []
        
        existe = server.existeDB(database)
        if existe is False:
            return []
        existe = server.existeTabla(database, table)
        if existe is False:
            return []
        res = server.extractR(database, table, columns)
        return res
    except:
        return []

    #initCheck()
    #hide = False
    #ncol = None
    #pkey = None
    #pk = ""
    #with open('data/json/databases') as file:
        #data = json.load(file)
        #if not database in data:
            #return []
        #else: 
            #if table not in data[database]:
                #return []
            #if "PKEY" not in data[database][table]:
                # hidden pk
                #hide = True
            #else:
                # defined pk
                #pkey = data[database][table]["PKEY"]            
    #with open('data/json/'+database+'-'+table) as file:
        #data = json.load(file)
        #if hide:
            #pk = columns[0]
        #else:
            #for i in pkey:
                #pk += str(columns[i])
        #if not pk in data:
            #return []
        #else:
            #return data[pk]

# UPDATE a register
def update(database: str, table: str, register: dict, columns: list) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier():
            raise Exception()        
        
        existe = server.existeDB(database)
        if existe is False:
            return 2
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3

        return server.actualizarDatos(database, table, register, columns)
    except:
        return 1
    
    #initCheck()
    #dump = False
    #hide = False
    #ncol = None
    #pkey = None
    #pk = ""
    #with open('data/json/databases') as file:
        #data = json.load(file)
        #if not database in data:
            #return 2
        #else: 
            #if table not in data[database]:
                #return 3
            #if "PKEY" not in data[database][table]:
                # hidden pk
                #hide = True
            #else:
                # defined pk
                #pkey = data[database][table]["PKEY"]            
    #with open('data/json/'+database+'-'+table) as file:
        #data = json.load(file)
        #if hide:
            #pk = columns[0]
        #else:
            #for i in pkey:
                #pk += str(columns[i])
        #if not pk in data:
            #return 4
        #else:            
            #for key in register:
                #data[pk][key] = register[key]
        #dump = True
    #if dump:
        #with open('data/json/'+database+'-'+table, 'w') as file:
            #json.dump(data, file)
        #return 0
    #else:
        #return 1

# DELETE a specific register
def delete(database: str, table: str, columns: list) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier():
            raise Exception()        
        
        existe = server.existeDB(database)
        if existe is False:
            return 2
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3

        return server.eliminarRegistro(database, table, columns)
    except:
        return 1
    #initCheck()
    #dump = False
    #hide = False
    #ncol = None
    #pkey = None
    #pk = ""
    #with open('data/json/databases') as file:
        #data = json.load(file)
        #if not database in data:
            #return 2
        #else: 
            #if table not in data[database]:
                #return 3
            #if "PKEY" not in data[database][table]:
                # hidden pk
                #hide = True
            #else:
                # defined pk
                #pkey = data[database][table]["PKEY"]            
    #with open('data/json/'+database+'-'+table) as file:
        #data = json.load(file)
        #if hide:
            #pk = columns[0]
        #else:
            #for i in pkey:
                #pk += str(columns[i])
        #if not pk in data:
            #return 4
        #else:
            #data.pop(pk)
        #dump = True
    #if dump:
        #with open('data/json/'+database+'-'+table, 'w') as file:
            #json.dump(data, file)
        #return 0
    #else:
        #return 1

# DELETE or truncate all registers of the table
def truncate(database: str, table: str) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() :
            raise Exception()             
        
        existe = server.existeDB(database)
        if existe is False:
            return 2
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3
        server.truncateT(database, table)
        return 0
    except:
        return 1
    #initCheck()
    #dump = False
    #hide = False
    #ncol = None
    #pkey = None
    #pk = ""
    #with open('data/json/databases') as file:
        #data = json.load(file)
        #if not database in data:
            #return 2
        #else: 
            #if table not in data[database]:
                #return 3
        #dump = True
    #if dump:
        #data = {}
        #with open('data/json/'+database+'-'+table, 'w') as file:
            #json.dump(data, file)
            #return 0
    #else:
        #return 1

def showRegister(database: str, table: str):
    server.generarReporteBMasPlus(database, table)
'''
#############
# Utilities #
#############

# Check the existence of data and json folder and databases file
# Create databases files if not exists
def initCheck():
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('data/json'):
        os.makedirs('data/json')
    if not os.path.exists('data/json/databases'):
        data = {}
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)

# Read a JSON file
def read(path: str) -> dict:
    with open(path) as file:
        return json.load(file)    

# Write a JSON file
def write(path: str, data: dict):
    with open(path, 'w') as file:
        json.dump(data, file)



# Show the complete file of databases and tables
def showJSON(fileName: str):
    initCheck()
    with open('data/json/'+fileName) as file:
        data = json.load(file)
        print(data)

# Delete all databases and tables by creating a new file
def dropAll():
    initCheck()
    data = {}
    with open('data/json/databases', 'w') as file:
        json.dump(data, file)

# show all collection of relational data
def showCollection():
    initCheck()
    databases = []
    tables = []
    datatables = []
    with open('data/json/databases') as file:
        data = json.load(file)
        for d in data:
            databases.append(d);
            for t in data[d]:
                tables.append(t)
                datatables.append(d+'-'+t)
    print('Databases: '+str(databases))
    print('Tables: '+str(tables))
    for d in datatables:
        registers = []
        with open('data/json/'+d) as file:
            data = json.load(file)
            for r in data:
                registers.append(r)
            print(d+' pkeys: '+str(registers))

'''