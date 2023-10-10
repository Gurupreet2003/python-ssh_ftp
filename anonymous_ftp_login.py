#!/usr/bin/python

import ftplib	#connection library

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)		# connection
		ftp.login('anonymous', 'anonymous')	#login function  user and password is anonymous
		print(hostname, " FTP Anonymous Logon Succeeded.")
		ftp.quit()	#ftp connection closed
		return True
	except Exception, e:	#any error that occur exception, e
		print(hostname, " FTP Anonymous Logon Failed")


host = input("Enter the IP Address : ")
anonLogin(host)

