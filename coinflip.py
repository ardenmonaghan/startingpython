##COIN FLIP

from logging import exception
from random import randint

def coin_flipper(user_input):
    for turns in range(0,user_input):
        flipped = randint(1,2)

        if flipped == 1:
            print('heads')
        else:
            print('tails')


def inputter():
    while True:
        try:
            ammount = int(input('How many times would you like to flip coin?: '))
            if ammount > 10000:
                raise exception
            return ammount
        except:
            print('Please enter a valid value!')
            continue


coin_flipper(inputter())
#Hello