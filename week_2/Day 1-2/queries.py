#the charactercreator_* and armory_* tables and where you should focus your attention.
#armory_item and charactercreator_character are the main tables for Items and Characters respectively
#the other tables are subsets of them by type (i.e. subclasses), connected via a key (item_id and character_id).
#===============================================================================================================

#TOTAL_CHARACTERS: How many total Characters are there?
SELECT COUNT(cc.character_id) TOTAL_CHARACTERS
FROM charactercreator_character cc;

#TOTAL_SUBCLASS: How many of each specific subclass (the necromancer table)?
SELECT COUNT(ccn.mage_ptr_id) TOTAL_SUBCLASS 
FROM charactercreator_necromancer ccn;

#TOTAL_ITEMS: How many total Items?
SELECT COUNT(ai.item_id) FROM armory_item ai;

#WEAPONS: How many of the Items are weapons? - Specify the weapons table
SELECT COUNT(ai.item_id) 
FROM armory_weapon aw LEFT JOIN armory_item ai ON ai.item_id=aw.item_ptr_id;

#NON_WEAPONS: How many of the items are not weapons? - Specify the armory table
SELECT COUNT(*) FROM armory_item WHERE item_id < 138;

#CHARACTER_ITEMS: How many Items does each character have? (Return first 20 rows) - fetch 20?
SELECT cci.character_id, count(cci.item_id) CHARACTER_ITEMS
FROM charactercreator_character_inventory cci
GROUP BY 1 ORDER BY 1 LIMIT 20;

#CHARACTER_WEAPONS: How many Weapons does each character have? (Return first 20 rows) - fetch 20?
SELECT cci.character_id, count(aw.item_ptr_id) CHARACTER_WEAPONS
FROM charactercreator_character_inventory cci LEFT JOIN armory_weapon aw
ON cci.item_id=aw.item_ptr_id GROUP BY 1 ORDER BY 1 LIMIT 20;

#AVG_CHARACTER_ITEMS: On average, how many Items does each Character have?
SELECT COUNT(item_id)*1.0/ COUNT(DISTINCT character_id) AVG_CHARACTER_ITEMS
FROM charactercreator_character_inventory;

#AVG_CHARACTER_WEAPONS: On average, how many Weapons does each character have?
SELECT COUNT(item_id)*1.0/ COUNT(DISTINCT character_id) AVG_CHARACTER_WEAPONS
FROM charactercreator_character_inventory WHERE item_id >= 138;

#===================================================================================================

## QUESTIONS ##

# Are these remotely close to what I'm supposed to be doing?