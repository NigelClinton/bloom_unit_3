# import libaries
import sqlite3
import psycopg2
import pandas as pd

# Create SQLite DB?
df = pd.read_csv('titanic.csv')

# Create connection to database
conn = sqlite3.connect("titanic.sqlite3")

df.to_sql('titanic', conn)

# Create cursor
cur = conn.cursor()

# create rows for database
rows = cur.execute(
    "SELECT Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare from titanic;").fetchall()

# Create connection variables
dbname = "wtjnvyve"
user = "wtjnvyve"
password = "APZ5ovhYkyOh9P0ml48zitzoclq9mI0r"
host = "chunee.db.elephantsql.com"

# Create cursor object
cur = conn.cursor()

# Create titanic table -
cur.execute("""
    CREATE TABLE titanic (
        index SERIAL PRIMARY KEY,
        Survived INTEGER,
        Pclass INTEGER,
        Name VARCHAR(50),
        Sex VARCHAR(6),
        Age INTEGER,
        Siblings_Spouses_Aboard INTEGER,
        Parents_Children_Aboard INTEGER,
        Fare MONEY)
    """)
)

# assign values, then populate them using the insert variable function
# using the INSERT function
values=','.join(['%s'] * len * (rows))
insert_query='INSERT INTO titanic (Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare) values{}'.format(values)

# Cursor execute query command
cur.execute(insert_query, rows)

# specification for the table that the fetch function will be targeting
cur.execute("SELECT * FROM titanic;")

# Fetch all to show all records inserted using the functions above
cur.fetchall()

# Commit the changes / records inserted to the database
conn.commit()

# close connection
conn.close()
