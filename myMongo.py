import simpleSQL
from pymongo import MongoClient
import json

def getMetadata():
    conn = getConnection()
    meta = dict((db, [collection for collection in conn[db].list_collection_names()])
             for db in conn.list_database_names())
    conn.close();
    return meta

def getConnection():
    return MongoClient()

def getData(sqlString):
    conn = getConnection()
    sql = simpleSQL.simpleSQL.parseString(sqlString)
    tableName = sql.tables[0].lower()
    names = tableName.split('.')
    data = conn[names[0]][names[1]]

    filters = {}
    for fil in sql.where[0]:
        if fil[1] is '=':
            filters[fil[0].lower()] = fil[2].replace('"','').replace('\'','')

    selects = {'_id':0}
    if not sql.columns[0] == '*' :
        for sel in sql.columns[0]:
            print(sel)
            selects[sel.lower()] = 1;

    for d in data.find(filters,selects):
        print(d)

    conn.close()


d = getMetadata()
print(json.dumps(d))
getData("select city, pop from test.zips where city='HYDER'")