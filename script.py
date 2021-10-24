

#file = open('/home/user/Documents/GIT/file1.txt')

#content = file.read()

#print(content)

import math

#x = math.pow(2.0, math.sqrt(9.0))
#print(x)

#print('Alex\\nAna!\\\nJoe\nJen')

#print('{:.0f}'.format(1.5555))

#user_num = int(input())

#x = int(input())

#print((user_num // x) , (((user_num // x) // x)) , (((user_num // x) // x ) // x))

#print(help(math))

my_list = ['red','blue','green']

print('\nColor Choices:')

for x in my_list:
    print(x)
    
my_list.append((input('\nPlease enter a new color Add new color \n')))

print('\nNew Color addition')
for x in my_list:
    print(x)

#removal of pop
my_list.pop(2)

print('\nRemoval Valdiation with pop index 2')
for x in my_list:
    print(x)


#List removal with.remove method
my_list.remove('red')

print('\nRemoval Valdiation with remove \"red\"')
for x in my_list:
    print(x)

#List modificaton to list
my_list[0] = 'red'

print('\nAdding new object')
for x in my_list:
    print(x)

my_list.append
