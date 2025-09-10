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

# Save user to file
def save_user(username, password):  # TECHNICAL: Function takes in a username and password
                                    # DESCRIPTIVE: Save a new user to the file
    with open(DB_FILE, "a") as f:  # TECHNICAL: Open the file in append mode so we don’t overwrite it
                                   # DESCRIPTIVE: Open file in "append" mode
        f.write(f"{username}:{password}\n")  # TECHNICAL: Write the new username and password with a newline
                                             # DESCRIPTIVE: Add new user to the file

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


# Handle GET requests
def handle_get(path):
    # TECHNICAL: Default to landing page if root
    # DESCRIPTIVE: If someone visits "/", show the home page
    if path == "/":
        path = "src/landing.html"
    elif path == "/login":
        path = "src/login.html"
    elif path == "/signup":
        path = "src/signup.html"
    elif path == "/welcome":  # TECHNICAL: Special route for welcome message        # DESCRIPTIVE: Page shown after login
        return welcome()

    filename = path.lstrip("/")  # TECHNICAL: Remove leading slash
                                 # DESCRIPTIVE: Make it a file path we can read
    return serve_file(filename)  # TECHNICAL: Serve the file (HTML, CSS, etc.)
                                 # DESCRIPTIVE: Send the requested page to the browser

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

# Create HTTP response
def http_response(status, content_type, body):
    reason = {200: "OK", 302: "Found", 404: "Not Found"}.get(status, "OK")  # TECHNICAL: Status reason
                                                                           # DESCRIPTIVE: Convert number to message
    headers = [
        f"HTTP/1.1 {status} {reason}",  # TECHNICAL: Status line
                                        # DESCRIPTIVE: Tell browser if it worked
        f"Content-Type: {content_type}",  # TECHNICAL: Type of content
                                          # DESCRIPTIVE: Let browser know the file type
        f"Content-Length: {len(body)}",  # TECHNICAL: Size of body
                                         # DESCRIPTIVE: How much data to read
        "Connection: close",  # TECHNICAL: Close after sending
                              # DESCRIPTIVE: Hang up when done
        "", ""
    ]
    return ("\r\n".join(headers)).encode() + body  # TECHNICAL: Combine headers + body
                                                   # DESCRIPTIVE: Send everything together

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
