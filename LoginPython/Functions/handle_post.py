# TECHNICAL: Standard imports
# DESCRIPTIVE: The python modules im using in this project
import socket  # TECHNICAL: Import the socket library to work with network connections
               # DESCRIPTIVE: This lets our program talk over the internet
import os      # TECHNICAL: Import the os library to check for files and file paths
               # DESCRIPTIVE: This lets us check if files exist and open them

from redirect import redirect
from http_response import http_response
from save_user import save_user
from load_users import load_users

users = load_users()

# Handle POST requests
def handle_post(path, body):
    params = {}  # TECHNICAL: Dictionary to hold form data
                 # DESCRIPTIVE: Where we’ll store form data
    for pair in body.split("&"):  # TECHNICAL: Split the body into key=value pairs
                                  # DESCRIPTIVE: Break "username=bob&password=1234"
        if "=" in pair:  # TECHNICAL: Only process valid pairs
                         # DESCRIPTIVE: Only split if it makes sense
            k, v = pair.split("=", 1)  # TECHNICAL: Split into key and value
                                       # DESCRIPTIVE: Separate the label and value
            params[k] = v  # TECHNICAL: Store them in the dictionary
                           # DESCRIPTIVE: Keep it in memory

    if path == "/login":  # TECHNICAL: If the request is a login
                          # DESCRIPTIVE: Someone is trying to log in
        username = params.get("username", "")  # TECHNICAL: Get the username from the form
                                               # DESCRIPTIVE: Look at the username field
        password = params.get("password", "")  # TECHNICAL: Get the password from the form
                                               # DESCRIPTIVE: Look at the password field
        if users.get(username) == password:  # TECHNICAL: Check if the username and password match
                                             # DESCRIPTIVE: Does it match our records?
            return redirect("/welcome")
        else:  # TECHNICAL: If the login fails
               # DESCRIPTIVE: Wrong details
            return http_response(200, "text/html", b"Invalid login. <a href='/login'>Try again</a>")

    elif path == "/signup":  # TECHNICAL: If the request is a signup
                             # DESCRIPTIVE: Someone is creating a new account
        username = params.get("username", "")
        password = params.get("password", "")
        if username in users:  # TECHNICAL: Check if the username already exists
                               # DESCRIPTIVE: Username already taken
            return http_response(200, "text/html", b"Username already exists. <a href='/signup'>Try again</a>")
        else:  # TECHNICAL: If the username is new
               # DESCRIPTIVE: New account
            users[username] = password  # TECHNICAL: Save to memory
                                        # DESCRIPTIVE: Keep it in memory
            save_user(username, password)  # TECHNICAL: Save them to the file
                                           # DESCRIPTIVE: Write it down
            return redirect("/welcome")

    else:  # TECHNICAL: If the path isn’t valid
           # DESCRIPTIVE: Page doesn’t exist
        return http_response(404, "text/plain", b"Not found")
