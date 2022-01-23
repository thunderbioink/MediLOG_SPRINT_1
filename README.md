# Overview

Welcome to MediLOG! An interactive Medical Database, integrated with SQL and Python, intended for our Health Professionals.

Once running the program, the user is displayed with a *Menu*. In this *menu view*, the user can select up to five choices:

1. **View existing patient folders:**

    * Enter number *"1"* to pick.
    * Displays patient folder table.
2. **Add a new patient folder:**

    * Enter number *"2"* to pick.
    * Prompts user to enter the following information:
        * Name
        * Date of birth
        * Illness/Disability
        * Folder creation time and date

3. **Edit an existing patient folder:**

    * Enter number *"3"* to pick.
    * Prompts user to pick a patient to edit. Enter number that correponds to patient. Type the name exactly as shown.
    * Prompts user to update the following fields:
        * Date of birth
        * Illness/Disability
            * *User must type name correctly to update the correct patient, otherwise "Invalid name!" is displayed and birth date and illness won't update after entering information.*

            * *User is not allowed to edit folder creation date since it's unique to each patient, in case they have the same First/Last name. To change folder creation date, user needs to delete patient folder and create new one.*

4. **Delete an existing patient folder:**
    * Enter number *"4"* to delete patient folder.
    * Prompts user to pick patient folder to delete. Enter number that corresponds to patient.
5.  **Quit the program:**
    * Enter number *"5"* to quit the program.
    * Exits program.

The purpose of this program is to aid Health proffesionals in the administration of their patient records. This program is the first step into integrating a future patient database, where the patient will be able to log medication, dosage, and intake date and time. These future improvements will automatically update into their existing patient folder.

The idea was originally inspired by individuals that need to constantly update their medically complex family member's medication,dosage, and intake date and time from home. They do this by calling their assigned health professional in plain 2022. One of them was able to express to me how during the pandemic, being able to keep their health provider's updated with their family member's medication intake patterns would be much easier if they had an app to send that information to their existing patient records.

MediLOG's current functionality is the first step into aiding, both, individuals with medically complex family members and professional health providers, enhance their patient record updating experience.

[Software Demo Video](https://www.loom.com/share/3670730299024978bb83f991ed789988)

# Relational Database

This relational database holds four sets of data:

1. Patient Name
2. Patient Birth Date
3. Illness/Disability
4. Patient Folder Creation Date & Time

* **Database Column Names:**
![Database Column Names](/program_images/COLUMNS.png)
* **Clean & Organized Database:**
![Database Cleaned](/program_images/TABLE_COMPLETE.png)
* **How to update a patient's folder:**
![Database Input Format](/program_images/3_UPDATE_FOLDER.png)

* **Database Organization:**
    * Information is displayed by name, in an ascending order.
![Database Column Names](/program_images/ASC_ORDER_BY_NAME.png)


* **There is a format that the user needs to follow when prompted to input patient information:**
![Database Input Format](/program_images/2_CREATE_FOLDER.png)

* **How to update a patient's folder:**
![Database Input Format](/program_images/3_UPDATE_FOLDER.png)
    * Input **Name ID:**
    * Type in patient name to match records
    * Type in *correct* birth date
    * Type in *correct* illness/disability
        * *The naming schemes match the naming scheme when selecting option **2**.*

# Development Environment

Tools used to develop this program were Visual Studio Code, SQL Language, Python language, and GitHub.

The programming languages I used were SQL and Python. To integrate both of these languages, I had to import the sqlite3 library:

![Database Input Format](/program_images/SQL.png)
* *It is essential this library is imported at the beginning of your python file, otherwise,you'll get an error:*

![Database Input Format](/program_images/error.png)

# Useful Websites

* [SQL Tutorial](https://www.w3schools.com/sql/default.asp)
* [SQLite](https://www.sqlite.org/index.html)
* [SQL Tutorial Dofactory](https://www.dofactory.com/sql)
* [SQL Geeksforgeeks](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/?ref=leftbar-rightbar)
* [SQL Techonthenet](https://www.techonthenet.com/sql/index.php)
* [Fake Names Documentation](https://cybertext.wordpress.com/2007/04/30/fake-names-for-documentation/)


# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* **1st priority:** Create the patient database so individuals with medically complex family members can upload medication, dosage, & date and time to their existing patient folder.

In this priority I intend to make the program more user-friendly to access and edit both databases.

* **2nd priority:** Have, both, MediLOG Health Professional and MediLOG Patient database speak to eachother so the users can have an automatic record update.

In this priority I'll have to connect both databases to a cloud database.
* **3rd priority:** Create a user-friendly platform that can be accessed as a smartphone App & as a Web App.

This priority will take longer, as I'll have to improve simple things in the program skeleton prior to publishing a fully working Web/Mobile App.