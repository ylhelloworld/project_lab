import tinydb

def xinsert(data,table='_default',path='data/tiny.json'):
    db=tinydb.TinyDB(path)
    table=db.table(table)
    table.insert(data)

def xtable(table_name,path='data/tiny.json'):
    db=tinydb.TinyDB(path) 
    return db.table(table_name)