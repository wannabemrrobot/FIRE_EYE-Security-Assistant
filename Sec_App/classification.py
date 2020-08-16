import random
def classifier(query):

    query.lower()
    greets=["hi","hello","hey","sup?","yo"]
    greet_resp = ["Hi!","Hello Sir!","Hello Boss!","Hello Bro!","Hi Dude! Wassup!","Hi Bro!","Yo! Wassup","Hey!Sup!"]
    if query in greets:
        ans = greet_resp[random.randint(0,(len(greets)-1))]
        return ans

    csrf = ['csrf assessment', 'assessment', 'csrf', 'cross site request forgery',
            'xsrf', 'xsrfprobe', 'xsrf scan','xsrf assessment', 'csrf probe',
            'csrfprobe', 'xsrfprobe']

    port_scan = ['port scan', 'scan', 'scanning', 'port enumeration', 'open port',
                 'open ports', 'closed port', 'closed ports','port detection',
                 'blocked ports', 'ports', 'port']
    dos = ['denial of service', 'dos', 'load balancing', 'load balance', 'dos-ing']

    hostDiscovery = ['alive', 'is working', 'working', 'is alive', 'exits', 'is exist', 'discover', 'ping', 'host',
                     'discovery']

    neg_respone = ["Sorry, I'm not sure how to help with that.",
                   "Sorry, I don't know how to help with that yet. But I'm always learning",
                   "Sorry, I don't understand","Sorry, I can't help with that yet.But I'm still learning.",
                   "Sorry, I don't know how to help with that.","Sorry, I can't help with that yet.",
                   "Sorry, Can you be more clear?"]

    c_csrf = 0; c_ps = 0; c_dos = 0; c_hd = 0
    action_words = ['do', 'check', 'perform', 'execute', 'initiate', 'run', 'can', 'please', 'you', 'would', 'hey', 'hello', 'assistant', 'buddy', 'dude', 'pal', 'will', 'should', 'now']

    q = list(query.split(" "))  # Transform query to list for processing
    ql = list(dict.fromkeys(q))  # Removing Duplicates from query list
    action_count: int = 0

    for i in ql:  # Action check sequence
        if i in action_words:  # Removing action words in Query list for processing
            action_count = 1
            ql.remove(i)

    func_list = []
    for i in ql:
        if i in csrf:
            c_csrf = 1
            func_list.append(i)

    for i in ql:
        if i in port_scan:
            c_ps = 1
            func_list.append(i)

    for i in ql:
        if i in dos:
            c_dos = 1
            func_list.append(i)

    for i in ql:
        if i in hostDiscovery:
            c_hd = 1
            func_list.append(i)

    irrelevant_words = list(set(ql) - set(func_list))
    irrelevant_words = list(set(irrelevant_words) - set(action_words))
    ow = ['a', 'on', 'for', 'in', 'an', 'the', 'to', ' ', '']
    meaning_less_words = []
    for i in irrelevant_words:
        if i not in ow:
            meaning_less_words.append(i)

    if len(meaning_less_words) > 0:
        ans = neg_respone[random.randint(0, (len(neg_respone) - 1))]
        return ans

    binary_check = [c_csrf, c_ps, c_dos, c_hd]
    count = 0
    for i in binary_check:
        if i == 1:
            count = count + 1
        else:
            continue
    if (count > 1) or (count == 0):
        ans = neg_respone[random.randint(0, (len(neg_respone) - 1))]
        return ans
    else:
        for index, value in enumerate(binary_check):
            if value == 1:
                if index == 0:
                    return "CSRF Assessment"

                elif index == 1:
                    return "Port Scanning"

                elif index == 2:
                    return "DOS Assessment"

                elif index == 3:
                    return "Host Discovery"

            else:
                continue

# DRIVER CODE
#["CSRF Assessment","Port Scanning","DOS Assessment","Host Discovery"]