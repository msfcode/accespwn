#!/usr/bin/env python
#this tool is coded by msfcode
#DO NOT COPY OR EDIT IT
#ASK PERMISSION  BEFORE USE ITs
import os
import sys
import subprocess
print('\u001b[1m')
def pip3():
 try:
  print('\u001b[37m')
  subprocess.call('apt-get install python3-pip', shell=True)
  print('')
  print('\u001b[32m                                         pip3 is installed')
 except:
   print('their is an error contact us at @msfcode ! try to install pip3')
pip3()
print('')
def pip():
 try:
  print('\u001b[37m')
  subprocess.call('apt-get install pip', shell=True)
  print('')
  print('\u001b[32m                                          pip is installed')
 except:
   print('\u001b[31mcontact me at msfcode if their is an error ! try to install pip')
pip()
print('')
def scapyer():
 try:
   print('\u001b[37m')
   subprocess.call('pip install scapy',shell=True)
   print('')
   print('\u001b[32m                                        scapy is installed')
 except:
  print('\u001b[31mtheir is an error !! try to fix it !! try to install scapy')
scapyer()
print('')
def scapyhttp():
  try:
   print('\u001b[37m')
   subprocess.call('pip3 install scapy-http',shell=True)
   print('')
   print('\u001b[32mscapy-http is installed')
  except:
   print('\u001b[31mtheir is an error !! try to fix it !! try to install scapy-http')
print('')
def pyinstalla():
 try:
    print('\u001b[37m')
    subprocess.call('pip install pyinstaller',shell=True) 
    print('')
    print('\u001b[32m                                  pyinstaller is installed')
 except:
  print('\u001b[31mtheir is an error !! try to fix it !! try to install pyinstaller')
pyinstalla()
def pynput():
  try:
   print('\u001b[37m')
   subprocess.call('pip install pynput', shell=True)
   print('')
   print('\u001b[32m                                         pynput is installed')
  except:
   print('\u001b[31mtheir is an error contact us at @msfcode ! try to install pynput Module')
   print('to install pynput :')
   print('\u001b[32mpip install pynput')
pynput()
def sslstrip():
 try:
   print('')
   subprocess.call('git clone https://github.com/moxie0/sslstrip', shell=True)
   subprocess.call('pip3 install virtualenv', shell=True)
   subprocess.call('virtualenv -p python2 sslstripenv', shell=True)
   subprocess.call('. sslstripenv/bin/activate', shell=True)
   subprocess.call('cd sslstrip',shell=True)
   subprocess.call('pip install Twisted pyOpenSSL service_identity',shell=True)
   print('')
   print('sslstrip is succesfully installed')
 except:
   print('')
   print('\u001b[31mtheir is an error contact us at @msfcode ! try to install sslstrip')
   print('')
def netfilterqueuea():
 try:
    print('')
    subprocess.call('\u001b[37mapt-get install build-essential python-dev libnetfilter-queue-dev',shell=True)
    subprocess.call('pip3 install -U git+https://github.com/kti/python-netfilterqueue', shell=True)
    print('')
    print('\u001b[32m                               NetFilterQueue is installed')
 except:
   print('\u001b[31mtheir is an error !! try to install netfilterqueue')
netfilterqueuea()
sslstrip()
print(''' \u001b[33m

					       Good Job, Dude, now you are ready to use accespwn
						             ./accespwn
				  (this tool is for educationaly purpose , i'm not responsable of your actions)

					  [+]instagram : msfcode if you have any question about this tool[+]
''')