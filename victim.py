#!/bin/bash/env python3 
import os 
import sys
import socket 
s = socket.socket()
port = 4444
host = input(str("Enter The server Address>>"))
s.connect((host,port))
print("connected")
