import random
randomWords = ["ducks" , "jumbo" , "lucky" , "pills" , "flour"]
secret = random.choice (randomWords)
letter = ""
updateWord = []
print secret #only for tester
def initialize():
    print "We have a secret word"
    print "_ _ _ _ _"
def getLetter():
    print "Enter a letter"
    global letter
    letter = raw_input()
def ifWon():
    if secret == updateWord:
        print "you win"
    else:
        getLetter()

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
def main():
    initialize ()
    getLetter ()
    ifWon ()
main()