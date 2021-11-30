#Guess Game
myGuesses = ''
import random
secretNumber = random.randint(1, 20)
print("Hello!, what is your name?")
myName = input()
print("Well, " +myName+ ", guess a number between 1 and 20")
def guess():
    return int(input())
for i in range(1, 6):
    guess()
    if guess == secretNumber:
        print("Good job, "+ myName + "!, you guessed my number in "+ str(len(myGuesses)) + " guesses")
    elif guess < secretNumber:
        print("Your guess is too high")
    elif guess > secretNumber:
        print("Your guess is too low")
    else: 
        print("Nope. The number I was thinking is: " + secretNumber)  
     
