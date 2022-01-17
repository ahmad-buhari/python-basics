

#Example 1 - Function Read File 
def file_source(source_readonly):
    a = open(source_readonly)
    content = a.read()
    return content
'''Help Guide:
1. def file_source -- is the function
2. (source_readonly) -- is the variable to hold the data value, typically passthrough from the input()
3. a --  is the variable to initilize file opening with open
4. open(source_readonly) --  is used to open the file from the source_readon;y var
5. content -- is the var to hold the a.read method data  
6. a.read() -- is calling the .read method to readthrough contnet with the a var
7. return -- must return value
'''


file_location = input('\nEnter File Location to read\n')
print('Content of file:',file_source(file_location))



#Enter Data
user_input = input('Enter text to append:\n')
user_input2 = '\n'+user_input+' '

#Example 2 - Write file using mode a to append str change
file_source2 = open('log.txt','a')
#contents = file_source.read()
file_source2.write(user_input2)
file_source2.close()

#Example 3 - Write file while open
file_source3 = open('log.txt','a+')
contents = file_source3.read()
print(contents)
file_source3.write(user_input2)
print(contents)
file_source3.close()