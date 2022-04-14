#playground tuotrial


import sys
import time

def slow(x):
    for char in x:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(1./11)




exit_key = ['q','quit']

print(slow('Welcome to the python playground'))
while True:
    try:
        user_input = (input('''\nSelect the following exercise to see live response
        \n1. Running the help() command
        \n2. Exploring the method of a class
        \n3. Slow print\nType \'q\' or \'quite\' to exit the window\n''')) 
        if user_input == 'q':
            slow('Exiting Window')
            break

        elif user_input == '1':
            print('help(str)')
        
        elif user_input =='3':
            slow('hello world, bye world3')

    
    except ValueError:
        slow('Exiting Window')
        