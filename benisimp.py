import random

x = random.randint(1, 101)
y = 1

while True :

    print ("Pick a number between 1 and 100.")

    q = int (input())

    if(q > x) :
        print("Guess Lower")
        y+=1
    elif(q < x) :
        print("Guess Higher")
        y+=1
    elif(q == x) :
        print("It took you " + str(y) + " tries to guess the number.")
        break
