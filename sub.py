import ipaddress
import os
xstr= """\033[91m
         👑 ━─━  ☚➳нɑм亗ɑdɑ☛  ━─━ 👑
           
         ☛ Join Telegram ¬ t.me/klinuxsd

"""
os.system('clear')
os.system('figlet Subnet-S')
print(xstr)

with open("subnets.txt", "r") as f:
        ip = f.read().splitlines()
with open('ip.txt','w') as f:
	for line in ip:
		for xip in ipaddress.IPv4Network(line):
			f.write(str(xip)+'\n')
os.system('clear')		
port = input('Which port you want to scann 443 or 80 ?\n')
if port == '80':
    os.system('bugscanner ip.txt --port 80 --method get --o hosts.txt')
elif port == '443':
   os.system('bugscanner ip.txt --port 443 --method get --o hosts.txt')
print('Saved in hosts.txt')   
os.system("cat hosts.txt")
