# Files for classification texts
    set1 = open("./CLASSIFICATION/CSRF.txt", "r")       # index = 0
    set3 = open("./CLASSIFICATION/dos.txt", "r")        # index = 2
    set5 = open("CLASSIFICATION/linux_audit.txt", "r")  # index = 4

    for line in set1:
        # print(line)
        line = line.lower()
        csrf_words = line.split()
    # print(csrf_words)
    for line in set3:
        # print(line)
        line = line.lower()
        dos_words = line.split()
    # print(dos_words)
    for line in set5:
        # print(line)
        line = line.lower()
        linux_audit = line.split()
    # print(greet_words)

    temp_str = command
    # print(temp_str)
    score = []
    count = 0
    for i in range(0, len(csrf_words)):
        if (csrf_words[i] in temp_str):
            count = count + 1
    score.append(count)
    for i in range(0, len(dos_words)):
        if (dos_words[i] in temp_str):
            count = count + 1
    score.append(count)
    for i in range(0, len(linux_audit)):
        if (linux_audit[i] in temp_str):
            count = count + 1
    score.append(count)

    # print("[+] Score allocated: "+ score)
    index = score.index(max(score))
    print(index)
    if index == 0:
        url = input("[>>] Enter the application url to start assessment: ")
        talkvoice("Please enter the url for the Web application, that needs to be scanned for cross site request forgery.")
        detect_csrf(url)
    if index == 4:
        audit()
        talkvoice("Hello Security Engineer! Fire Eye is here to serve you?")

    else:
        response = random.choice(errors)
        talkvoice(response)
