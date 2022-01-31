#import libaries
import sqlite3

#Create SQLite DB?

#Create connection to database
s_conn = sqlite3.connect("buddymove_holidayiq.sqlite3")

#Create cursor
s_cur = s_conn.cursor()

#close connection
s_conn.close()
