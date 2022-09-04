from genericpath import isfile
import os

# ANSI coloring for errors and directory changes.
pref = "\033["
reset = f"{pref}0m"

class colors:
    black = "30m"
    red = "31m"
    green = "32m"
    yellow = "33m"
    blue = "34m"
    magenta = "35m"
    cyan = "36m"
    white = "37m"

# List of directories that contain temporary files that should be deleted
dir = ['/mnt/c/Windows/Temp', '/mnt/c/Users/your user name/AppData/Local/Temp']

# Loop through files in directory and delete them 
for d in dir:
    print(f'{pref}{colors.green}You are deleting files in {d}{reset}')
    for (root, dir, files) in os.walk(d):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
                print(f'succesfully removed the temp file{file}')
            except Exception as e:
                    print(f'{pref}{colors.red}{e}{reset}')
