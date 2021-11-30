#Guess Game
import random
print("Hello!, what is your name?")
name = input()
def playGame():
    print("Well, " +name+ ", guess a number between 1 and 20")
    secretNumber = random.randint(1, 20)
    for numberOfGuesses in range(6):
        myGuess = int(input())
        if myGuess < secretNumber:
            print("Your guess is too low")
        elif myGuess > secretNumber:
            print("Your guess is too high")
        else:
            break
    if myGuess == secretNumber:
        print("Good job, "+ name + "!, you guessed my secret number in "+ str(numberOfGuesses) + " guesses")
    else:
        print("Nope. The number I was thinking of is: " + str(secretNumber))    
playGame()
print("Do You Want to Play Again?")
def playerChoice():
    myChoice = input("Enter yes or no: " )
    if  myChoice.lower() == "yes":
        playGame()
    
    elif myChoice.lower() == "no":
        print("game over")
    else: 
        breakpoint
    return ("Error")   
playerChoice()
if playerChoice() == "Error":
    playerChoice()
else:
    breakpoint

