import sqlite3
# # The SELECT statement allows you to read data from one or more tables. Its syntax looks like this:
# # SELECT column FROM table_name;
# # or
# # SELECT column1, column2, column3, …, columnN FROM table_name;
# # or
# # SELECT * FROM table_name;
# if mysqlitedb2.py is executed beforehand then tasks table will be there in the todo databaase and it  have data also
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# After calling the execute method with the appropriate SELECT statement, the Cursor object is treated as an iterator.
# The variable row in each iteration takes a row in the form of a tuple
# Access to individual columns is done using an index, e.g., print (row [0]) will display the values saved in the id column.
# for row in c.execute('SELECT * FROM tasks'):
#     print(row)

# The fetchall method is less efficient than the iterator, because it reads all records into the memory and then returns a list of tuples
# # The fetchall method returns an empty list when no rows are available
# c.execute('SELECT * FROM tasks')
# rows = c.fetchall()
# for row in rows:
#     print(row)

# The fetchone method returns None if there is no data to read
# fetchone retrieves the next available record
c.execute('SELECT * FROM tasks')
row = c.fetchone()
print(row)
row = c.fetchone()
print(row)
conn.close()

