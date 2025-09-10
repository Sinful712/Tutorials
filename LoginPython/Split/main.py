# TECHNICAL: Standard imports
# DESCRIPTIVE: The python modules im using in this project
import socket  # TECHNICAL: Import the socket library to work with network connections
               # DESCRIPTIVE: This lets our program talk over the internet
import os      # TECHNICAL: Import the os library to check for files and file paths
               # DESCRIPTIVE: This lets us check if files exist and open them

from handle_get import handle_get
from handle_post import handle_post
from load_users import load_users
from http_response import http_response

# Run server
def run_server():
    host, port = "localhost", 8000  # TECHNICAL: Host and port
                                    # DESCRIPTIVE: Computer address and “door”
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # TECHNICAL: TCP socket
                                                                  # DESCRIPTIVE: Open a phone line
        s.bind((host, port))  # TECHNICAL: Bind to address
                              # DESCRIPTIVE: Listen at this door
        s.listen(5)  # TECHNICAL: Queue limit
                     # DESCRIPTIVE: Let 5 guests wait outside
        print(f"Server running at http://{host}:{port}/")
        while True:  # TECHNICAL: Loop forever
                     # DESCRIPTIVE: Keep listening
            conn, addr = s.accept()  # TECHNICAL: Accept connection
                                     # DESCRIPTIVE: Open door for guest
            with conn:  # TECHNICAL: Ensure cleanup
                        # DESCRIPTIVE: Close door afterwards
                request = conn.recv(1024).decode()  # TECHNICAL: Get request
                                                   # DESCRIPTIVE: Listen to guest
                if not request:  # TECHNICAL: Ignore empty
                                 # DESCRIPTIVE: Skip silent knocks
                    continue

                lines = request.split("\r\n")  # TECHNICAL: Split into lines
                                               # DESCRIPTIVE: Break letter into sentences
                method, path, _ = lines[0].split(" ")  # TECHNICAL: Method, path, protocol
                                                      # DESCRIPTIVE: First sentence tells us what they want

                body = ""
                if method == "POST":  # TECHNICAL: Extract body
                                      # DESCRIPTIVE: Get sent form data
                    body = lines[-1]

                if method == "GET":  # TECHNICAL: Handle GET
                                     # DESCRIPTIVE: Sending page
                    response = handle_get(path)
                elif method == "POST":  # TECHNICAL: Handle POST
                                         # DESCRIPTIVE: Receiving form submission
                    response = handle_post(path, body)
                else:  # TECHNICAL: Unsupported method
                       # DESCRIPTIVE: Unknown request type
                    response = http_response(405, "text/plain", b"Method not allowed")

                conn.sendall(response)  # TECHNICAL: Send response
                                        # DESCRIPTIVE: Give answer to guest

users = load_users()  # TECHNICAL: Load users from file into memory
                      # DESCRIPTIVE: Read saved login list

if __name__ == "__main__":  # TECHNICAL: Run only if main program
                            # DESCRIPTIVE: Start server if run directly
    run_server()