spam = 42 # global variable

def eggs():
    spam = 43 # local variable
    print('I have ' + str(spam) + ' berries')

def berries():
    print('I have ' + str(spam) + ' berries')

berries()  #used global variable  
eggs() #used local variable

print(str(eggs.spam))
