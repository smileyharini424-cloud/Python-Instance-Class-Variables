# Python Instance and Class Variables

## Explanation

Python classes can contain two important types of variables:

* **Instance variables** belong to individual objects and can have different values for each object.
* **Class variables** belong to the class and are shared by all objects of that class.

This program demonstrates both types.

## Problem Statement

Write a Python program to create a `Student` class with instance variables for student name and age, and a class variable for the college name.

## Features

* Demonstrates instance variables
* Demonstrates class variables
* Creates multiple objects
* Shows shared class data
* Shows object-specific data

## How It Works

1. A `Student` class is created.
2. `college` is defined as a class variable.
3. `name` and `age` are created as instance variables inside `__init__()`.
4. Multiple student objects are created.
5. Each object has its own name and age.
6. All objects share the same college value.

## Technologies Used

* Python 3
* Object-Oriented Programming
* Classes
* Objects
* Instance Variables
* Class Variables

## Program Flow

Start → Define Class Variable → Define Instance Variables → Create Objects → Display Object Data → Display Shared Data → End

## Sample Input

```text id="8f4y2c"
No user input required.
```

## Sample Output

```text id="w1m7qa"
Student 1:
Name: Harini
Age: 20
College: ABC College

Student 2:
Name: Anu
Age: 21
College: ABC College
```

## Key Learning

* Instance variables belong to individual objects.
* Class variables are shared by objects of the class.
* Instance variables are usually defined using `self`.
* Class variables are defined directly inside the class.
* Changing a class variable can affect the value shared by objects.

## File Location

```text id="5d9r2v"
Python-Instance-Class-Variables/instance_class_variables.py
```

## Repository Structure

```text id="p6k3xm"
Python-Instance-Class-Variables/
│
├── instance_class_variables.py
└── README.md
```

## Author

V.Harini
