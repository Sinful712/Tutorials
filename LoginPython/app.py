import socket
import os

DB_FILE = "logins.txt"

# Load users from file
def load_users():
    users = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            for line in f:
                if ":" in line:
                    username, password = line.strip().split(":", 1)
                    users[username] = password
    return users

# Save users to file
def save_user(username, password):
    with open(DB_FILE, "a") as f:
        f.write(f"{username}:{password}\n")

users = load_users()

def handle_get(path):
    if path == "/":
        return serve_file("landing.html")
    elif path == "/login":
        return serve_file("login.html")
    elif path == "/signup":
        return serve_file("signup.html")
    elif path == "/welcome":
        return http_response(200, "text/html", b"<h1>You are logged in!</h1>")
    else:
        return http_response(404, "text/plain", b"Not found")

def handle_post(path, body):
    params = {}
    for pair in body.split("&"):
        if "=" in pair:
            k, v = pair.split("=", 1)
            params[k] = v

    if path == "/login":
        username = params.get("username", "")
        password = params.get("password", "")
        if users.get(username) == password:
            return redirect("/welcome")
        else:
            return http_response(200, "text/html", b"Invalid login. <a href='/login'>Try again</a>")

    elif path == "/signup":
        username = params.get("username", "")
        password = params.get("password", "")
        if username in users:
            return http_response(200, "text/html", b"Username already exists. <a href='/signup'>Try again</a>")
        else:
            users[username] = password
            save_user(username, password)
            return redirect("/welcome")

    else:
        return http_response(404, "text/plain", b"Not found")

def serve_file(filename):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            content = f.read()
        return http_response(200, "text/html", content)
    else:
        return http_response(404, "text/plain", b"File not found")

def http_response(status, content_type, body):
    reason = {200: "OK", 302: "Found", 404: "Not Found"}.get(status, "OK")
    headers = [
        f"HTTP/1.1 {status} {reason}",
        f"Content-Type: {content_type}",
        f"Content-Length: {len(body)}",
        "Connection: close",
        "",
        ""
    ]
    return ("\r\n".join(headers)).encode() + body

def redirect(location):
    headers = [
        "HTTP/1.1 302 Found",
        f"Location: {location}",
        "Connection: close",
        "",
        ""
    ]
    return ("\r\n".join(headers)).encode()

def run_server():
    host, port = "localhost", 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        print(f"Server running at http://{host}:{port}/")
        while True:
            conn, addr = s.accept()
            with conn:
                request = conn.recv(1024).decode()
                if not request:
                    continue
                lines = request.split("\r\n")
                method, path, _ = lines[0].split(" ")

                # Extract body for POST
                body = ""
                if method == "POST":
                    body = lines[-1]

                if method == "GET":
                    response = handle_get(path)
                elif method == "POST":
                    response = handle_post(path, body)
                else:
                    response = http_response(405, "text/plain", b"Method not allowed")

                conn.sendall(response)

if __name__ == "__main__":
    run_server()
