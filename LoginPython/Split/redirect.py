# TECHNICAL: Standard imports
# DESCRIPTIVE: The python modules im using in this project
import socket  # TECHNICAL: Import the socket library to work with network connections
               # DESCRIPTIVE: This lets our program talk over the internet
import os      # TECHNICAL: Import the os library to check for files and file paths
               # DESCRIPTIVE: This lets us check if files exist and open them


# Create redirect
def redirect(location):
    headers = [
        "HTTP/1.1 302 Found",  # TECHNICAL: Redirect status
                               # DESCRIPTIVE: Say “go elsewhere”
        f"Location: {location}",  # TECHNICAL: Target URL
                                   # DESCRIPTIVE: Where to send the browser
        "Connection: close",
        "", ""
    ]
    return ("\r\n".join(headers)).encode()  # TECHNICAL: Return bytes
                                            # DESCRIPTIVE: Send redirect instruction
