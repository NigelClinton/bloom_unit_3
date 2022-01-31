# Import Libary
import sqlite3

# create connection
conn = sqlite3.connect('health_records.sqlite3')

# create object cursor
curs = conn.cursor()

# Create Table
create_table = """
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER,
    patient_name TEXT,
    patient_age INTEGER
);
"""

# Execute Table Creation
curs.execute(create_table)

if not curs.execute("""SELECT * FROM patients;""").fetchall():
    # Patients inserted into table
    patient_insert = """
    insert into patients values
        (0, 'Rochelle Joy',62),
        (0, 'Daniel Krieg',22),
        (0, 'Jamie Klein',41),
        (0, 'Sam Tillman',20),
        (0, 'Amanda Bynes',30);
    """

    # Execute Patient Insert
    curs.execute(patient_insert)

#Commit Changes
conn.commit()

# Number of patients
num_patients = """
SELECT COUNT(*)
FROM patients;
"""

# Number of patients over 30
num_patients_over_30 = """
SELECT COUNT(*)
FROM patients
WHERE patient_age >= 30;
"""

# avg patient age
avg_patient_age = """
SELECT AVG(patient_age)
FROM patients;
"""


if __name__ == '__main__':
    quries = [num_patients,num_patients_over_30,avg_patient_age]

for qurey in quries:
    results = curs.execute(qurey).fetchall()
    print(results)

conn.close()