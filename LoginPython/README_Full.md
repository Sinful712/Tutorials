# Python Login App

## File Structure:
Before anything you need to make your file structure. 

```
root
├── logins.txt
├── main.py
└── src
    ├── landing.html
    ├── login.html
    ├── signup.html
    └── style.css
```

## Imports/modules:
Then you need to make sure you are useing the correct imports for your project.

```python
import socket
import os
```

## create your variables:
In this project we use the 'os' module to open, read and write a file,  
so what we are going to do is create a variable 'DB_FILE' and make it "logins.txt" so we can use that variable instead of writing "logins.txt" everytime we want to use it.  
This file will have all of our users usernames and passwords in it.

```python
DB_FILE = "logins.txt"
```

## Functions:

Next I will take you through each function and explain them line by line so you can understand.

### load_users()

First off we make the function definition. This tells python that anything indented underneath it should be run when it is called(told to run)
```python
def load_users():
```

Next we make a dictionary variable called users. This is an empty dictionary we are going to use to store our usernames and passwords.
```python
users = {} # each username and password will look like: 'username': 'password'

# a populated users variable will look as follows, 
# once we've gotten the data from the file:
users = {
    'user'  : 'pass'
    'Jimmy' : 'Password2345', 
    'Happy' : 'NewPass1'
}
```

To get the users out of a file we first have to open the file.
```python
if os.path.exists(DB_FILE): # this checks to see if the file is there.
                            # if not -> skip.

    with open(DB_FILE, "r") as f: # this opens the file and just reads it
                                  # then stores what it reads in 'f'

         for line in f: # a loop function that takes each item in the list
                        # 'f' and runs some code on it

                if ":" in line: # if the line we just got from 'f' has a colon
                                # do the next code.

                    username, password = line.strip().split(":", 1) # creates 2
                    # variables from the line item by spliting it in two
                    # then deletes all the spaces around it.

                    users[username] = password # creates a line in the users
                    # dictionary putting username as the 'key'
                    # and password as the 'value'
```

At the end your function should look like this.

```python
def load_users():
    users = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            for line in f:
                if ":" in line:
                    username, password = line.strip().split(":", 1)
                    users[username] = password
    return users
```

