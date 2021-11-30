print('How many cats do you have')
numCats = int(input())
try:    
    if numCats < 0:
        print("you cannot have less than zero cats")
        
    elif numCats >= 4:
        print("You have a lot of cats")
    else:
        print("That's not a lot of cats")    
except: ValueError