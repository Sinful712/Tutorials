# TECHNICAL: Standard imports
# DESCRIPTIVE: The python modules im using in this project
import socket  # TECHNICAL: Import the socket library to work with network connections
               # DESCRIPTIVE: This lets our program talk over the internet
import os      # TECHNICAL: Import the os library to check for files and file paths
               # DESCRIPTIVE: This lets us check if files exist and open them

# TECHNICAL: Path to the file where usernames and passwords will be stored
# DESCRIPTIVE: File to store usernames and passwords
DB_FILE = "logins.txt" 

# Save user to file
def save_user(username, password):  # TECHNICAL: Function takes in a username and password
                                    # DESCRIPTIVE: Save a new user to the file
    with open(DB_FILE, "a") as f:  # TECHNICAL: Open the file in append mode so we don’t overwrite it
                                   # DESCRIPTIVE: Open file in "append" mode
        f.write(f"{username}:{password}\n")  # TECHNICAL: Write the new username and password with a newline
                                             # DESCRIPTIVE: Add new user to the file
