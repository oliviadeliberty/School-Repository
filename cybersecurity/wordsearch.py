def wsSolve():
    #get wordsearch and legend
    wordsearch = raw_input("the wordsearch: ")
    legend = raw_input("legend: ")

    #clean up strings and code
    word = legend.split(" ")
    wordsearch = wordsearch.replace(" ","")
    letters = len(wordsearch)

    #create the format of the wordsearch
    wsLines = []
    wsLines.append(wordsearch[0:4])
    wsLines.append(wordsearch[5:9])
    wsLines.append(wordsearch[10:14])
    wsLines.append(wordsearch[15:19])
    wsLines.append(wordsearch[20:24])

    #looking for the letters of the key
    wordcheck = 0
    for a in word:
        return word[wordcheck]

        wordcheck = wordcheck + 1
    #show progress
    print("There are ", letters, " letters in this wordsearch.")
    print(wordsearch)
    print(word)
    print(wsLines)

wsSolve()

# f u n l o r e o o v e c o v e s a n e r h n a s a