#!/usr/etc/python
#!/usr/etc/bash
import sys,os,platform
from time import *
x = platform.system()
import requests
from tqdm import tqdm
import random
import time
G = "\033[32;1m" 
Gt = "\033[0;32m" 
Bt = "\033[34;1m" 
b = "\033[36;1m" 
R = "\033[31;1m" 
c = "\033[0m" 
W = "\033[37;1m" 
u = "\033[35;1m" 
M = "\033[3;1m" 
k = "\033[33;1m" 
kt = "\033[0;33m" 
a = "\033[30;1m" 
#
#
os.system("pkg install mpv")
os.system("sleep 2")
print " "+Bt+" NIKMATI LAGUNYA"
os.system("mpv hbd.mp3;clear")
os.system("clear")
print ""+k+"\t\t[ WELCOME TO SCRIPT ULTAH]"
nama = raw_input(""+Bt+"[ NAMA YANG ULATAH]>> "+W+" ")
os.system("clear")
print ""+k+"\t\t[ WELCOME TO SCRIPT ULTAH]"
print ""
print ""+W+"Selamat Datang "+G+"[", nama,"]"+W+" Semoga Kamu Sehat Selalu"
os.system("sleep 2")
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)
mengetik(" "+Bt+" SAYA MEMPUNYAI DOA UNTUK KAMU YANG SEDANG ULANG TAHUN")
os.system("sleep 2")
os.system("sleep 2")
mengetik(" "+u+"SEMOGA ALLOH MEMBERIKAN REZEKI YANG BYK, DOSANYA DI AMPUNI OLEH ALLOH")
os.system("sleep 2")
os.system("sleep 2")
mengetik(" "+W+"DOSA ORNG TUANYA DI AMPUNI OLEH ALLOH, DI BERIKAN JALAN YANG LURUS AMIN...")
os.system("sleep 3")
os.system("sleep 3")
mengetik(" "+G+" AMIN...")
os.system("sleep 3")
os.system("sleep 3")
print " "+u+" AMIN..."
os.system("sleep 3")
os.system("sleep 3")
mengetik(" "+Gt+" YA ROBAL ALAMIN ALFATIHAH")
os.system('figlet SELAMAT| lolcat')
os.system('figlet ULANG| lolcat')
os.system('figlet TAHUN| lolcat')
os.system("sleep 3")
os.system("sleep 3")
os.system('xdg-open http://allpaint.co.za/ulang-tahun.html')
