# This is a number guessing game
import random


print('Hey, what is your naaaaame?!')
name = input()

print('Hi, ' + name + ', I am thinking of a number between 1 and 30 mate.')
print('You only have 6 guesses')
secretNumber = random.randint(1, 30)


for guessCount in range(1,7):
    guess = int(input())
    
    if guess < secretNumber:
       print('To low ' + name)
    elif guess > secretNumber:
       print('To high ' + name)
    else:
       break #guessed number

if guess == secretNumber:
    print('Good guessing ' + name + '. You got the number in ' + str(guessCount) + ' attempts!')
else:
    print('Nice try, ' + name + ', the number was ' + str(secretNumber))
          
