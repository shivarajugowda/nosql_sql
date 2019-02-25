from cassandra.cluster import Cluster


def getMetadata():
    conn = getConnection()
    session = conn.connect()
    tables = [];
    rows = session.execute("SELECT * FROM system_schema.tables")
    for user_row in rows:
        keysp = user_row.keyspace_name;
        if not keysp.startswith("system"):
            tables.append(user_row.table_name)
    conn.shutdown()
    return tables;

def getConnection():
    return Cluster()

def getData(sqlString):
    conn = getConnection()
    session = conn.connect()
    rows = session.execute(sqlString)
    for user_row in rows:
        print user_row
    conn.shutdown()

d = getMetadata()
print(d)
getData("SELECT * FROM testkeyspace.myTable WHERE theKey='key4'")

