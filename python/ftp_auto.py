#Python version: 3.x
import pdb #for debug
import os
from time import sleep
from subprocess import Popen, PIPE

def cmd(cmd1, cmd2, cmd3, cmd4 = None):
        command = '%s %s %s' % (cmd1, cmd2, cmd3)
        #print(command)
        os.system(command)

# service begin
while (1) :
        tmp = Popen("date +%w", shell=True, stdout=PIPE).stdout.read()
        week_int = int(tmp)
        #print(week_int)

        if week_int != 0 or week_int != 6:
                tmp = Popen("date +%H", shell=True, stdout=PIPE).stdout.read()
                hour_int = int(tmp)
                #print(hour_int)
                
                if hour_int <= 11 or hour_int >= 20:
                        print("proftpd start")
                        cmd("service", "proftpd", "start")
                else: 
                        print("proftpd stop")	
                        cmd("service", "proftpd", "stop")
                sleep(60 * 10) # sleep 10 mins
        else:
                sleep(60 * 60 * 24) # sleep 1 day
