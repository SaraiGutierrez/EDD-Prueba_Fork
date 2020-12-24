# File:         JSON Mode Test File for EDD
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Luis Espino

from principalManager import BPlusMode as bp
'''
# create database
print(bp.createDatabase('world'))

# create tables
print(bp.createTable('world', 'countries', 4))
print(bp.createTable('world', 'cities',    4))
print(bp.createTable('world', 'languages', 4))

# create simple primary keys
print(bp.alterAddPK('world', 'countries', [0]))
print(bp.alterAddPK('world', 'cities',    [0]))
print(bp.alterAddPK('world', 'languages', [0, 1]))

# insert data in countries
print(bp.insert('world', 'countries', ['GTM', 'Guatemala',  'Central America', 108889]))
print(bp.insert('world', 'countries', ['SLV', 'El Salvado', 'Central America',  21041]))  

# insert data in cities
print(bp.insert('world', 'cities', [1, 'Guatemala',    'Guatemala',    'GTM']))
print(bp.insert('world', 'cities', [2, 'Cuilapa',      'Santa Rosa',   'GTM']))
print(bp.insert('world', 'cities', [3, 'San Salvador', 'San Salvador', 'SLV']))
print(bp.insert('world', 'cities', [4, 'San Miguel',   'San Miguel',   'SLV']))
         
# inser data in languages
print(bp.insert('world', 'languages', ['GTM', 'Spanish', 'official',  64.7]))
print(bp.insert('world', 'languages', ['SLV', 'Spanish', 'official', 100.0]))

bp.server.serializar()
'''

#bp.server.deserializar()
#print()
#print(bp.showTables('world'))
#print()
#print(bp.extractTable('world','countries'))
#bp.server.generarReporteBMasPlus('world', 'cities')

# test Databases CRUD
print(bp.createDatabase('db1'))      # 0 
print(bp.createDatabase('db1'))      # 2
print(bp.createDatabase('db4'))      # 0
print(bp.createDatabase('db5'))      # 0
print(bp.createDatabase(0))          # 1
print(bp.alterDatabase('db5','db1')) # 3
print(bp.alterDatabase('db5','db2')) # 0
#print(bp.dropDatabase('db4'))        # 0
print(bp.showDatabases())            # ['db1','db2']

# test Tables CRUD
print(bp.createTable('db1','tb4',3))     # 0
print(bp.createTable('db1','tb4',3))     # 3
print(bp.createTable('db1','tb1',3))     # 0
print(bp.createTable('db1','tb2',3))     # 0
print(bp.alterTable('db1','tb4','tb3'))  # 0
print(bp.dropTable('db1','tb3'))         # 0
print(bp.alterAddPK('db1','tb1',0))      # 1
print(bp.alterAddPK('db1','tb1',[2]))    # 0
print(bp.showTables('db1'))              # ['tb1', 'tb2']

# test Registers CRUD
#print(bp.insert('db1','tb1',[1,1]))              # 5
#print(bp.insert('db1','tb1',['1','line','one']))   # 0
#print(bp.insert('db1','tb1',['2','line','two']))   # 0
#print(bp.insert('db1','tb1',['3','line','three']))   # 0
#print(bp.insert('db1','tb1',['4','line','four']))   # 0
#print(bp.insert('db1','tb1',['5','line','five']))   # 0
#print(bp.insert('db1','tb1',['6','line','six']))   # 0
#print(bp.loadCSV('tb1.csv','db1','tb1'))         # [0, 0, 0, 0, 0]
print(bp.extractTable('db1','tb1'))          
# [['1', 'line', 'one'], ['2', 'line', 'two'],
#  ['3', 'line', 'three'], ['4', 'line', 'four'],
#  ['5', 'line', 'five'], ['6', 'line', 'six']]
print(bp.extractRangeTable('db1', 'tb1', 2, 1, 4))
print(bp.alterAddColumn('db1', 'tb1', "Nueva columna"))
print(bp.extractTable('db1','tb1'))
#print(bp.alterDropColumn('db1', 'tb1', 1))
#print(bp.extractTable('db1','tb1'))
#bp.server.generarReporteBMasPlus('db1', 'tb1')
print(bp.extractRow('db1', 'tb1', ['three']))
print(bp.truncate('db1', 'tb1'))
print(bp.extractTable('db1','tb1'))


bp.server.serializar()

#bp.server.deserializar()
#print()
#print(bp.showDatabases())            # ['db1','db2']
#print()
#print(bp.showTables('db1'))              # ['tb1', 'tb2']
#print()
#print(bp.extractTable('db1','tb1'))          
# [['1', 'line', 'one'], ['2', 'line', 'two'],
#  ['3', 'line', 'three'], ['4', 'line', 'four'],
#  ['5', 'line', 'five'], ['6', 'line', 'six']]

#bp.server.generarReporteBMasPlus('db1', 'tb1')
'''
# test Databases CRUD
print(bp.createDatabase('db1'))      # 0 
print(bp.createDatabase('db1'))      # 2

# test Tables CRUD
print(bp.createTable('db1','tb4',3))     # 0
print(bp.createTable('db1','tb4',3))     # 3
print(bp.createTable('db1','tb1',3))     # 0
print(bp.createTable('db1','tb2',3))     # 0
print(bp.alterTable('db1','tb4','tb3'))  # 0
print(bp.dropTable('db1','tb3'))         # 0
#print(bp.alterAddPK('db1','tb1',0))      # 1
#print(bp.alterAddPK('db1','tb1',[0]))    # 0
print(bp.showTables('db1'))              # ['tb1', 'tb2']

print(bp.createDatabase('db4'))      # 0
print(bp.createDatabase('db5'))      # 0
print(bp.createDatabase('db10'))      # 0
print(bp.createDatabase('db3'))      # 0
print(bp.createDatabase('db15'))      # 0
print(bp.createDatabase(0))          # 1
print(bp.alterDatabase('db5','db1')) # 3
print(bp.alterDatabase('db1','db2')) # 0
print(bp.dropDatabase('db4'))        # 0
print(bp.showDatabases())            # ['db2','db3','db5','db10','db15']

print(bp.showTables('db2'))              # ['tb1', 'tb2']


# test Registers CRUD
print(bp.insert('db1','tb1',[1,1]))              # 5
print(bp.insert('db1','tb1',['1','line','one']))   # 0
print(bp.loadCSV('tb1.csv','db1','tb1'))         # [0, 0, 0, 0, 0]
print(bp.extractTable('db1','tb1'))          
# [['1', 'line', 'one'], ['2', 'line', 'two'],
#  ['3', 'line', 'three'], ['4', 'line', 'four'],
#  ['5', 'line', 'five'], ['6', 'line', 'six']]
'''

#Tipo de archivo para el informe de B+
#dot -Tsvg archivo.dot -o salida.svg