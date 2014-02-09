#!/usr/bin/env python3
import os
from subprocess import Popen, PIPE

def update():
    os.system('sudo apt-get update')

def install(feature = []):
    app_list = ' '.join(feature)
    command = 'sudo apt-get -y install %s' % (app_list)
    #os.system(command)
    print(command)

class Cmd:
    def __init__ (self, string):
        self.string = string
    #os.system(string)
    def send(self):
        #os.system(self.string)
        print(self.string)

class RootCmd(Cmd):
    def send(self):
        #os.system('sudo %s' % (self.string)
        print('sudo %s' % (self.string))

class ServiceCmd(Cmd):
    def __init__(self, app, action):
        self.app = app
        self.action = action
    def send(self):
        #os.system('sudo service %s %s' % (self.app, self.action)
        print('sudo service %s %s' % (self.app, self.action))

class Command:
    def SendCmd(self, behavior):
        behavior.send()
