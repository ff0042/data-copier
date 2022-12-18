# Main function
# ---------------
# any code not part of a function will execute even when another program that imports the file containing the "global" code.
# special variable: __name__
# When we run any Python program, the value of __name__ is set to __main__.
# Use __name__ and __main__ to prevent inadvertent execution when code is imported by another program

# Access Host / OS Environment Values
# -----------------------------------
# On Mac or Linux
# export DB_NAME=retail_db

# On Windows (must be double quotes)
# $env:DB_NAME = "retail_db" 

# We can get the value of DB_NAME by passing it to os.environ.get
#   import os
#   db_name = os.environ.get('COMPUTERNAME')

# configs = dict(os.environ.items()) # dict of all host environment variables
### show all env vars
#   for item in configs.items():
#       print(f'{item[0]}: {item[1]}')
#   configs['COMPUTERNAME'] # show COMPUTERNAME only. If key does not exist, returns key error. configs is a dict
#   os.environ.get('COMPUTERNAME') # Same thing as above. If key does not exist, returns None

# Passing Env Variables to python program
# ---------------------------------------
# To see env variable in debug, define value under project's debug property setting.
import os

def myFunc():
    COMPUTERNAME = os.environ.get('COMPUTERNAME')
    print(f'Hello World from {COMPUTERNAME}')

if __name__ == '__main__':
    myFunc();