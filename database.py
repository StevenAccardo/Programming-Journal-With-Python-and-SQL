import sqlite3

connection = sqlite3.connect('data.db')
connection.row_factory = sqlite3.Row

def create_table():
    # Can either explicitly commit the transaction manually using connection.commit() or you can use the "with" keyword to leverage python's context manager to handle that for us.
    with connection:
        # In SQlite its standard to use fonnection.cursor() to intereact with the DB, however connection.execute() creates a cursor for you, so its not needed in this case.
        connection.execute('CREATE TABLE IF NOT EXISTS entries (content Text, date Text);')

def add_entry(entry_content, entry_date):
    with connection:
        # This syntax is used instead of string interpolation. This is still very similar, but it allows sqlite to parse the data to prevent insertion of any nefarious code.
        connection.execute("INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date))

def get_entries():
    cursor = connection.execute("SELECT * FROM entries")
    return cursor