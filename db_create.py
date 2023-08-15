
import sqlite3


def create_content_table():
    '''Function to create database and main content table'''
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS content (
                            id int AUTO_INCREMENT PRIMARY KEY,
                            name text NOT NULL,
                            content text NOT NULL)''')
    connection.commit()
    connection.close()


def insert_content():
    '''Function for initial filling of the table with content'''
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO content
                      VALUES
                      ('<id>', '<start_message>', '<response_after_ButtonPush>')
                   ''')
    connection.commit()
    connection.close()


def update_content():
    '''Function to change individual fields of a table'''
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('''UPDATE content
                      SET response = '<response_after_ButtonPush>'
                      WHERE id = <id>
                   ''')
    connection.commit()
    connection.close()



create_content_table()
insert_content()
# update_content()
