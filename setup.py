import os

os.system("clear")
os.system("pkg install git python &&  git clone https://github.com/aztecrabbit/bugscanner && cd bugscanner && pip install loguru && pip install requests setuptools && python -m pip install -r requirements.txt && python3 setup.py install")
print("Successfully Installed \nrun sub.py to scan subnets or \nsubnet.py to scan signal subnet")
