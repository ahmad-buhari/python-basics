#playground tuotrial

#importing the sys and time module
import sys
import time

# function to write out str by wpm speed.
def slow(x):
    for char in x:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(1./11)




exit_key = ['q','quit', ' ']

welcome_msg = 'Welcome to the python playground, with live console returns'


while True:
    try:
        slow(welcome_msg)
        user_input = (input('''\nSelect the following exercise to see live response
        \n1. Running the help() command
        \n2. Exploring the method of a class
        \n3. Slow print\nType \'q\' or \'quite\' to exit the window\n''')) 
        if user_input == 'q':
            slow('Exiting Window')
            break

        elif user_input == '1':
            print('help(str)')
            slow('In this example we\'ll run the help command in the python console. Press Ctrl + C to exit the help menu')
            print(help(str))
            slow('Enter new selection')
            break


        
        elif user_input =='3':
            slow('hello world, bye world3')

        slow('Enter Selection:\n')
        user_input = input()
    except ValueError:
        slow('Exiting Window')
        