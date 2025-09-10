# TECHNICAL: Standard imports
# DESCRIPTIVE: The python modules im using in this project
import socket  # TECHNICAL: Import the socket library to work with network connections
               # DESCRIPTIVE: This lets our program talk over the internet
import os      # TECHNICAL: Import the os library to check for files and file paths
               # DESCRIPTIVE: This lets us check if files exist and open them

from http_response import http_response

DB_FILE = "logins.txt" 

# Displays all the currently registered usernames to the user
def welcome():
    usernames = []  # TECHNICAL: Initialize an empty list to store usernames
                     # DESCRIPTIVE: Start a list to collect all usernames from the file
    with open(DB_FILE, "r") as f:  # TECHNICAL: Open the database file in read mode
                                   # DESCRIPTIVE: Look at our saved users
        for line in f:  # TECHNICAL: Loop through each line in the file
                        # DESCRIPTIVE: Read each line like "bob:1234"
            if ":" in line:  # TECHNICAL: Only process lines with username:password
                               # DESCRIPTIVE: Skip invalid lines
                username, _ = line.strip().split(":", 1)  # TECHNICAL: Split into username and password
                                                            # DESCRIPTIVE: Separate the name from the password
                usernames.append(username)  # TECHNICAL: Add username to the list
                                            # DESCRIPTIVE: Save it in memory

    # Create the HTML content for the response
    content = f"""<h1>Welcome</h1>
    <p>You are logged in!</p>
    <p>All users:</p>
    <ul>
        {''.join(f'<li>{u}</li>' for u in usernames)}  <!-- TECHNICAL: Generate <li> items for each username
                                                         DESCRIPTIVE: Make a bullet point for each user -->
    </ul>
    <p><a href="/">Logout</a></p>""".encode()  # TECHNICAL: Encode the string to bytes
                                                    # DESCRIPTIVE: Prepare it to send to the browser

    return http_response(200, "text/html", content)  # TECHNICAL: Return an HTTP response with status 200
                                                    # DESCRIPTIVE: Show the welcome page with the list of users
