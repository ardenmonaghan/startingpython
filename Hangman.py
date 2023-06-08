#Hangman

from random import choice
import os


def choose_word(list_of_words):
     '''chooses a word from word_list'''

     chosen_word = choice(word_list)
     return chosen_word.lower()

def failed_attempt(attempt,word,tries):
     ''' If the attempt is not part of the word '''

     global playing
     print('\n')
     print('\n')
     print('That letter is not inside the word')
     tries -= 1
     print(f' you have {tries} attempts remaining!')

     return tries

def attempt():
     '''user input of a letter that is an attempt'''

     while True:
          the_attempt = input('Type in a letter to guess: ')

          if len(the_attempt) > 1 or len(the_attempt) == 0:
               print('Sorry, couldnt get that letter!')
               continue
          else:
               if the_attempt in '0123456789':
                    print('Please enter a letter')

               else:
                    return the_attempt.lower()


def success_attempt(remaining,word,letter):
     #a and b are going to be x and y defined below
     global x
     global y #have to call global x and y because doing reassignments, only edits work (mutable objects)

     '''If the letter is in the word'''
     remaining -= word.count(letter)
     print(f'You have {remaining} letters to guess left!')

     for num in range(word.count(letter)):   
          x[y.index(letter)] = letter
          y[y.index(letter)] = 0

     return remaining

     

     

def hangman(tries):
     if tries == 6:
          print('''
     
            ______    
           |      |
           |      O
           |
           | 
          ---
     
          ''')

     elif tries == 5:
           print('''
     
            ______    
           |      |
           |      O
           |      |
           | 
          ---
     
          ''')

     elif tries == 4:
          print('''
     
            ______    
           |      |
           |      O
           |      |
           |      |
          ---
     
          ''')
     
     elif tries == 3:
          print('''
     
            ______    
           |      |
           |      O
           |      |
           |      |
          ---   ./
     
          ''')

     elif tries == 2:
          print('''
     
            ______    
           |      |
           |      O
           |      |
           |      |
          ---   ./ \.
     
          ''')

     elif tries == 1:
          print('''
     
            ______    
           |      |
           |      O
           |    - |
           |      |
          ---   ./ \.
     
          ''')


     elif tries == 0:
          print('''
     
            ______    
           |      |
           |      O
           |    - | -
           |      |
          ---   ./ \.
     
          ''')

     
a = True
while a:
     while True:
          ans = input('Would you like to start the game, yes or no?: ')       
          if ans.lower() not in ['yes','no']:
               print('Please enter a yes or no answer')   
          else:
               if ans.lower() == 'yes':
                    print('lets start')
                    playing = True
                    break
               else:
                    print('Alright')
                    a = False
                    break
     if a == False:
          break
      
     while playing:               

          word_list = ['revolution', 'newspaper', 'soup', 'candidate', 'actor', 'topic', 'media', 'psychology', 'pizza', 'excitement', 'improvement', 'youth', 'debt', 'map', 'owner', 'dad', 'patience', 'consequence', 'alcohol', 'disease', 'protection', 'thanks', 'lady', 'way', 'safety', 'manufacturer', 'chocolate', 'volume', 'setting', 'city', 'library', 'exam', 'perception', 'music', 'expression', 'activity', 'priority', 'independence', 'population', 'solution', 'personality', 'recommendation', 'version', 'discussion', 'church', 'police', 'feedback', 'error', 'people', 'sympathy']
          the_word = choose_word(word_list)
          remaining_letters = len(the_word)
          the_tries = 7
          x = []
          for a in range(len(the_word)):
               x.append('_')
          y = []
          for a in the_word:
               y.append(a)
          print(the_word)
          print('Welcome to hangman!')
          enter = input('Press any key to continue!')

          print('''
     
            ______    
           |      |
           |
           |
           | 
          ---
     
          ''')

          print(f'The length of the word is {len(the_word)}')
          print('\n')
          print('You have 7 misses remaining')


          enter = input('Press any key to continue!')
          
          
               
          print(f'There are {len(x)} letters in the word')

     
          b = True
          while b:

               print(x)
               if '_' not in x:
                    print('Print you win!')
                    playing = False
                    break

               if the_tries == 0:
                    print('You lose')
                    hangman(the_tries)
                    playing = False
                    break

               the_attempt = attempt()
          
               if the_attempt in the_word:
                    
                    if the_attempt in x:
                         print('You already guessed that letter, please put another letter')
                         continue

                    print('\n')
                    print('\n')
                    remaining_letters = success_attempt(remaining_letters,the_word,the_attempt)
                    continue

               else:
                    the_tries = failed_attempt(the_attempt,the_word,the_tries)
                    hangman(the_tries)
                    continue

          
          print(x)
     
     again = input('Would you like to play again Y or N?: ')

     if again == 'Y':
          continue
     else:
          break
