# TECHNICAL: Standard imports
# DESCRIPTIVE: The python modules im using in this project
import socket  # TECHNICAL: Import the socket library to work with network connections
               # DESCRIPTIVE: This lets our program talk over the internet
import os      # TECHNICAL: Import the os library to check for files and file paths
               # DESCRIPTIVE: This lets us check if files exist and open them

# TECHNICAL: Path to the file where usernames and passwords will be stored
# DESCRIPTIVE: File to store usernames and passwords
DB_FILE = "logins.txt" 

# Load users from file
def load_users(): 
    users = {}  # TECHNICAL: Create an empty dictionary to hold users and passwords
                # DESCRIPTIVE: Start with an empty list of users
    if os.path.exists(DB_FILE):  # TECHNICAL: Check if the logins file exists
                                 # DESCRIPTIVE: Check if the file already exists
        with open(DB_FILE, "r") as f:  # TECHNICAL: Open the file in read mode
                                       # DESCRIPTIVE: Open it so we can read
            for line in f:  # TECHNICAL: Loop through each line in the file
                            # DESCRIPTIVE: Read each line like "bob:1234"
                if ":" in line:  # TECHNICAL: Only process lines with username:password
                                 # DESCRIPTIVE: Only split if the line looks valid
                    username, password = line.strip().split(":", 1)  # TECHNICAL: Split line into username and password
                                                                    # DESCRIPTIVE: Separate the name and password
                    users[username] = password  # TECHNICAL: Store them in the dictionary
                                                # DESCRIPTIVE: Save them in memory
    return users  # TECHNICAL: Return the dictionary of users
                  # DESCRIPTIVE: Hand back the list of users