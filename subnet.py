import ipaddress
import os
xstr= """\033[91m
         👑 ━─━  ☚➳нɑм亗ɑdɑ☛  ━─━ 👑
           
         ☛ Join Telegram ¬ t.me/klinuxsd

"""
os.system('clear')
os.system('figlet Subnet-S')
print(xstr)

m = input('ENTER SUBDOMAIN EX.127.0.0.1/24 :: ')
with open('ip.txt','w') as f:
	for xip in ipaddress.IPv4Network(m):
		f.write(str(xip)+'\n')
os.system('clear')		
port = input('Which port you want to scann 443 or 80 ?\n')
if port == '80':
    os.system('bugscanner ip.txt --port 80 --method get --o hosts.txt')
elif port == '443':
   os.system('bugscanner ip.txt --port 443 --method get --o hosts.txt')
print('Saved in hosts.txt')   
    
		
		
