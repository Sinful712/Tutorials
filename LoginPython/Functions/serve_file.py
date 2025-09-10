# TECHNICAL: Standard imports
# DESCRIPTIVE: The python modules im using in this project
import socket  # TECHNICAL: Import the socket library to work with network connections
               # DESCRIPTIVE: This lets our program talk over the internet
import os      # TECHNICAL: Import the os library to check for files and file paths
               # DESCRIPTIVE: This lets us check if files exist and open them

from http_response import http_response

# Serve static files
def serve_file(filename):
    print(f"Serving {filename}")  # TECHNICAL: Print the file being served
                                  # DESCRIPTIVE: For debugging which page is sent
    if os.path.exists(filename):  # TECHNICAL: Check if file exists
                                  # DESCRIPTIVE: Make sure the file is there
        with open(filename, "rb") as f:  # TECHNICAL: Open file in binary mode
                                        # DESCRIPTIVE: Read raw bytes of the file
            content = f.read()
        # TECHNICAL: Determine Content-Type
        if filename.endswith(".html"):
            content_type = "text/html"
        elif filename.endswith(".css"):
            content_type = "text/css"
        elif filename.endswith(".js"):
            content_type = "application/javascript"
        else:
            content_type = "text/plain"
        return http_response(200, content_type, content)  # TECHNICAL: Send file with proper content type
                                                         # DESCRIPTIVE: Return the page to browser
    else:
        return http_response(404, "text/plain", b"File not found")  # TECHNICAL: File missing
                                                                    # DESCRIPTIVE: Tell browser it’s not found
