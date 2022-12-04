#!/usr/bin/env python3

#Python Libraries used in our port scanner
import socket
import sys
from datetime import datetime

#Local Subs
def outputSeparator():
    print("=" * 60)

#We'll incremement portsOpen when we find an open port
portsOpen = 0

#The ports dictionary contains a list of Application layer protocols & port numbers
ports = {"FTP": 21, "SSH": 22, "SMTP": 25, "HTTP": 80, "HTTPS": 443, "Minecraft": 25565}

#Ask for the host (IP Address or host name) we will scan
#If nothing is entered, scan the local machine
remoteServer = input("Enter host to scan: ")
if len(remoteServer) == 0 :
    remoteServer ="127.0.0.1"
#Translates a host name (eg www.example.com) into an IP Address
remoteServerIP = socket.gethostbyname(remoteServer)


#Inform the user when the scan starts
timeOfStart = datetime.now()
outputSeparator()
print("Port scan on", remoteServer, "started at", timeOfStart)
outputSeparator()


#Now iterate through the dictionary to see which of the ports we are interested in are open
#Alternatively, you could use something like for portNumber in range (1,5000): to ensure you don't miss any out
for protocolName, portNumber in ports.items():
    
        #Setup the socket for use
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
         
        #Make the connection to the server/port
        result = s.connect_ex((remoteServerIP,portNumber))
        if result == 0:
            #Port is open
            status = "[X]"
            portsOpen += 1
        else:
            #Port is not accessible
            status = "[ ]"
        s.close()
        
        #Output the result of this port scan
        print(status, protocolName, portNumber)

#Inform the user when the scan ends as well as a summary of ports open
timeOfEnd = datetime.now()
outputSeparator()
print("Port scan on", remoteServer, "ended at", timeOfEnd)
outputSeparator()
print("Ports open on", remoteServer, ":" , portsOpen)
outputSeparator()
