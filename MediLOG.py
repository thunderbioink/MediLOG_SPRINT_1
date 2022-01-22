"""
CSE310 SQL MediLOG Program

This database will store patient names, birthdays, disability/illness, and a folder date/time creation.
The purpose is to create a medical database using SQL and Python.
The public intended are people that need to log their medical information from home & send it to a
a health professional. 
"""

import sqlite3

# Connect to the database
connection = sqlite3.connect('patientrecords.db')
cursor = connection.cursor()

# Create table (if it does not already exist)
cursor.execute("CREATE TABLE IF NOT EXISTS patients (name TEXT, birthday DATE, illness TEXT, creation REAL)")

def get_name(cursor):
    cursor.execute("SELECT name FROM patients")
    results = cursor.fetchall()
    if len(results) == 0:
        print("No names in database")
        return None
    for i in range(len(results)):
        print(f"{i+1} - {results[i][0]}")
    choice = 0
    while choice < 1 or choice > len(results):
        choice = int(input("Name ID: "))
    return results[choice-1][0]


choice = None
while choice != "5":
    print("1) View Patient Folders")
    print("2) Add Patient Folder")
    print("3) Update Patient Folder")
    print("4) Delete Patient Folder")
    print("5) Quit")
    choice = input("> ")
    print()
    if choice == "1":
        # Display patients
        cursor.execute("SELECT * FROM patients ORDER BY creation ASC ")
        print("{:>20}  {:>10}  {:>40}  {:>40}".format("Name/Middle/Last", "Birthday", "Disability/Illness", "Folder Date Creation"))

        for record in cursor.fetchall():
          print("{:>20}  {:>10}  {:>40}  {:>40}".format(record[0], record[1], record[2], record[3]))
        
    elif choice == "2":
        # Add New Patient
        try:
            name = input("Name (i.e. First Middle Last ): ")
            birthday = input("Birth Date (i.e. YYYY-MM-DD ): ")
            dis_ill = input("Disability/Illness (i.e. No Abbreviations): ")
            creation = input("Folder Creation Date (i.e YYYY-MM-DD HH:MI ): ")
            values = (name, birthday, dis_ill, creation)
            cursor.execute("INSERT INTO patients VALUES(?,?,?,?)", values)
            connection.commit()
        except ValueError:
            print("Invalid data!")
    elif choice == "3":
        # Update existent patient folder
        try:
            name = get_name(cursor)
        
            if name == None:
                continue
            
            name = input("Name: ")
            birthday = input("Birth Date (i.e. YYYY-MM-DD ): ")
            dis_ill = input("Disability/Illness (i.e. No Abbreviations): ")
            values = (dis_ill, birthday, name, ) # Make sure order is correct
            cursor.execute("UPDATE patients SET illness = ?, birthday = ? WHERE name = ?", values)
            connection.commit()
            # Display updated patient folder
            # cursor.execute("SELECT * FROM patients ORDER BY creation DESC ")
            # print("{:>20}  {:>10}  {:>40}  {:>40}".format("Name/Middle/Last", "Birthday", "Disability/Illness", "Folder Date Creation"))

            # for record in cursor.fetchall():
            #     print("{:>20}  {:>10}  {:>40}  {:>40}".format(record[0], record[1], record[2], record[3]))
            
            if cursor.rowcount == 0:
                print("Invalid Name!")
        except ValueError:
            print("Invalid data!")
    elif choice == "4":
        # Delete Patient
        name = get_name(cursor)
        
        if name == None:
            continue
        values = (name, )
        cursor.execute("DELETE FROM patients WHERE name = ?", values)
        connection.commit()
    print()
    # Continue improving project.

# Close the database connection before exiting
connection.close()