# Object-oriented programming (OOP)

- Python is an **object-oriented programming language**.
- Everything in python is an **object**.
  
## What is an object

- An **object is a collection or a bundle of data(variables) and methods(functions)** that act on those data.
- An **object is also called an instance of a class** and the process of creating an object is called instantiation.

```python
name = "Nimoh"
print(type(name))
```
- Here `name` is an object of type `str`.

## What is a class

- A class is a template or a construtor used to create objects.
- A class provides a means of bundling data and functionality together.

```python
name_1 = str("Nimoh") # instanciate an object called name that stores "Nimoh"
name_2 = str("Olum")

print(name_1.lower())
print(name_1.upper())
print()
print(name_2.lower())
print(name_2.upper())
```
- `name_1` and `name_2` are objects(instances of a class `str`). Other classes available in python `int`, `float`, `bool`, `list`, `dict`,`set`,`tuple` etc
- `lower()` and `upper()` are methods that are used to manipulate the data in a particular object of class `str`.
  



