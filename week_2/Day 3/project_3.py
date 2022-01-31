#==================================================================================================
## IMPORT lIBRARIES ##

#import libraries
import pymongo
import sqlite3

#===================================================================================================
## ESTABLISH CONNECTION ##

#establish connection
client = pymongo.MongoClient("mongodb+srv://pmuserds30:Livelife1995@cluster0.i3uoh.mongodb.net/test?retryWrites=true&w=majority")

#confirm connection
client

#assign db
db = client.test

#check directory
dir(db.test)

#establish connection
s_conn = sqlite3.connect('rpg_db.sqlite3')

#create a cursor object
s_cur = s_conn.cursor()

#===================================================================================================
## charactercreator_character TABLE ##

#assigning the rows from the charactercreator_character
rows = s_cur.execute("SELECT * FROM charactercreator_character;").fetchall()

#List comprehention for creating columns in table
columns = [d[0] for d in s_cur.description]

#for loop to import the data into a list
charactercreator_character_doc = []
for row in rows:
    charactercreator_character_doc.append(dict(zip(columns,row)))

#insert many to populate the table
db.character.insert_many(charactercreator_character_doc)

#===================================================================================================
## charactercreator_character_inventory TABLE ##

#assigning the rows from the charactercreator_character_inventory 
rows = s_cur.execute("SELECT * FROM charactercreator_character_inventory;").fetchall()

#List comprehention for creating columns in table
columns = [d[0] for d in s_cur.description]

#for loop to import the data into a list
charactercreator_character_inventory_doc = []
for row in rows:
    charactercreator_character_inventory_doc.append(dict(zip(columns,row)))

#insert many to populate the table
db.character_inventory.insert_many(charactercreator_character_inventory_doc)

#===================================================================================================
## ARMORY ITEM TABLE ##

#assigning the rows from the armory item table
rows = s_cur.execute("SELECT name FROM armory_item;").fetchall()

#List comprehention for creating columns in table
columns = [d[0] for d in s_cur.description]

#for loop to import the data into a list
armory_item_doc = []
for row in rows:
    armory_item_doc.append(dict(zip(columns,row)))

#insert many to populate the table
db.armory_item.insert_many(armory_item_doc)

#===================================================================================================
## ARMORY WEAPON TABLE ##

#assigning the rows from the armory weapon table
rows = s_cur.execute("SELECT name FROM armory_weapon;").fetchall()

#List comprehention for creating columns in table
columns = [d[0] for d in s_cur.description]

#for loop to import the data into a list
armory_weapon_doc = []
for row in rows:
    armory_weapon_doc.append(dict(zip(columns,row)))

#insert many to populate the table
db.weapon_item.insert_many(armory_weapon_doc)

#===================================================================================================

## FINALIZE AND CLOSE CONNECTION ##

#Commit the changes / records inserted to the database
s_conn.commit()

#close connection
s_conn.close()
