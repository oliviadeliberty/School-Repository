
def loops():
    word = raw_input("word")
    letters = len(word)
    for letters in word:
        print word


def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x
        return runningtotal
    print runningtotal

loops()
square(2)