import os
import time
time.sleep(10)
os.system("ping {} -c4 > host_result.txt &".format(host))
with open('./host_result.txt', 'r') as f:
    lines = f.read()
    if '4 packets transmitted, 0 received' in lines:
        print("[!] This site is vulnerable to Denial Of Service Attack")
        exit()
    else:
        print("[+] This site is not Vulnerable to Denial Of Service Attack.")
        exit()