import hangmanmodel

print("P1, give a word that would be hard to guess.")
playerword = input()
hangmanmodel.start(playerword)
for i in range(0, 100) :
    print()

# print("If you would like to guess a letter, please specify with (l), but if you would like to guess the word, please specify (w) with the parenthensis.")
while not hangmanmodel.finished() :
    if(hangmanmodel.errorCount == 6) :
        break
        
    for i in range(len(hangmanmodel.word)) :
        print(hangmanmodel.GH[i], end = " ")
    print()
    print("P2, Guess a letter.")
    playerguess = input()
    hangmanmodel.guessL(playerguess)
    print("Current Errors: " + str(hangmanmodel.errorCount))
if(hangmanmodel.errorCount == 6) :
    print("You Lose. The word was: " + hangmanmodel.word)
else :
    print("You got the word correct. It was : " + hangmanmodel.word)