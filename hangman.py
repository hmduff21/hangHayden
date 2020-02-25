updatedWord = [] 
def test():
    global secret
    life = 6
    guess = raw_input('Guess a letter: ')
    updatedWord = []
    if guess in secret:
        updatedWord += 
        print(updatedWord)
        
        
    if updatedWord == secret:
        ifWon()
    if life == 0:
        print('You lost buckwheat \n Get em next time' )
    else:
        life - 1
        getLetter()
