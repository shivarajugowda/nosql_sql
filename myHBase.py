import simpleSQL
import happybase


def getMetadata():
    conn = getConnection()
    meta = conn.tables()
    conn.close();
    return meta

def getConnection():
    return happybase.Connection(host='localhost')


def getData(sqlString):
    conn = getConnection()
    sql = simpleSQL.simpleSQL.parseString(sqlString)
    tableName = sql.tables[0].lower()

    table = conn.table(tableName)
    for key, data in table.scan():
        print(key, data)

    conn.close()


d = getMetadata()
print(d)
getData("SELECT * FROM test")