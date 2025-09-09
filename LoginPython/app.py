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


# Save user to file
def save_user(username, password):  # TECHNICAL: Function takes in a username and password
                                    # DESCRIPTIVE: Save a new user to the file
    with open(DB_FILE, "a") as f:  # TECHNICAL: Open the file in append mode so we don’t overwrite it
                                   # DESCRIPTIVE: Open file in "append" mode
        f.write(f"{username}:{password}\n")  # TECHNICAL: Write the new username and password with a newline
                                             # DESCRIPTIVE: Add new user to the file


# Handle GET requests
def handle_get(path):
    if path == "/":  # TECHNICAL: If the request is for the home page
                     # DESCRIPTIVE: Home page
        return serve_file("landing.html")
    elif path == "/login":  # TECHNICAL: If the request is for the login page
                            # DESCRIPTIVE: Login page
        return serve_file("login.html")
    elif path == "/signup":  # TECHNICAL: If the request is for the signup page
                             # DESCRIPTIVE: Signup page
        return serve_file("signup.html")
    elif path == "/welcome":  # TECHNICAL: If the request is for the welcome page
                              # DESCRIPTIVE: Welcome page after login
        return http_response(200, "text/html", b"<h1>You are logged in!</h1>")
    else:  # TECHNICAL: If the page doesn’t exist
           # DESCRIPTIVE: Page not found
        return http_response(404, "text/plain", b"Not found")


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


# Serve static files 
def serve_file(filename):
    if os.path.exists(filename):  # TECHNICAL: Check if the file exists
                                  # DESCRIPTIVE: Make sure the file is there
        with open(filename, "rb") as f:  # TECHNICAL: Open the file in binary read mode
                                         # DESCRIPTIVE: Open it as bytes
            content = f.read()  # TECHNICAL: Read the file’s contents
                                # DESCRIPTIVE: Grab everything inside
        return http_response(200, "text/html", content)  # TECHNICAL: Send the file content with success
                                                         # DESCRIPTIVE: Give the page back
    else:  # TECHNICAL: If the file doesn’t exist
           # DESCRIPTIVE: Page missing
        return http_response(404, "text/plain", b"File not found")


# Create HTTP Response
def http_response(status, content_type, body):
    reason = {200: "OK", 302: "Found", 404: "Not Found"}.get(status, "OK")  # TECHNICAL: Look up the text reason for status
                                                                           # DESCRIPTIVE: Match number to message
    headers = [  # TECHNICAL: Build the list of HTTP headers
                 # DESCRIPTIVE: Write the labels the browser expects
        f"HTTP/1.1 {status} {reason}",  # TECHNICAL: The status line
                                        # DESCRIPTIVE: Say if it worked or not
        f"Content-Type: {content_type}",  # TECHNICAL: The type of content (HTML, text, etc.)
                                          # DESCRIPTIVE: Tell the browser what kind of file
        f"Content-Length: {len(body)}",  # TECHNICAL: The length of the response body
                                         # DESCRIPTIVE: How big the message is
        "Connection: close",  # TECHNICAL: Close the connection after sending
                              # DESCRIPTIVE: Hang up the phone afterwards
        "",  # TECHNICAL: Blank line to separate headers from body
             # DESCRIPTIVE: Leave a space before the message
        ""
    ]
    return ("\r\n".join(headers)).encode() + body  # TECHNICAL: Join headers, encode to bytes, then add the body
                                                   # DESCRIPTIVE: Stick the labels and the content together


# Create Redirect
def redirect(location):
    headers = [  # TECHNICAL: Build the redirect headers
                 # DESCRIPTIVE: Write a note telling browser to go elsewhere
        "HTTP/1.1 302 Found",  # TECHNICAL: Status line for redirect
                               # DESCRIPTIVE: "Go somewhere else"
        f"Location: {location}",  # TECHNICAL: Tell the browser where to go
                                  # DESCRIPTIVE: Give the new address
        "Connection: close",  # TECHNICAL: Close the connection
                              # DESCRIPTIVE: Hang up after telling them
        "", "", 
    ]
    return ("\r\n".join(headers)).encode()  # TECHNICAL: Return the headers as bytes
                                            # DESCRIPTIVE: Send the instruction back


# Run Server
def run_server():
    host, port = "localhost", 8000  # TECHNICAL: Run on localhost at port 8000
                                    # DESCRIPTIVE: Run on your own computer, door 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # TECHNICAL: Make a TCP socket (IPv4 + TCP)
                                                                  # DESCRIPTIVE: Create a "phone" to take calls
        s.bind((host, port))  # TECHNICAL: Bind the socket to the host and port
                              # DESCRIPTIVE: Say "I’m sitting at door 8000"
        s.listen(5)  # TECHNICAL: Allow up to 5 people waiting in line
                     # DESCRIPTIVE: Let 5 guests queue outside
        print(f"Server running at http://{host}:{port}/")
        while True:  # TECHNICAL: Keep server always running
                     # DESCRIPTIVE: Don’t stop listening
            conn, addr = s.accept()  # TECHNICAL: Accept incoming connections
                                     # DESCRIPTIVE: Open the door to a guest
            with conn:  # TECHNICAL: Ensure the connection is cleaned up after
                        # DESCRIPTIVE: Close the door when they leave
                request = conn.recv(1024).decode()  # TECHNICAL: Receive and decode the request
                                                   # DESCRIPTIVE: Listen to what they ask
                if not request:  # TECHNICAL: If the request is empty, restart loop
                                 # DESCRIPTIVE: Ignore silent knocks
                    continue

                lines = request.split("\r\n")  # TECHNICAL: Split the request into lines
                                               # DESCRIPTIVE: Break the letter into sentences
                method, path, _ = lines[0].split(" ")  # TECHNICAL: Split into method, path, and protocol (ignored)
                                                      # DESCRIPTIVE: First sentence says "GET this address"

                # Extract body for POST Requests
                body = "" 
                if method == "POST":  # TECHNICAL: If it’s a POST request
                                      # DESCRIPTIVE: If they’re sending info
                    body = lines[-1]  # TECHNICAL: Get the last line of the request (the body)
                                      # DESCRIPTIVE: Last line is the form data

                # Handle the request
                if method == "GET":  # TECHNICAL: If the method is GET
                                     # DESCRIPTIVE: If they’re asking for a page
                    response = handle_get(path) 
                elif method == "POST":  # TECHNICAL: If the method is POST
                                         # DESCRIPTIVE: If they’re sending details
                    response = handle_post(path, body) 
                else:  # TECHNICAL: If method is neither GET nor POST
                       # DESCRIPTIVE: Don’t understand the request
                    response = http_response(405, "text/plain", b"Method not allowed")

                conn.sendall(response)  # TECHNICAL: Send the response back to the client
                                        # DESCRIPTIVE: Give the guest an answer


users = load_users()  # TECHNICAL: Load users from the file into memory
                      # DESCRIPTIVE: Read the saved login list

if __name__ == "__main__":  # TECHNICAL: Run only if this file is the main program
                            # DESCRIPTIVE: Start the server only if we run this file directly
    run_server()
