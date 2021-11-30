#Guess Game
import random
print("Hello!, what is your name?")
name = input()
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
    print("Nope. The number I was thinking is: " + str(secretNumber))    
