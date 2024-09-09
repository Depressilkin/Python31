import sqlite3 as sq
with sq.connect('C:/Users/Преподаватель/Documents/python31/Python31/Saloon/DataBase.db') as con:
    cur = con.cursor()
    cur.execute('''
CREATE TABLE IF NOT EXISTS products(
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    name TEXT NOT NULL)
''')
    con.commit()
    cur.execute('''
CREATE TABLE IF NOT EXISTS masters(
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    name TEXT NOT NULL,
    phone TEXT NOT NULL)
''')
    con.commit()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS clients(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    discount REAL NOT NULL DEFAULT 0)
''')
    con.commit()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS service(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    date TEXT NOT NULL,
    id_product TEXT NOT NULL,
    id_client INTEGER NOT NULL,
    id_master TEXT NOT NULL,
    price REAL NOT NULL,
    amount  REAL NOT NULL,
    salary REAL NOT NULL,
    profit REAL NOT NULL,            
    FOREIGN KEY (id_product) REFERENCES products(id),
    FOREIGN KEY (id_client) REFERENCES client(id),
    FOREIGN KEY (id_master) REFERENCES masters(id))
''')
    con.commit()