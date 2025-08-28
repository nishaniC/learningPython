import sqlite3
# The standard Python library has a module called sqlite3, providing an interface compliant with the DB-API 2.0 specification described by PEP 249.
# The purpose of the DB-API 2.0 specification is to define a common standard for creating modules to work with databases in Python.

# The connect method returns the database representation as a Connection object
# the database will be created in the same directory as the script that wants to access it
conn = sqlite3.connect('todo.db')

# conn = sqlite3.connect('C:\sqlite\hello.db')
# It's also possible to use a special name, :memory:, which creates a database in RAM:
# conn = sqlite3.connect(':memory:')
# Remember that the connect method creates a database only if it cannot find a database in the given location with the given name. If a database exists, SQLite connects to it.

# The cursor method creates a Cursor object that allows any SQL statements to be executed in the database.
c = conn.cursor()

# SQL statement
# CREATE TABLE table_name (
# column1 datatype,
# column2 datatype,
# column3 datatype,
# …
# columnN datatype
# );

# Calling the execute method executes the CREATE TABLE statement in our database.
# The execute method takes any single SQL statement and optional parameters necessary to execute the query.
# NOTE: Running the below part twice will throw an exception with the following message: sqlite3.OperationError: table tasks already exists.
# c.execute('''CREATE TABLE tasks (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# priority INTEGER NOT NULL
# );''')

c.execute('''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')

# The INSERT INTO sql statement is used to insert records in a table. Its syntax is as follows:
#
# INSERT INTO table_name (column1, column2, column3, ..., columnN)
# VALUES (value1, value2, value3, ..., value4);
# id column can be omitted. In that case, we inform the database management system of the desire to use auto-incrementation (a unique value is generated for us when a new record is inserted).
# The INSERT INTO statement also has a short form in which we can omit the column names:
# INSERT INTO table_name VALUES (value1, value2, value3, ..., valueN);

# This is to avoid an SQL injection attack in which malicious SQL is appended to a query that could possibly destroy our database.
# Restarting the program will create another task with the same name and priority, but with a different id that is auto-incremental.
c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My first task', 1))


tasks = [
    ('My first task', 1),
    ('My second task', 5),
    ('My third task', 10),
]
c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)

# The commit method confirms our changes (the current transaction). If you forget to call it, your changes won't be visible in the database.
conn.commit()

# closes the database connection
conn.close()