#!/usr/bin/python3

import json
import requests
import time
import os

time.sleep(.1)

R = '\033[91m'  # red
G = '\033[92m'  # green
B = '\033[94m'  # blue

print ("""\n%s_________| WP-Admin Exposer |_________________________________________
%s                  _  _   _______  .__  __    __ 
               __| || |__\      \ |__|/  |__/  |______    _____ 
               \   __   //   |   \|  \   __\   __\__  \  /     \ 
    ./c0d3d By  |  ||  |/    |    \  ||  |  |  |  / __ \|  Y Y  \\
               /_  ~~  _\____|__  /__||__|  |__| (____  /__|_|  /
                 |_||_|         \/                    \/      \/ \n
%s___________________________________________| %sEminenceways.com%s |_______""" % (B, G, B, G, B))

time.sleep(.2)

def start():
		print("%s______________________________________________________________________" %(B))
		url = input(r"%s Target Site : %s" %(B, G))

		r = requests.get(url+"/wp-json/wp/v2/users")
		# print(r.url)
		data = r.text
		output = json.loads(data)

		print ("\n\n%s_______________________| %sGrabbed Information%s |________________________%s\n\t\t" %(B, G, B, G))

		if "rest_user_cannot_view" in r.text :
			print(output["message"])
		else:
			for loop in output:
				print (">>\033[94m Name         :\033[92m ", loop["name"])
				print (" >>\033[94m Username     :\033[92m ", loop["slug"] ,"\033[91m(Possible Username!!!)\033[92m")
				pic = (loop["avatar_urls"]["96"]).replace("?s=96","?s=1000")
				print (" >>\033[94m User Photo   : \033[92m "+pic)
				print (" >>\033[94m User ID      :\033[92m ", loop["id"])
				print (" >>\033[94m Url          :\033[92m ", loop["url"])
				print (" >>\033[94m Description  :\033[92m ", loop["description"])
				print ("\n")

		print ("%s_________________________| %sScan Complete!!!%s |_________________________" %(B, G, B))

while True:
		switch = input("\n%s Continue / Exit (C/E) : " %(R ))
	
		if (switch == 'C' or switch == 'c'):
				start()

		elif (switch == 'e' or switch == 'E'):
				print("\n")
				time.sleep(.5)
				print(" ||||||||||||||||||||||||| %s(25)" % (G ))
				time.sleep(.7)
				print("%s ||||||||||||||||||||||||||||||||||||||| %s(50)" % (R, G ))
				time.sleep(1)
				print("%s ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| %s(100)" % (R, G ))
				time.sleep(1.5)
				os.system("clear")
				exit()
# start()
		else:
			print ("""\n%s______________________________________________________________________
		                                         
		         %sInvalid Command Detected!!!
%s______________________________________________________________________\n"""  % (B, G, B))
			break
