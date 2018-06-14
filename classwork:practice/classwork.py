
def shrink(word):
    for i in range(len(word)+1):
        print (word[i:len(word)])
word2 = raw_input("insert a word: ")
shrink(word2)