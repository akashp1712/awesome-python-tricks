# [Awesome Python Tricks](https://akashp1712.github.io/python-tricks/) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
* Awesome python tips and tricks, you can't ignore. Everyday.

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
```
