def classify(command):
    # weather=['what is the Weather?','how is it outside?','Whats the climate?','can i go outside?']
    # greet=['how are you?','how about you?','how are you doing?','hi there',]
    inputtext = command
    print("Question: " + inputtext)
    set1 = open("weather.txt", "r")
    set2 = open("csrf.txt", "r")
    set3 = open("sqli.txt", "r")
    set4 = open("portscan.txt", "r")
    set5 = open("dos.txt", "r")
    for line in set1:
        print(line)
        line = line.lower()
        words1 = line.split()
    # print(words1)
    for line in set2:
        # print(line)
        line = line.lower()
        words2 = line.split()
    # print(words2)
    for line in set3:
        # print(line)
        line = line.lower()
        words3 = line.split()
    # print(words3)
    for line in set4:
        # print(line)
        line = line.lower()
        words4 = line.split()
    for line in set5:
        # print(line)
        line = line.lower()
        words5 = line.split()
    # print(words5)
    # punctuation=[',','"',"?"]
    temp_str = inputtext
    # print(temp_str)
    score = []
    count = 0
    for i in range(0, len(words1)):
        if (words1[i] in temp_str):
            count = count + 1
    score.append(count)
    count = 0
    for i in range(0, len(words2)):
        if (words2[i] in temp_str):
            count = count + 1
    score.append(count)
    count = 0
    for i in range(0, len(words3)):
        if (words3[i] in temp_str):
            count = count + 1
    score.append(count)
    count = 0
    for i in range(0, len(words4)):
        if (words4[i] in temp_str):
            count = count + 1
    score.append(count)
    count = 0
    for i in range(0, len(words5)):
        if (words5[i] in temp_str):
            count = count + 1
    score.append(count)
    print(score)
    biased = 0
    count1 = 0
    for i in range(0, len(score)):
        if (max(score) == score[i]):
            count1 = count1 + 1
    maxoccur = count1
    print("max_occurence:" + str(maxoccur))
    if (maxoccur > 1):
        biased = 1
    pointer = score.index(max(score))
    # print(pointer)
    Assessments = ["WEATHER", "CSRF", "SQLINJECTION", "PORTSCAN", "DENIAL OF SERVICE"]
    print(Assessments)
    if (biased == 1):
        print("CANNOT PREDICT ANYTHING")
    else:
        print("Predicted as: " + str(Assessments[pointer]))


cmd = input("ENTER COMMAND:")

classify(cmd)
