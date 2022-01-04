print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    elif int(numCats) <= 0:
        print('You don\'t have any cats I see.')
    elif int(numCats) < 0:
        print('I take it you don\'t like cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a valid number.')
