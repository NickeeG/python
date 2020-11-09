from watchdog.observer import observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json

class MyHandler(FileSystemEventHandler):
i=1
def on_modifier(self,event):
if ()
for filename in os.listner(folder_to_track):
    src = folder_to_track + "/" + filename
    new_destination = folder_destination + "/" + filename
    os.rename(sre, new_destination)

folder_to_track