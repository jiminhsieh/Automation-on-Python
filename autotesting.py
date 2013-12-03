# Python version 2.7: 
# automation for ftp put/get in Windows 

import thread
import os

def loop_cmd(service, action):
        command = '%s -s:ftp_%s.txt\n' % (service, action)
        while 1:
                print(command)
                #os.system(command)

try: 
        thread.start_new_thread(loop_cmd, ("ftp", "get"))
        thread.start_new_thread(loop_cmd, ("ftp", "put"))
except: 
        print("Error!")
while 1:
        pass
