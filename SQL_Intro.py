''' This file introduces the basic concept of SQL to be used with Python'''

import sqlite3

# creating a database and a connection
# the below code creates a new database every time you run the code
connection = sqlite3.connect('data.db')

# creating cursor
CURSOR = connection.cursor()

# creating table
create_table = "CREATE TABLE users (id int,username text, password text)"
CURSOR.execute(create_table)

# saving the changes
connection.commit()

# closing the connection
connection.close()