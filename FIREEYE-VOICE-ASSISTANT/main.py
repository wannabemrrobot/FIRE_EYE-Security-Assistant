import random                               # Random function
from microphone import listenCmd           # Speech-to-text
from voiceback import talkvoice             # Text-to-Speech
from playsound import playsound             # Playing pre-defined alerts
from csrf import detect_csrf                # Cross-Site Request Forgery
import banner
from linux_audit import audit

def edith(command):
    command_list = command.split(" ")
    if "csrf" in command_list or "CSRF" in command_list or "cross" in command_list or "request" in command_list:
        talkvoice("Enter the Web Application URL that you want to assess for cross site request forgery")
        print("1. Manual (Accurate)\n"
              "2. Voice (Subjective to BG noise)")
        url = ""
        choice = input(">> ")
        if choice == str(1):
            url = input("[!] Enter the URL for CSRF Assessment : ")
            detect_csrf(url)
        if choice == str(2):
            detect_csrf(url)
    ###########################################
    if "lynis" in command or "system" in command or "audit" in command or "linux" in command:
        audit()

errors = ["Cannot find a proper solution", "Decision could not be made"]
#playsound("./NOVA_CONFIG/SOUNDS/SCRIPT_GREET/nova-init.mp3")
banner.display()
while True:
    edith(listenCmd())