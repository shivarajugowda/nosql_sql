import happybase

connection = happybase.Connection(host='localhost')
connection.delete_table('mytable',disable=True)
connection.create_table(
    'mytable',
    {'cf1': dict(max_versions=10),
     'cf2': dict(max_versions=10),
     'cf3': dict(),  # use defaults
    }
)
table = connection.table('mytable')

table.put(b'row-key', {b'family:cf1': b'value1'})

row = table.row(b'row-key')
print(row[b'family:cf1'])  # prints 'value1'

for key, data in table.rows([b'row-key-1', b'row-key-2']):
    print(key, data)  # prints row key and data for each row

for key, data in table.scan(row_prefix=b'row'):
    print(key, data)  # prints 'value1' and 'value2'

row = table.delete(b'row-key')