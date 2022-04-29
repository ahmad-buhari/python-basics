'''
LAB 31.1
Given four values representing counts of quarters, dimes, nickels and pennies, output the total amount as dollars and cents.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'Amount: ${dollars:.2f}')

Ex: If the input is:

4
3
2
1

Ex output:
Amount: $ 1.41

----
where 4 is the number of quarters, 3 is the number of dimes, 2 is the number of nickels, and 1 is the number of pennies, the output is:
'''

#Solution

def func_lab_31_1(i,ii,iii,iv):
  a = int(i) * 0.25
  b = int(ii) * 0.10
  c = int(iii) * 0.05
  d = int(iv) * 0.01
  total = a+b+c+d
  return 'Amount: ${:.2f}'.format(total)
  
i = input('\nEnter quater\n')
ii = input('Enter dime\n')
iii = input('Enter nickel\n')
iv = input('Enter pennie\n')
print(func_lab_31_1(i,ii,iii,iv))



  

  