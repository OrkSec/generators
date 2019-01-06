# made by 666trapgod
import sys
import random
import os
import time
from array import *
import string

if len(sys.argv) < 4:
	print "Usage: python "+sys.argv[0]+" <amount> <combo> <output file>"
	sys.exit()

print("\033]0;Netflix GC Gen | Made by: 666TRAPGOD\007")
print("\x1b[38;5;196m   _   _      _    __ _ _         ____ _  __ _                    _    ____            ")
print("\x1b[38;5;196m  | \ | | ___| |_ / _| (_)_  __  / ___(_)/ _| |_ ___ __ _ _ __ __| |  / ___| ___ _ __  ")
print("\x1b[38;5;196m  |  \| |/ _ \ __| |_| | \ \/ / | |  _| | |_| __/ __/ _` | '__/ _` | | |  _ / _ \ '_ \ ")
print("\x1b[38;5;196m  | |\  |  __/ |_|  _| | |>  <  | |_| | |  _| || (_| (_| | | | (_| | | |_| |  __/ | | |")
print("\x1b[38;5;196m  |_| \_|\___|\__|_| |_|_/_/\_\  \____|_|_|  \__\___\__,_|_|  \__,_|  \____|\___|_| |_|")
print("                                                                                                     ")
print("\033[1;32m                                 CODED BY 666TRAPGOD                                       ")
print("\x1b[0m                                                                                              ")

amount = sys.argv[1]
combo = sys.argv[2] # eg: LEQ
output_file = sys.argv[3]

print("\x1b[38;5;196m[+] Codes: [+]")
print("")

for n in range(int(amount)):
	try:
		y = "".join(random.choice(string.ascii_uppercase) for _ in range(2))
		amount = random.randint(000000,999999)
		huh = str(random.randint(1,9))
		shit = "%s%s%6d"%(combo,y,amount)
		real = shit.replace(" ", huh)
		print("\033[93m"+real) #print it out
		os.system("echo "+real+" >> "+output_file) #output it to file
	except KeyboardInterrupt:
        	os.kill(os.getpid(), 9)
