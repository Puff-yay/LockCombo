def LockCombo():
    pin = input("What is your 4 digit password? ")
    numerics = "0123456789"
    for item in pin:
        if (item not in numerics) or (len(pin) != 4):
            return
    return pin

def PinCracker():
    combo = LockCombo()
    if combo == None:
        return
    characters = "0123456789"
    guess = ""
    for a in range(len(characters)):
        for b in range(len(characters)):
            for c in range(len(characters)):
                for d in range(len(characters)):
                    guess = str(characters[a]) + str(characters[b]) + str(characters[c]) + str(characters[d])
                    print(guess)
                    if guess == combo:
                        print("My guess is " + guess)
                        return
                    
PinCracker()
