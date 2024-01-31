#HANGMAN-GAME

import random
from words import words


def valid_word():

    word = random.choice(words).upper() #randomly chooses something from the list

#verify that the hidden word doesn't contain underscores or spaces
#if it has underscores or spaces the loop selects a new word
    while '_' in word or ' ' in word or '-' in word:
        word = random.choice(words).upper()
        
    return word
    

def HANGMAN():
    print('\n~WELCOME TO THE HANGMAN GAME~')
    print('\nA word was chosen, try to guess!!\n')

    word = valid_word()
    lives = 8
    # set for not repeat a letter
    letters_tried = set()

    try:

        #list comprehension #check if the letters of word are in letters_ried if not continue with an underscore
        word_hidden = ''.join([letter if letter in letters_tried else '_' for letter in word])

    #as long as there is still an underscore in the hidden word or the lives have not yet gone to 0
     #will continue looping
        while( '_' in word_hidden and lives > 0): 
        
            print(f'You have: {lives} lives\n')
            print(word_hidden, '\n')

            #letter typed by the user
            user_trys = input('type a letter: ').upper().strip()

            if not user_trys:
                print('error, blank space...\n')
            #if what the user typed is part of the alphabet and is only one character
            elif user_trys.isalpha() and len(user_trys) == 1:

            # If the user's input letter is in letters tried, it means that it had already been typed
                if user_trys in letters_tried:
                    print('\nLetters you have tried: ')
                    for k in letters_tried:
                        print(k, end=' ')
                    
                    print(f'\n\nYOU HAVE ALREADY TRIED THE LETTER {user_trys}, please try a different one.')
                    continue
            
                #add to letters_tried
                letters_tried.add(user_trys)
           
                print('-----------------------------')
                print('\nLetters you have tried: ')
                for i in letters_tried:
                    print(i, end=' ') 

                if user_trys in word:
                    word_hidden = ''.join([letter if letter in letters_tried else '_' for letter in word ])
                    print()
                    nice = ['Good guessed! ^^','Awesome! ^^','nice guessed!^^', 'Keep going! ^^', 'perfect!^^','well done!^^']
                    random_nice = random.choice(nice)
                    print('\n',random_nice, '\n')
                else:    
                    lives -= 1 #takes away a life if wrong
                    print()
                    print('\nIncorrect guessed... you lose a life! :(')
            else:
                print('\nsorry, only letters from the alphabet...\n')
    
        if lives == 0:
            print(f'''Game over... 
you lost! the word was: {word}\n''')
        else:
            print(F'{word}')
            print(f'\nCongrats! You have gussed the word "{word}"\n')
 
    except KeyboardInterrupt:
        print('\n\nGame interrumpted buy user...\n')
    except:
        print('\nError!\n')

HANGMAN()
print("Thank's for playing HANGMAN WITH OUR COMPUTER!^^\n")

