# made by shmadul (mason), made more sexy with python by 666trapgod
import os
import sys
from array import *
import string
import random
import time

if len(sys.argv) < 3:
	print "Usage: python "+sys.argv[0]+" <amount> <output file>"
	sys.exit()

amount = sys.argv[1]
output_file = sys.argv[2]


g810_rgb = "1811MR05"
g810_red = "1806MR06"
g502_rgb = "1703LZ0H"
g933_hds = "1625ML00"
brio_uhd = "1708LZ0H"
g610_bck = "1701MR02"


print("\033]0;Logitech Serial Gen | Made by: Mason & 666TRAPGOD\007")                                                            
print("\x1b[38;5;196m   __            _ _           _      _____ _____    _____         ")
print("\x1b[38;5;196m  |  |   ___ ___|_| |_ ___ ___| |_   |   __|   | |  |   __|___ ___ ")
print("\x1b[38;5;196m  |  |__| . | . | |  _| -_|  _|   |  |__   | | | |  |  |  | -_|   |")
print("\x1b[38;5;196m  |_____|___|_  |_|_| |___|___|_|_|  |_____|_|___|  |_____|___|_|_|")
print("\x1b[38;5;196m            |___|                                                  ")
print("                                                                                 ")
print("\033[1;32m                     CODED BY MASON & 666TRAPGOD                       ")
print("\x1b[0m                                                                          ")

choose_nigga = input("[+] Press 1 for G810_RBG | Press 2 for G810_RED | Press 3 for G502_RGB [+]\r\n[+] Press 4 for G933_HDS | Press 5 for BRIO_UDH | Press 6 for G610_BCK [+]\r\n")
print(choose_nigga)

print("\x1b[38;5;196m[+] Serial Numbers: [+]")
print("")

if (choose_nigga == 1):
    for n in range(int(amount)):
	try:
		amount = random.randint(0000,9999)

		huh = str(random.randint(1,9))
		shit = "%s%d"%(g810_rgb,amount)
		real = shit.replace(" ", huh)

		print("\033[94m"+real) #print it out
		os.system("echo "+real+" >> "+output_file) #output it to file
	except KeyboardInterrupt:
        	os.kill(os.getpid(), 9)


if (choose_nigga == 2):
    for n in range(int(amount)):
	try:
		amount = random.randint(0000,9999)

		huh = str(random.randint(1,9))
		shit = "%s%d"%(g810_red,amount)
		real = shit.replace(" ", huh)

		print("\033[94m"+real) #print it out
		os.system("echo "+real+" >> "+output_file) #output it to file
	except KeyboardInterrupt:
        	os.kill(os.getpid(), 9)


if (choose_nigga == 3):
    for n in range(int(amount)):
	try:
            k = "".join(random.choice(string.ascii_uppercase) for _ in range(1))
            r = "".join(random.choice(string.ascii_uppercase) for _ in range(1))
            amount = random.randint(0,9)
            anothaone = random.randint(0,9)

            huh = str(random.randint(1,9))
            shit = "%s%s%d%s%d"%(g502_rgb,k,amount,r,anothaone)#combo|letter|number|letter|number
            real = shit.replace(" ", huh)

            print("\033[94m"+real) #print it out
            os.system("echo "+real+" >> "+output_file) #output it to file
        except KeyboardInterrupt:
                os.kill(os.getpid(), 9)


if (choose_nigga == 4):
    for n in range(int(amount)):
	try:
            k = "".join(random.choice(string.ascii_uppercase) for _ in range(1))
            r = "".join(random.choice(string.ascii_uppercase) for _ in range(1))
            amount = random.randint(0,9)
            anothaone = random.randint(0,9)

            huh = str(random.randint(1,9))
            shit = "%s%s%s%d%d"%(g933_hds,k,r,amount,anothaone)#combo|letter|letter|number|number
            real = shit.replace(" ", huh)

            print("\033[94m"+real) #print it out
            os.system("echo "+real+" >> "+output_file) #output it to file
        except KeyboardInterrupt:
                os.kill(os.getpid(), 9)


if (choose_nigga == 5):
    for n in range(int(amount)):
	try:
            k = "".join(random.choice(string.ascii_uppercase) for _ in range(1))
            r = "".join(random.choice(string.ascii_uppercase) for _ in range(1))
            w = "".join(random.choice(string.ascii_uppercase) for _ in range(1))
            amount = random.randint(0,9)

            huh = str(random.randint(1,9))
            shit = "%s%s%s%s%d"%(brio_uhd,k,r,w,amount)#combo|letter|letter|number|number
            real = shit.replace(" ", huh)

            print("\033[94m"+real) #print it out
            os.system("echo "+real+" >> "+output_file) #output it to file
        except KeyboardInterrupt:
                os.kill(os.getpid(), 9)


if (choose_nigga == 6):
    for n in range(int(amount)):
	try:
            k = "".join(random.choice(string.ascii_uppercase) for _ in range(1))
            amount = random.randint(0,9)
            anothaone = random.randint(0,9)
            okthen = random.randint(0,9)

            huh = str(random.randint(1,9))
            shit = "%s%s%d%d%d"%(g610_bck,k,amount,anothaone,okthen)#combo|letter|number|number|number
            real = shit.replace(" ", huh)

            print("\033[94m"+real) #print it out
            os.system("echo "+real+" >> "+output_file) #output it to file
        except KeyboardInterrupt:
                os.kill(os.getpid(), 9)
