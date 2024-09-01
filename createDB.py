import sqlite3


conn = sqlite3.connect('data.db')
c = conn.cursor()


with open('create_tables.sql', 'r') as sql_file:
    sql_script = sql_file.read()
c.executescript(sql_script)


conn.commit()
conn.close()

print("Database and tables created successfully.")
