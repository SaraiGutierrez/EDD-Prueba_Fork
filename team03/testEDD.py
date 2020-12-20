# File:         JSON Mode Test File for EDD
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Luis Espino

from principalManager import BPlusMode as bp

# assume no data exist or execute the next drop function
#bp.dropAll()

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

'''
# test Registers CRUD
print(bp.insert('db1','tb1',[1,1]))              # 5
print(bp.insert('db1','tb1',['1','line','one']))   # 0
print(bp.loadCSV('tb1.csv','db1','tb1'))         # [0, 0, 0, 0, 0]
print(bp.extractTable('db1','tb1'))          
# [['1', 'line', 'one'], ['2', 'line', 'two'],
#  ['3', 'line', 'three'], ['4', 'line', 'four'],
#  ['5', 'line', 'five'], ['6', 'line', 'six']]
'''