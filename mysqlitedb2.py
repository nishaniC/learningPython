import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo2.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def add_task(self):
        name = ""
        while (name is None) or (name == ''):
            name = input('Enter task name: ').strip()
            # print("name:",name)
        priority = 0
        while priority < 1:
            priority = int(input('Enter priority: '))
        if self.find_task(name) is None:
            self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
            self.conn.commit()

    def find_task(self, name):
        find=self.c.execute('SELECT * FROM tasks WHERE name = ?', (name,))
        find = find.fetchone()
        if find is None:
            return None
        else:
            return find

    def delete_task(self, name):
        # SQL statement called DELETE:
        # DELETE FROM table_name WHERE condition;
        # If you forget about the WHERE clause, all data in the table will be deleted.
        self.c.execute('DELETE FROM tasks WHERE name = ?', (name,))
        self.conn.commit()
    #   if no matching row then nothing get deleted self.c.rowcount is zero

    def show_tasks(self):
        self.c.execute('SELECT * FROM tasks')
        for row in self.c:
            print(row)

    def update_task(self, idid, priority):
        # SQL statement UPDATE is used to modify existing records in the database.
        # UPDATE table_name
        # SET column1 = value1, column2 = value2, column3 = value3, …, columnN = valueN
        # WHERE condition;
        # If you forget about the WHERE clause, all data in the table will be updated
        self.c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (priority, idid))
        self.conn.commit()
    #   if no matching row then nothing get updated self.c.rowcount is zero

app = Todo()

exit = 5
exit =int(input('Enter number 1 to quit, enter 2 to update, enter 3 to delete task, enter 4 to enter data: '))
while exit!=1:
    if exit==4:
        app.add_task()
        app.show_tasks()
    elif exit==3:
        myid = input('Enter task name: ').strip()
        app.delete_task(myid)
        app.show_tasks()
    elif exit==2:
        myid = int(input('Enter task id: ').strip())
        mypriority = int(input('Enter task priority: ').strip())
        app.update_task(myid,mypriority)
        app.show_tasks()
    exit = int(input('Enter number 1 to quit, enter 2 to update, enter 3 to delete task, enter 4 to enter data: '))