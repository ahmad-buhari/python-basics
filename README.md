# Zybook Introduction to Python

Check out each lab.py file to see my take on answering the questions. Then you can simply copy and past the code to main.py and run it there.


## Tips

1. Check any incoming input strings for trailing spaces with `rstrip()`


2. Use `join` to save time for concanting (combining) a list of str values. No need to loop and concat the str togther.

  Example:

  `colour_list = ['red','blue']`
  
  `print('$'.join(color_list))`
  
  `>red$blue` 


3. Using the `help()` function to print all properties of a given class.

      Try typing `help(str)`


4. To see check builtin-in modules loaded check.

 Loop through `__builtins__.__dict__` and review modules for additional info/


 Example:

 `for x in __builtins__.__dict__:`
 
----`print(x)` # remeber to indent this line, markup is not friendly with empty spaces

or with comprehension

`[print(x) for x in __builtins__.__dict__]`

5. Try to pratice using python comprhension to simplify code.
  

6. `assert` is useful for evaluting code. 


## Exception
Are used to throw defined errors. Cause you know users are human so mistakes happens. Child proof it by explicitn allowing certain inputs.