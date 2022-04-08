# My Journey with Python
![GitHub last commit](https://img.shields.io/github/last-commit/ahmad-buhari/python-basics)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ahmad-buhari/python-basics)

Throughout my career and personal education in information technology, I have taken about three beginner python courses. I took those classes because it was the coolest language at the moment, and I thought I had a decent understanding. Boy, was I wrong.... when I went through the fourth python course as part of my degree program to my shock, it was one of the most challenging courses I've taken. Since I didn't remember any of the material from the previous classes,  I had to start all over again. It truly shined a light on the importance of applying the skills you learn and keep practicing your trade. This page is dedicated to my never-ending journey with python.

## Status

```mermaid
      gantt
      dateFormat YYYY-MM-DD
      title Writing Schedule
      
      Section Timeline
      README.md             :done,      de1, 2022-04-06, 2022-04-07
      Tansfer lesson notes          :active,    des2, 2022-04-07, 5d
      Transfer code from Replit     : active, des3, 2022-04-12, 5d
```



## Tips for real-world application

1. Remember when writing code to follow the best practices outlined in [PEP20 - Zen of Python](https://peps.python.org/pep-0020/)

2. Check any incoming input strings and prep to remove empty spaces with `strip()` remember we're human and sometime folks added an extra space at the end by accident. 

3. Use `join` to save time for concanting (combining) a list of str values. No need to loop and concat the str togther.
  
      ```python
      #Example
      color_list = ['red','blue']
      print('$'.join(color_list))
      ```   


4. Using the `help()` function to print all properties of a given class or method.

      ```python
      #Example: 
      #Print help for the str method on the python console
      help(str)
      
      ```


5. To see check builtin-in modules loaded check.

      Loop through `__builtins__.__dict__` and review modules for additional info/
      ```python
      #Example
      for x in __builtins__.__dict__:
            print(x)
      ```
      or with comprehension
      ```python
      #Example
      [print(x) for x in __builtins__.__dict__]
      ```
6. Try to pratice using python comprhension to simplify code.  

7. `assert` is useful for evaluting code. 


## Basic Knowledege
- When creating a variable, it must start as a **letter** or an **underscore**
- Python treats characters differently depending on the class, i.e. '1' is not 1
- When in doubt reference [Python documenation](https://docs.python.org/)

## Manipluating the string = str 
Any string / str can be modified, there are many tools at your disposal to convert the character to whatever endstate.

### String Splicing
Essentially selecting a character by picking it's positional place in the word. Remember positional value starts from 0 and empty value (i.e. blank space) counts.
```python
#Example
word = 'Hello World!'
print(word[0])
print(word[1])
print(word[11])
```

### String Splicing II
You can also iterate over strings with a verbose method `[a:b:c]`
- a is the starting position
- b is the ending position
- c is the frequency

Note: 
- When using this method positional value start at 1.
- Default starting value is 0, and  frequency value is 1, `[0::1]`
- To print in reverse order use the frequency value at -1, `[::-1]`

```python
#Example
word = 'Hello World!'
print(word[1:5:])
print(word[::2])
print(word[::-1])

```

## Exceptions
Are used to handled data that does not mesh with your code. Example, you want a user to enter a data in string format, you can use the Exception class dervived from the BaseException to throw and error.


