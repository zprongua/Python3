language = 0

def langsupport():
    """
    pick between given languages
    """
    language = int('1. English\n2. Espanol\n3.Deutsch\n')

def name_input():
    """
    takes name from user, prints it to console
    """
    if language == 1:
        name = int(input('What is your name?\n'))
    if language == 2:
        name = int(input('Cual es tu nombre?\n'))
    if language == 3:
        name = int(input('Wie heise?\n'))
    greet(name)


def greet(name):
    """
    this greets someone in chosen language
    """
    if language == 1:
        print('Hello '+str(name))
    if language == 2:
        print('Hola ' + str(name))
    if language == 3:
        print('Guten Tag, ' + str(name))


name_input()
