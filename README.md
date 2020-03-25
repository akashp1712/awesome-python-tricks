# [Awesome Python Tricks](https://akashp1712.github.io/python-tricks/) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
* Awesome python tips and tricks, you can't ignore.

    [View a random trick](https://akashp1712.github.io/python-tricks/random){: .btn .btn-green }

----

- ### Boolean Confusion 1 - empty list
An empty list ie, bool([]) returns False.<br/>Usually, an empty list has a different meaning than None.

```python
list1 = []
bool(list1) # prints False
list2 = [10, 20, 30]
bool(list2) # prints True

#None means no value while an empty list means zero values.
#Semantically, they are different.
```
- ### Print the file name from the path
Just print the file name with extension from the any path

```python
print (os.path.basename("/path/to/file.txt"))
# file.txt
```
- ### Asserts that never fail
Assertion never fails when the first argument is a tupple. It Always evaluates as true

```python
assert("python" == "java", 'Assert Failed')
# This will always be true and will never fail.
# Following is the right way of doing it" 
assert "python" == "java", 'Assert Failed'
```
- ### Underscores explained
Underscores in Python and what do they mean

```python
_var # Preferred convention for internal variables and methods
var_ # Used to avoid naming conflicts with Python keywords
__var # Used for [name mangling](https://dbader.org/blog/meaning-of-underscores-in-python) by Python when used in class context
    # Python interpreter changes the name of the variable to avoid collision with child class
__var__ # Reserved for special use in the language
 - # Used as a temporary or don't care varaibles
```
- ### The Zen of Python, by Tim Peters
Open your python console and hit **`import this`**

```python
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
- ### Print the Object Attributes
Use the built-in **`dir()`** funciton to print attribute of an object.

```python
lst = list()
print(dir(lst))
# ['__add__', '__class__', '__contains__', '__delattr__', ..., 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

number = 123
print(dir(number))
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', ..., 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

str = "This is a String"
print(dir(str))
# ['__add__', '__class__', '__contains__', '__delattr__', ..., 'title', 'translate', 'upper', 'zfill']
```
- ### Disassembler for Python bytecode
Disassembler helps understanding the object by converting it to a human-readable representation of the bytecodes for analysis.

```python
def my_name():
...     return "Akash"
...

>>> dis.dis(my_name)
  2           0 LOAD_CONST               1 ('Akash')
 
3 RETURN_VALUE 


>>> def my_name():
...     print("Akash")
...
>>> dis.dis(my_name)
  2           0 LOAD_CONST               1 ('Akash')
              3 PRINT_ITEM
              4 PRINT_NEWLINE
              5 LOAD_CONST               0 (None)
              8 RETURN_VALUE
```
- ### Implement map (built-in pytohn function)
`map` is a higher-order function.<br/>It takes a function object and an iterable And calls the fucntion on each element in the iterable, yielding the results as it goes along

```python
def map2(func, iter):
    for val in iter:
        yield func(val)

# The above method can be used as bellow similar to `map` function
lst = list(map2(str.upper, ['Save Earth', 'Save Animals', 'Save water']))
print(lst)
#['SAVE EARTH', 'SAVE ANIMALS', 'SAVE WATER']
```
- ### Read csv data to Dictionary
Read csv data with headers and convert to Dictionary where each column header is key.

```python
import csv

with open( <path-to-file>, 'r' ) as theFile:
    reader = csv.DictReader(theFile)
    for line in reader:
        # line is { 'house_name': 'Houstan', 'price': 7.334, 'age': 5, ... }
        print (line)
```
- ### Iterate through a pair of lists
Use zip() to iterate through a pair of lists

```python
namelist = ["Avish", "Piyush", "Tom"]
agelist = [17, 22, 38]

for name, age in zip(namelist, agelist):
    print(name, age)

```
