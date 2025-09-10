# TECHNICAL: Standard imports
# DESCRIPTIVE: The python modules im using in this project
import socket  # TECHNICAL: Import the socket library to work with network connections
               # DESCRIPTIVE: This lets our program talk over the internet
import os      # TECHNICAL: Import the os library to check for files and file paths
               # DESCRIPTIVE: This lets us check if files exist and open them


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
