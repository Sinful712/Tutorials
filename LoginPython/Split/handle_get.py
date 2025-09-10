# TECHNICAL: Standard imports
# DESCRIPTIVE: The python modules im using in this project
import socket  # TECHNICAL: Import the socket library to work with network connections
               # DESCRIPTIVE: This lets our program talk over the internet
import os      # TECHNICAL: Import the os library to check for files and file paths
               # DESCRIPTIVE: This lets us check if files exist and open them

from serve_file import serve_file
from welcome import welcome

# Handle GET requests
def handle_get(path):
    # TECHNICAL: Default to landing page if root
    # DESCRIPTIVE: If someone visits "/", show the home page
    if path == "/":
        path = "/landing.html"
    elif path == "/login":
        path = "/login.html"
    elif path == "/signup":
        path = "/signup.html"
    elif path == "/welcome":  # TECHNICAL: Special route for welcome message        # DESCRIPTIVE: Page shown after login
        return welcome()

    filename = path.lstrip("/")  # TECHNICAL: Remove leading slash
                                 # DESCRIPTIVE: Make it a file path we can read
    return serve_file(filename)  # TECHNICAL: Serve the file (HTML, CSS, etc.)
                                 # DESCRIPTIVE: Send the requested page to the browser
