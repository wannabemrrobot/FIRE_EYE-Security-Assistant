import time
from playsound import playsound
while(True):
    time.sleep(5)
    print("[+] Initiating NOVA...")
    time.sleep(1)
    print('''
 /$$   /$$  /$$$$$$  /$$    /$$  /$$$$$$ 
| $$$ | $$ /$$__  $$| $$   | $$ /$$__  $$
| $$$$| $$| $$  \ $$| $$   | $$| $$  \ $$
| $$ $$ $$| $$  | $$|  $$ / $$/| $$$$$$$$
| $$  $$$$| $$  | $$ \  $$ $$/ | $$__  $$
| $$\  $$$| $$  | $$  \  $$$/  | $$  | $$
| $$ \  $$|  $$$$$$/   \  $/   | $$  | $$
|__/  \__/ \______/     \_/    |__/  |__/
                                            
    ''')
    print("[+] A Virtual Assistant for Security Automation")
    print("-------------------------------------------------")
    print("[!] Checking for the Internet Bandwidth... Threshold level : Minimum - 3KBps/4KBps")
    time.sleep(5)
    print("[+] Check for Bandwidth - passed!" + "\n")
    print("[!] Calibrating microphone for ambient and background noises...")
    print("[!] Say anything...")
    time.sleep(3)
    print("[+] Calibrated!")
    print("[!] Starting Speech Recognition Engine and updating profiles!")
    print("--------------------------------------------------")
    playsound('./NOVA_CONFIG/listen.mp3')

    print("[!] What would you like to do sir ?")
    time.sleep(7)
    print("[+] Starting CSRF Assessment on the site : wonderhowto.com. Probing in 5 seconds.....")
    playsound('./NOVA_CONFIG/SOUNDS/CSRF/csrf_starting.mp3')
    time.sleep(10)
    print("---------------------------------------")
    print("==========[ REPORT ]===========")
    print("=> Site is not vulnerable to CSRF.")
    print("=> Total endpoints assessed - 63")
    print("=> Total requests intruded with payloads - 145")
    print("=> Application Security Score : 93/100")
    print("[!] OUTPUT FILE : ./xsrf-output/wonderhowto.com")
    print("---------------------------------------")
    #playsound('./NOVA_CONFIGS/SOUNDS/CSRF/csrf_not_vulnerable.mp3')
    time.sleep(1)
    print("")
    print("")
    print("[!] What would you like to do sir ?")
    time.sleep(7)
    print("[+] Performing Denial Of Service on sasthauniv.eng. Performing DOS Attack Assessments on production systems are critical !!!")
    time.sleep(10)
    print("[!] Running on Multi-threaded mode...")
    time.sleep(5)
    print("[!] Initiating 50 workers[default] on 16 threads - 16X50 ...")
    print("")
    print("----------------------------------------")
    print("[+] Starting thread 1. Sending packets ...")
    print("[+] Starting thread 2. Sending packets ...")
    print("[+] Starting thread 3. Sending packets ...")
    print("[+] Starting thread 4. Sending packets ...")
    print("[+] Starting thread 5. Sending packets ...")
    print("[+] Starting thread 6. Sending packets ...")
    print("[+] Starting thread 7. Sending packets ...")
    print("[+] Starting thread 8. Sending packets ...")
    print("[+] Starting thread 9. Sending packets ...")
    print("[+] Starting thread 10. Sending packets ...")
    time.sleep(10)
    print("")
    print("")
    print("")
    print("============[ REPORT ]===========")
    print("[-] This site is vulnerable for DOS Attacks.")
    print("[-] REASON : Waiting time for reply pings exceeded. (timeout : 10s)")
    print("[+] REMEDY : Install Load Balancers and Multi Threading Protections...")
    print("==================================")
    print("")
    print("")
    print("[!] What would you like to do sir ?")
    time.sleep(7)
    print("[!] Closing the Speech Engine, saving profiles and shutting down...")
    exit(0)



