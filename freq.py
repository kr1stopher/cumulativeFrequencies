# Kristopher Swartzbaugh
# CWID 890939184
# CPSC 535


CF = {} #dictionary of keywords and their cumulative frequencies
CFfinal = {} #final cumulative frequencies for output, combining similar words
syn =[] #array storing all synonyms

#go through synonyms input file, convert into array, holding all synonyms grouped together, and make sure the first eleement in each set is the first alphabetically
def parseSyn(line):
    first = True #if true, quotation found is start of new word, if false the quotation is the end of the word
    char = 0
    #parse through the input line, adding new keywords to the list
    while (char<len(line)):
        if (line[char]=='"'): #keywords can be found within quotation marks
            beginWord = char
            char +=1
            while (line[char]!='"'):
                char = char+1
            endWord = char
            if (first == True):
                firstWord = line[beginWord+1:endWord]
                first = False
            else:
                first = True
                secondWord = line[beginWord+1:endWord]
                syn.append([firstWord,secondWord])
        char=char+1

    #update syn to account for multiple synonyms, grouping all together   ex: ("long", "big"),("big","large") -> ("big", 'large", "long")
    i = 0
    while (i<len(syn)-1):
        j=0
        while (j<len(syn[i])):
            n=1
            while (i+n<len(syn)):
                if (i+n<len(syn) and syn[i][j]==syn[i+n][0]):
                    isDuplicate = False #must check to see if its a duplicate per ex 3
                    for items in syn[i]:
                        if items == syn[i+n][1]:
                            isDuplicate=True
                    if isDuplicate == False:
                        syn[i].append(syn[i+n][1])
                    syn.pop(i+n)
                if (i+n<len(syn) and syn[i][j]==syn[i+n][1]):
                    isDuplicate = False #must check to see if its a duplicate per ex 3
                    for items in syn[i]:
                        if items == syn[i+n][0]:
                            isDuplicate=True
                    if isDuplicate == False:
                        syn[i].append(syn[i+n][0])
                    syn.pop(i+n)

                n=n+1
            j=j+1

        #make sure i has the alphabetical character first
        k = 1
        while (k<len(syn[i])):
            if syn[i][0]>syn[i][k]:
                holder = syn[i][0]
                syn[i][0] = syn[i][k]
                syn[i][k] = holder
            k=k+1

        i=i+1
    #print(syn)
    #print('above is syn')

#parse through the frequencies of the input file (odd lines), add to the CF dictinoary
def parseFreq(line):
    char = 0 # location of the current character in the line
    #parse through input line, seperating words and cumulative frequencies and adding to the CF dictionary
    while (char<len(line)):
        if (line[char]=='"'):
            char +=1 #location of the current character
            beginWord = char #begining of the key word
            while (char<len(line) and line[char]!='"'): #find ending of the keyword
                char = char+1
            endWord = char
            firstWord = line[beginWord:endWord]
            char = char+3 #move to start of frequency integer
            startInt = char
            while (char<len(line) and line[char]!=')'): #find end of integer, could be multiple digits
                char = char+1
            endInt = char
            CF[firstWord] = line[startInt:endInt].strip() #add keyword and frequency to CF
        char=char+1
    #print(CF)
    #print('above is CF')

#seperate input file into valid dictionaries
def cumFreq():
    #read input file
    lines = []
    with open('input2.txt') as input:
            lines = input.readlines()
    count = 1
    for line in lines:
        if count%2 == 1:
        #if count == 1:
            parseFreq(line)
            #parse syn
        if count%2==0:
        #if count == 2:
            parseSyn(line)

            #combine the cumulative frequency of the synonyms into one list
            for items in syn:
                sum = 0
                for itemz in items:
                    sum = sum + int(CF[itemz])
                CFfinal[items[0]] = sum
            print(CFfinal, "of size ", len(CFfinal))
            print('The above is CFfinal')
            CFfinal.clear()
            CF.clear()
            syn.clear()
        count = count + 1



#call the main program
cumFreq()
