word = None
errorCount = 0
GH = None

def start(w) :
    global word, errorCount, GH
    word = w
    errorCount = 0
    GH = ["_" for i in range(len(w))]

def guessL(L) :
    global word, errorCount, GH
    if L in word :
        for i in range(len(word)) :
            if L == word[i] :
                GH[i] = L
        return True
    else :
        errorCount+=1
        return False

def guessW(W) :
    global word, errorCount, GH
    if W == word :
        return True
    else :
        return False
        errorCount+=1

def finished() :
    x = 0
    global word, errorCount, GH
    for i in range(len(word)) :
        if(GH[i] == "_") :
            x+=1
    if(x == 0) :
        return True
    else :
        return False
