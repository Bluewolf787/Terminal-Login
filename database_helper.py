import sqlite3


# This function is used to connect to the DB
def connect():
    try:
        return sqlite3.connect('test.db') # Return the connection
    except (Exception, sqlite3.ProgrammingError) as error:
        print(error)


# This function is used to create a users table in the DB
def create_users_table():
    try:
        connection = connect() # Create a connection to the DB
        cursor = connection.cursor() # Create a SQLite cursor object

        # Create the table
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL UNIQUE,
            username TEXT NOT NULL UNIQUE,
            key BLOB NOT NULL,
            salt BLOB NOT NULL,
            PRIMARY KEY(id AUTOINCREMENT))''')
        connection.commit() # Save (commit) changes to the DB
        connection.close() # Close the connection to the DB
    except (Exception, sqlite3.ProgrammingError) as error:
        print('SQL Error: %s' % error)


# This function is used to store data in the users table
def save_user(username, key, salt):
    try:
        connection = connect() # Create a connection to the DB
        cursor = connection.cursor() # Create a SQLite cursor object

        # Store a new user in the table users with username and the key and salt from hashed password
        cursor.execute('INSERT INTO users (username, key, salt) VALUES (?, ?, ?)', (username, key, salt,))  
        connection.commit() # Save (commit) changes to the DB
        connection.close() # Close the connection to the DB
    except (Exception, sqlite3.ProgrammingError) as error:
        print('SQL Error: %s' % error)


# This function is used to check if a specific username is in the table users
def check_username(username):
    try:
        connection = connect() # Create a connection to the DB
        cursor = connection.cursor() # Create a SQLite cursor object

        # Select the id from the row with the specific username
        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        data = cursor.fetchone() # Store the tuple from the SQL query in the variable data
        connection.close() # Close the connection to the DB

        if data is None: # Check if the data variable has a value
            return False # If not then return False
        else:
            return True # Else return True
    except (Exception, sqlite3.ProgrammingError) as error:
        print('SQL Error: %s' % error)


# This function is used to get the key for a specific user
def get_key(username):
    try:
        connection = connect() # Create a connection to the DB
        cursor = connection.cursor() # Create a SQLite cursor object

        # Select the key from the row with the specific username
        cursor.execute('SELECT key FROM users WHERE username = ?', (username,))
        key = cursor.fetchone() # Store the tuple from the SQL query in the variable key
        connection.close() # Close the connection to the DB
        return key[0] # Return the first value from the tuple variable key
    except (Exception, sqlite3.ProgrammingError) as error:
        print('SQL Error: %s' % error)


# This function is used to get the salt for a specific user
def get_salt(username):
    try:
        connection = connect() # Create a connection to the DB
        cursor = connection.cursor() # Create a SQLite cursor object
        
        # Select the salt from the row with the specific username
        cursor.execute('SELECT salt FROM users WHERE username = ?', (username,))
        salt = cursor.fetchone() # Store the tuple from the SQL query in the variable salt
        connection.close() # Close the connection to the DB
        return salt[0] # Return the first value from the tuple variable salt
    except (Exception, sqlite3.ProgrammingError) as error:
        print('SQL Error: %s' % error)