# Folder-Manager

A Python library to organise a folder. Creates relavent folders and moves the files accordingly into them.
If the script is left running in the background, it will watch for all incoming files and move them to their relavent folder. (Tip: Use it to manage your Downloads folder)

# Prerequisites

Python 3 or greater

# How to run 

1. Install the requirements from requiremts.txt file

2. Run FileManager.py using python and provide a folder path you want to organise as an argument. 
  (Eg. python3 FileManager.py  /path/to/folder/you/want/to/organise)
  
3. Modify the script according to your requirement.

# FileManager.py

Watchdog script that watches for any new files created or moved in the folder.

# CleanFolder.py

Finds the appropriate mapping of the given files extension to its destination folder name and moves it to that folder. 

# util.js

Contains folder mapping for all file extensions. 
  
# Take full advantage of the library

Use any job scheduler(eg. crontab) to run the FileManager.py on reboot. This will start the script at boot time and keep it running in the background. 