import sqlite3

# Connect to the database
connection = sqlite3.connect('records.db')
cursor = connection.cursor()

# Create table (if it does not already exist)
cursor.execute("CREATE TABLE IF NOT EXISTS patients (name TEXT, birth TEXT, creation REAL)")


# START PROGRAM - MENU

start_menu = input("""
  
  MENU
  
1. LOGIN TO MEDILOG
2. SIGN UP TO MEDILOG
3. DELETE MY MEDILOG
4. SHARE MY MEDILOG
5. QUIT 

""")

# LOOP TO KEEP PROGRAM RUNNING UNTIL FALSE:
"""
PART 1 OF THE PROGRAM: THE USER CAN CREATE THEIR
MEDILOG FOLDER.

"""

while start_menu != False: 
  
  # START MENU - OPTION 1:  LOGIN TO MEDILOG 
  if start_menu == 1:
    # PROMPT USER TO ENTER LOGIN INFO:
    existing_folder_menu = input(
      """
      LOGIN TO YOUR FOLDER:

      1. Name:
      2. Birth Date (required):
      3. Password (required):
      
      """
    )
    existing_name = input(str(""))
    existing_birth_date = input(int(""))
    existing_password = input(str(""))
    
  # START MENU - OPTION 2:  SIGN UP TO MEDILOG 
  elif start_menu == 2:
    # PROMPT USER TO ENTER LOGIN INFO:
    new_folder_menu = input(
        """
        SIGN UP AND CREATE YOUR MEDILOG FOLDER:

        1. First Name (required):
        2.Last Name (required):
        3. Birth Date (required):
        4. Password (required):
        
        """
    )
    new_name = input(str(""))
    new_last_name = input(str(""))
    new_birth_date = input(int(""))
    new_password = input(str(""))
  
  # START MENU - OPTION 3:  DELETE MEDILOG ACCOUNT & INFORMATION 
  elif start_menu == 3:
      prompt_Y_N = input(str("DELETING YOUR MEDILOG CAN'T BE UNDONE.\n\n\nDO YOU WISH TO CONTINUE? Y/N...\n\n\n"))
      if prompt_Y_N == str("Y", "Yes", "YES"):
        delete_existing_folder = input(
              """
              PLEASE ENTER YOUR LOGIN INFORMATION TO DELETE\nYOUR MEDILOG ACCOUNT & DATA:
              
              1. Name:
              2. Birth Date (required):
              3. Password (required):
              
              """
          )
      # CREATE REMOVE FOR THE FOLLOWING ITEMS & PERMANENTLY REMOVE THAT DATA:
        existing_name = input(str(""))
        existing_birth_date = input(int(""))
        existing_password = input(str(""))
    # If user chooses No, return to START MENU
      else:
          if prompt_Y_N == str("N", "No", "NO"):
                # Return to START MENU
                pass  
  # START MENU OPTION 4: SHARE MY MEDILOG - only work on this if possible to get previous three working: 
  elif start_menu == 4:
    # PROMPT USER TO SHARE THE INFORMATION TO NURSES/DOCTORS...
    break
  else:
        if start_menu == 5:
              break
  
  """
  PART 2 OF THE PROGRAM: A MEDILOG FOLDER WILL CONTAIN A DAILY FOLDER WITH MEDICATION NAME, TIME MEDICATION WAS TAKEN,
  AND DOSAGE.
  """
  # Implement if possible...continue here if first part works. 