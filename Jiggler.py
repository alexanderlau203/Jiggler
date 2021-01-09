import sys
import re
from datetime import datetime

def get_timeout():
    print("""
        Welcome to Jiggler! Please specify the datetime you 
        wish the script to expire. Else, leave the argument blank 
        if you want it to run indefinitely.
    """)

    while True:
        timeout = input("Specify timeout (dd:mm:yyyy:hh:MM:ss): ")

        if timeout is None:
            return None
        elif re.compile(r'\d{2}:\d{2}:\d{4}:\d{2}:\d{2}:\d{2}').match(timeout) is not None:
            t = timeout.split(':')
            return datetime(int(t[2]), int(t[1]), int(t[0]), int(t[3]), int(t[4]), int(t[5]))
        else:
            print('Invalid format.')

if __name__ == '__main__':
    timeout = get_timeout()
    