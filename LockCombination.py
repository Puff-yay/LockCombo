def LockCombo():
    pin = input("What is your 4 digit password? ")
    if len(pin) == 4 and pin.isdigit():
        return pin
    else:
        print("That is not a valid 4 digit pin.")

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


