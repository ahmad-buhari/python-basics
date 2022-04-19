#loading os module to access system files
import os 
import sys
import time

path = './' #specifiying working file diretory
repl_files = os.listdir(path) #calling os method to list directory (listdir)


# function to write out str by wpm speed.
def slow(x):
    for char in x:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(1./11)


exit_key = ['q','quit', ' ']

welcome_msg = 'Welcome to the python playground, with live console returns'
slow(welcome_msg)



while True:
    try:
        user_input = (input('''\nSelect the following exercise to see live response
        \n1. Running the help() command
        \n2. Exploring the method of a class
        \n3. Display execrise files
        \n4. Slow print example
        \nType \'q\' or \'quit\' to exit the window\n''')) 
      
        if user_input == 'q':
            slow('\nExiting Window, bye bye')
            break

        elif user_input == '1':
            print('help(str)')
            slow('In this example we\'ll run the help command in the python console. Press Ctrl + C to exit the help menu')
            print(help(str))
            slow('Enter new selection')
            break


        elif user_input == '3':
          [print(files) for files in repl_files if files[0] == 'l' ]
          
        
        elif user_input =='4':
            slow('hello world, bye world')

        slow('\n**restarting**\n')
        
    except ValueError:
        slow('\nExiting Window, bye bye')