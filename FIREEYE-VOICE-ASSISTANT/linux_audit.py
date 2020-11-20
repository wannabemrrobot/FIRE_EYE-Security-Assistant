import os
from colorama import Fore as f, Back as b, Style as s
import time

def audit():
    print(f.YELLOW + "[!] INFO : "+ b.YELLOW + f.BLACK + " Starting FIRE-EYE Full System Security Auditing..." + s.RESET_ALL)
    time.sleep(4)
    print(f.YELLOW + "[!]" + s.RESET_ALL + " Performing Audit on :")
    time.sleep(1)
    print(b.RED + "[+] SYSTEM      " + s.RESET_ALL)
    time.sleep(1)
    print(b.RED + "[+] KERNEL      " + s.RESET_ALL)
    time.sleep(1)
    print(b.RED + "[+] NETWORK     " + s.RESET_ALL)
    time.sleep(1)
    print(b.RED + "[+] PERMISSIONS " + s.RESET_ALL)
    time.sleep(1)
    print(b.RED + "[+] SERVICES    " + s.RESET_ALL)
    time.sleep(1)
    print(b.RED + "[+] DISTRO      " + s.RESET_ALL)
    time.sleep(1)
    print(b.RED + "[+] EXTERNAL    " + s.RESET_ALL)
    print("")
    time.sleep(3)
    print(f.YELLOW + "[!] INFO : " + s.RESET_ALL + "Please wait till the scan is finished. Reports will be generated in the form of HTML.")
    time.sleep(1)
    print(f.YELLOW + "[!] INFO : " + s.RESET_ALL + " Thus, automatically reports will be displayed in your default browser.")
    time.sleep(3)
    print(b.YELLOW + f.BLACK + "[+] DEFAULT : Firefox" + s.RESET_ALL)
    time.sleep(3)
    command = "echo 1999 | sudo -S otseca --ignore-failed --tasks system,kernel,network,permissions,services,distro,external -o ~/security-audit/report/"
    os.system(command)

    command2 = "echo 1999 | sudo -S chown -Rf pavisrini:pavisrini ~/security-audit"
    os.system(command2)

    default_location = "/home/pavisrini/security-audit/report/"
    for dirpath, dirname, filename in os.walk(default_location):
        dir_list = dirname
        break

    sufix = 1
    int_list = [1,2,3,4,5,6,7,8,9,0]
    for dnames in dir_list:
        source = default_location + dnames
        destination = default_location + str(sufix)
        try:
            if int(dnames) in int_list:
                pass
        except:
            cmd = "sudo mv " + source + " " + destination
            os.system(cmd)
            sufix = sufix + 1

    for dpath, dname, fname in os.walk(default_location):
        dlist = dname
        break
    l = len(dlist)
    report_launch = "cd " + "~/security-audit/report/" + str(l-1) + "/" + " && firefox index.html &"
    os.system(report_launch)
#audit()