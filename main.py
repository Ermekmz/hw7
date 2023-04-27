import sqlite3
from sqlite3 import Error as e


# CRUD create raed update delete

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except e:
        print(e)


def create_student(conn, student):
    sql = '''INSERT INTO student(fullname,hobby,mark,date_b,is_married)
    VALUES (?,?,?,?,?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except e:
        print(e)


def reed_student(conn):
    try:
        sql = '''SELECT * FROM student'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except e:
        print(e)


def update_student(conn, id, name):
    sql = '''UPDATE student SET fullname=? WHERE id=?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,(name,id))
        conn.commit()
    except e:
        print(e)

def delete_student(conn, id):
    sql = '''DELETE from student WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except e:
        print(e)


database = 'test.db'

sql_create_table = '''
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname varchar (102) NOT NULL,
hobby TEXT DEFAULT NULL,
mark DOUBLE (3,2) NOT NULL DEFAULT 0.0,
date_b DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE 
);
'''

connection = create_connection(database)

if connection is not None:
    print('все работает')
    # create_table(connection, sql_create_table)
    # create_student(connection, ('Sultan', None, 44.4, '2000-01-05', True))
    # create_student(connection, ('Sulan', '', 44.4, '2000-01-05', True))
    update_student(connection,5,'NUr')
    reed_student(connection)
    delete_student(connection,9)



