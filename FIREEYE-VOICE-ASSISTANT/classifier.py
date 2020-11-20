#!/usr/bin/python3
# Can be run with "./classifier.py" in terminal

def classifier2_0(query):
    csrf = ['csrf assessment', 'assessment', 'csrf', 'cross site request forgery', 'xsrf', 'xsrfprobe', 'xsrf scan',
            'xsrf assessment', 'csrf probe', 'csrfprobe', 'xsrfprobe']
    port_scan = ['port scan', 'scan', 'scanning', 'port enumeration', 'open port', 'open ports', 'closed port', 'closed ports',
                 'port detection', 'blocked ports', 'ports', 'port']
    dos = ['denial of service', 'dos', 'load balancing', 'load balance', 'dos-ing']
    hostDiscovery = ['alive', 'is working', 'working', 'is alive', 'exits', 'is exist', 'discover', 'ping', 'host',
                     'discovery']

    c_csrf = 0; c_ps = 0; c_dos = 0; c_hd = 0
    action_words = ['do', 'check', 'perform', 'execute', 'initiate', 'run',
                    'can', 'please', 'you', 'would', 'hey', 'hello', 'assistant',
                    'buddy', 'dude', 'pal', 'will', 'should', 'now']

    q = list(query.split(" "))  # Transform query to list for processing
    ql = list(dict.fromkeys(q))  # Removing Duplicates from query list
    print("-------------------------------------------------- \n[!] Initial Query list without duplicates: ", ql)
    action_count: int = 0

    for i in ql:  # Action check sequence
        if i in action_words:  # Removing action words in Query list for processing
            action_count = 1
            ql.remove(i)

    print("[i] Query_list without action_words:", ql)
    print("[i] Action count: " + str(action_count) + "\n --------------------")
    # Function count snippet
    func_list = []
    for i in ql:
        if i in csrf:
            c_csrf = 1
            func_list.append(i)
    print("[!] csrf: " + str(c_csrf))
    for i in ql:
        if i in port_scan:
            c_ps = 1
            func_list.append(i)
    print("[!] port_scan: " + str(c_ps))
    for i in ql:
        if i in dos:
            c_dos = 1
            func_list.append(i)
    print("[!] dos: " + str(c_dos))
    for i in ql:
        if i in hostDiscovery:
            c_hd = 1
            func_list.append(i)
    print("[!] hostDiscovery: " + str(c_hd) + "\n --------------------")

    # Removing prepositions, definite verbs, modal verbs, extra spaces.
    irrelevant_words = list(set(ql) - set(func_list))
    irrelevant_words = list(set(irrelevant_words) - set(action_words))
    print(irrelevant_words)
    ow = ['a', 'on', 'for', 'in', 'an', 'the', 'to', ' ', '']
    meaning_less_words = []
    for i in irrelevant_words:
        if i not in ow:
            meaning_less_words.append(i)
    print("[!] Meaning less words Found: ", meaning_less_words)

    # Exiting program if meaning less words are specified.
    if len(meaning_less_words) > 0:
        print("[!] Cannot process your query! Enter proper query.")
        exit()

    # Checking if more than one function is specified.
    binary_check = [c_csrf, c_ps, c_dos, c_hd]
    print("[!] Binary bits set for 4 func(): ", binary_check)
    count = 0
    for i in binary_check:
        if i == 1:
            count = count + 1
        else:
            continue
    if (count > 1) or (count == 0):
        print("[!] Cannot process your query! More than one function is specified.")
    else:
        for index, value in enumerate(binary_check):
            if value == 1:
                print(index, value)
                if index == 0:
                    print("[+] perforing CSRF.")
                if index == 1:
                    print("[+] perforing port scanning.")
                if index == 2:
                    print("[+] perforing DOS.")
                if index == 3:
                    print("[+] perforing Host Discovery.")
            else:
                continue

# DRIVER CODE
query = input("[!] Enter your query: ")
classifier2_0(query)
