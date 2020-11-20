import speech_recognition as sr
from playsound import playsound
import time
from colorama import Fore as f, Style as s, Back as b

def listenCmd():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("")
        print("")
        print("")
        print("")
        r.pause_threshold = 1
        print(f.YELLOW + "[!]" + f.WHITE + " Adjusting for background noise...")
        print(b.YELLOW + f.BLACK + "Detecting Ambient Noises and adjusting microphone sensitivity. Hold On . . ." + s.RESET_ALL)
        time.sleep(2)
        r.adjust_for_ambient_noise(source, duration=1)
        print(b.GREEN + "[+] Microphone Calibrated." + s.RESET_ALL)
        time.sleep(1)
        print(f.YELLOW + "[!]"  + f.WHITE + " Speech Recognition works depending on the " + b.RED  + " NETWORK BANDWIDTH " + s.RESET_ALL + " of your connected network.")
        print(f.YELLOW + "[!]" + s.RESET_ALL + " Checking Network Bandwidth...")
        time.sleep(5)
        print(f.YELLOW + "\n[!] WARNING : " + b.YELLOW + f.BLACK + " Speech Recognition may be slow. Your reported network speed is lower than the required speed." + s.RESET_ALL)
        playsound('./NOVA_CONFIG/listen.mp3')
        print(f.GREEN + "[+]" + s.RESET_ALL +" FireEye is Ready . . .")
        print(f.BLUE + "[>]"+ s.RESET_ALL + b.BLUE + " Say your command >>" + s.RESET_ALL)

        #audio = r.listen(source)
        audio = r.record(source=mic, duration=15)

        try:
            command = r.recognize_google(audio).lower()
            #command = r.recognize_sphinx(audio) #offline_Speech_Recognition
            print("You Said: " + command + "\n")
        #loopback to continue listening for commands if unrecognizable speech is received
        except sr.UnknownValueError:
            print("Your last command couldn\'t be heard.")
            command = listenCmd()

        return command

#listenCmd()