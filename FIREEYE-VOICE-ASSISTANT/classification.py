def classify(command):
    set1 = open("./CLASSIFICATION/CSRF.txt", "r")  #index = 0
    set2 = open("./CLASSIFICATION/nmap.txt", "r")  #index = 1
    #set3 = open("./CLASSIFICATION/shutdown.txt", "r")

    for line in set1:
        #print(line)
        line = line.lower()
        csrf_words = line.split()
    #print(csrf_words)
    for line in set2:
        #print(line)
        line = line.lower()
        nmap_words = line.split()
    #print(nmap_words)

    temp_str = command
    #print(temp_str)
    score = []
    count =  0
    for i in range(0, len(csrf_words)):
        if(csrf_words[i] in temp_str):
            count = count+1
    score.append(count)
    count = 0
    for i in range(0, len(nmap_words)):
        if(nmap_words[i] in temp_str):
            count = count + 1
    score.append(count)
    #print(score)
    index = score.index(max(score))
    print(index)

command = input("Enter the command: ")
classify(command)



