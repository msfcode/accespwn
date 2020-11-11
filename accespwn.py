#!/bin/bash/env python3
import os
import sys
import socket
print("                                             Coded By @msfcode                     ")
print("                                             exploits, Coffee                                  ")
print("                                                KEEP-CALM")
print("                                             They Watch YOU !!                      ")
print("")
print("")
print("")
print("")
print("                                                \u001b[31mAttacks ")
print("")
print("                                \u001b[37m1-Port Scanning          2-Backdoor ")
print("")
number = int(input("Type the attack number>>"))
if number == 1:
  print("")
  print("")
  print("                 \u001b[31mPort Scanners are an important tool when you want to investigate any remote or")
  print("                local network for security considerations. Used by programmers and network administrators,")    
  print("                these port scanners are used to mainly know what ports are being used by what applications,") 
  print("                     so you can identify malicious programs right away.")
  print("")
  print("")
  socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  host = input("\u001b[32mType The Ip>>")
  port = int(input("Type Port Number>>"))
  if socket.connect_ex((host, port)):
   print("\u001b[31mThe Port is closed")
  else: 
   print("\u001b[33mThe Port is opened")
if number == 2:
   print("")
   print("              \u001b[36mA backdoor is a malware type that negates normal authentication procedures to access a system.") 
   print("              As a result, remote access is granted to resources within an application,") 
   print("              such as databases and file servers, giving perpetrators the ability to remotely") 
   print("                            issue system commands and update malware.")
   print("")
   print("")