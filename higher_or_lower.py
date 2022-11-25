from random import randrange

rando = randrange(10)
guess = 11

while guess != rando:
    guess = int(input('Guess a number between 0 and 10\n'))
    if guess < rando:
        print('Too low')
    if guess > rando:
        print('Too high')

print('You did it!')
