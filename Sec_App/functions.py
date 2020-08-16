import random,textwrap,re,os,json
import requests,time
from datetime import datetime

def greet():

    greets = ["Hi!","Hello Sir!","Hello Boss!","Hello Bro!","Hi Dude! Wassup!","Hi Bro!","Yo! Wassup","Hey!Sup!"]
    ans = greets[random.randint(0,(len(greets)-1))]
    return ans

def launcher(command):
    import os
    words = command.split(" ")
    program = words[-1]
    print(program)
    os.system(program)
    ans ="Application launched..."
    return ans

def nmapScan(command = "104.193.19.59"):
    #s = command.split(" ")
    network = command
    result =""
    json = {}
    p_s=[]
    print("[+] Scanning the network {} for open ports".format(network))
    import nmap
    nmScan = nmap.PortScanner() #Initialise the portScanner
    nmScan.scan(network)    #Scanning the network

    for host in nmScan.all_hosts():
        
        json['host'] = str(host)
        s = "HOST : " + str(host) +"\n"
        s = s + " " * (40 - len(s))
        a = []
        a.append(s)

        s="STATE: " + str(nmScan[host].state()) + "\t"
        json['state'] = str(nmScan[host].state()).upper()
        s = s + " " * (40 - len(s))
        a.append(s)

        s="NAME : " + nmScan[host].hostname().upper()
        json['name'] = nmScan[host].hostname().upper()
        s = s + " " * (40 - len(s))
        a.append(s)

        for proto in nmScan[host].all_protocols():

            s = "PROTOCOL : " + proto.upper()
            json['protocol'] = proto.upper()
            s = s + " " * (40 - len(s))
            a.append(s)

            s = "- - - - - - -  "
            s = s + " " * (40 - len(s))
            a.append(s)

            s = "PORTS" + "\t" + "STATE"
            s = s + " " * (40 - len(s))
            a.append(s)

            lport = nmScan[host][proto].keys()
            #lport.sort()
            for port in lport:
                t=[]
                t.append(str(port))
                t.append(nmScan[host][proto][port]['state'].upper())
                s = "\t" + str(port) + "\t" + nmScan[host][proto][port]['state'].upper()
                s = s + " "*(40 - len(s))
                a.append(s)
                p_s.append(t)
        json['ps'] = p_s
        original = ''.join(a)
        wrapper = textwrap.TextWrapper(width=40)
        dedented_text = textwrap.dedent(text=original)
        result = wrapper.fill(text=dedented_text)
        return [result,json]

def check(Ip):
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
    if (re.search(regex, Ip)):
        return 1
    else:
        return 0

def detect_csrf(url):
    command = "xsrfprobe -u {} --crawl > Sec_App/csrf-result.txt".format(url)
    #print(command)
    cht_result=""
    result=[]
    os.system(command)
    f = open("Sec_App/csrf-result.txt", mode="r")
    r = f.read()
    #print(r)
    if 'endpoint might be [1;97;43m VULNERABLE' in r:
        cht_result = cht_result + "This Application is vulnerable to Cross Site Request Forgery.\n   "
        cht_result = cht_result + "Ensuring proper CSRF Token Validation and Same Referer and Origin Policy may help."
        result.append("THIS APPLICATION IS VULNERABLE TO CROSS SITE REQUEST FORGERY.")
        result.append("ENSURING PROPER CSRF TOKEN VALIDATION AND SAME REFERER AND ORIGIN POLICY MAY HELP.")

        wrapper = textwrap.TextWrapper(width=38)
        dedented_text = textwrap.dedent(text=cht_result)
        cht_result = wrapper.fill(text=dedented_text)

        return [cht_result,result]
    else:
        cht_result = "This application is not vulnerable to Cross Site request Forgery."
        result.append("THIS APPLICATION IS NOT VULNERABLE TO")
        result.append("CROSS SITE REQUEST FORGERY")

        wrapper = textwrap.TextWrapper(width=40)
        dedented_text = textwrap.dedent(text=cht_result)
        cht_result = wrapper.fill(text=dedented_text)
        return [cht_result,result]

def curl(url):
    print(url)
    try:
        r = requests.get(url)
        print(r)
        return "HOST IS ALIVE"
    except:
          return "HOST IS NOT ALIVE"






#talk("Which network you want to scan ?")104.193.19.59
