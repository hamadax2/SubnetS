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
port = input('Which port you want to scann ?\n')
os.system(f'bugscanner ip.txt --port {port} --method get --o hosts.txt')
print('Saved in hosts.txt')
os.system("cat hosts.txt")
