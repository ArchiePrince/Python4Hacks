#! /usr/bin/python

#==============================================================#
#This python code simply scans a given port on a specified host#
#import the socket package for connection		       #	
#==============================================================#

import socket

#This is to create an object of socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#declare variables and receive inputs from user for the host and port

host = input("[*] Enter the Host address to scan: ")
port = input("[*] Enter the Port to scan: ")

port = int(port)


# A function that scans if a port is closed or opened.
def portscanner(port):
	if soc.connect_ex((host, port)):
		print ("Port %d is closed!" % (port))
	else:
		print ("Port %d is opened!" % (port))

portscanner(port)
