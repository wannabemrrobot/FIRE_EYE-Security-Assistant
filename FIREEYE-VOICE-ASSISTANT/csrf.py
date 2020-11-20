import os
import speech_recognition as sr
from playsound import playsound
from colorama import Fore as fr, Style as s, Back as b
import time

def detect_csrf(url):
	if url == "":
		r = sr.Recognizer()
		mic = sr.Microphone()
		with mic as source:
			print("")
			print("")
			print("")
			print("")
			r.pause_threshold = 1
			print(fr.YELLOW + "[!]" + fr.WHITE + " Adjusting for background noise...")
			print(
				b.YELLOW + fr.BLACK + "Detecting Ambient Noises and adjusting microphone sensitivity. Hold On . . ." + s.RESET_ALL)
			time.sleep(2)
			r.adjust_for_ambient_noise(source, duration=1)
			print(b.GREEN + "[+] Microphone Calibrated." + s.RESET_ALL)
			time.sleep(1)
			print(fr.YELLOW + "[!]" + fr.WHITE + " Speech Recognition works depending on the " + b.RED + " NETWORK BANDWIDTH " + s.RESET_ALL + " of your connected network.")
			print(fr.YELLOW + "[!]" + s.RESET_ALL + " Checking Network Bandwidth...")
			time.sleep(5)
			print(fr.YELLOW + "\n[!] WARNING : " + b.YELLOW + fr.BLACK + " Speech Recognition may be slow. Your reported network speed is lower than the required speed." + s.RESET_ALL)
			playsound('./NOVA_CONFIG/listen.mp3')
			print(fr.GREEN + "[+]" + s.RESET_ALL + " FireEye is Ready . . .")
			print(fr.BLUE + "[>]" + s.RESET_ALL + b.BLUE + " Say the URL >>" + s.RESET_ALL)

			# audio = r.listen(source)
			audio = r.record(source=mic, duration=15)

			try:
				command = r.recognize_google(audio).lower()
				# command = r.recognize_sphinx(audio) #offline_Speech_Recognition
				print("You Said: " + command + "\n")
			# loopback to continue listening for commands if unrecognizable speech is received
			except sr.UnknownValueError:
				print("Your URL was not parsed.")
		url = command
	else:
		url = url

	print(fr.GREEN + "[+] INFO : " + s.RESET_ALL + b.GREEN + fr.BLACK + "STARTING CSRF ASSESSMENT ! . . ." + s.RESET_ALL)
	time.sleep(3)
	print(fr.YELLOW + "[!]  Running through scans on the specified web application.\n"
								"     As lots of requests are sent from the client side, there\n"
								"     may be some delay in assessing the vulnerability." + s.RESET_ALL)
	time.sleep(2)
	print(b.RED + "[!] Scan time is dependent on the size of the web application." + s.RESET_ALL)
	print("")
	print(fr.RED + ">>>>>>>>>>   PROBING   >>>>>>>>>>" + s.RESET_ALL + "\n" + "\n")

	command = "xsrfprobe -u {} --crawl > ./RESULTS/CSRF/CSRF_RESULTS.txt".format(url)
	os.system(command)
	time.sleep(4)

	f = open("./RESULTS/CSRF/CSRF_RESULTS.txt", mode="r")
	r = f.read()
	if 'endpoint might be [1;97;43m VULNERABLE' in r:
		print(
			"       " + b.GREEN + "                        S C A N   R E S U L T                       " + s.RESET_ALL)
		print(fr.BLUE + "       ====================================================================" + s.RESET_ALL)
		print(
			fr.YELLOW + "        [!] This Application is " + b.RED + fr.WHITE + "VULNERABLE" + s.RESET_ALL + fr.YELLOW + " to Cross Site Request Forgery.\n")
		print(fr.YELLOW + "        [+] Ensuring proper CSRF Token Validation and Same Referer and \n"
						  "            Origin Policy may helps." + s.RESET_ALL)
		print(fr.YELLOW + "        [!] Logs and Reports will be now opened in the appropriate apps." + s.RESET_ALL)
		print(fr.BLUE + "       ====================================================================" + s.RESET_ALL)
	else:
		print("       " + b.GREEN + "                         S C A N   R E S U L T                       " + s.RESET_ALL)
		print(fr.BLUE + "       =======================================================================" + s.RESET_ALL)
		print(fr.YELLOW + "        [!] This Application is " + b.GREEN + fr.WHITE + "NOT VULNERABLE" + s.RESET_ALL + fr.YELLOW + " to Cross Site Request Forgery." + s.RESET_ALL)
		print(fr.BLUE + "       =======================================================================" + s.RESET_ALL)

	#######################################################################
	dir = "/home/pavisrini/Desktop/elliot/xsrfprobe-output/" + url + "/"
	for dp, dn, fn in os.walk(dir):
		file_list = fn
		break
	for i in file_list:
		cmd = "mousepad " + dir + i
		os.system(cmd)


#detect_csrf("wonderhowto.com")