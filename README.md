# Python Bank App

This is a Python Bank App created using Object Oriented Programming in Python, Abstraction using Abstract Classes and Methods, Control Flow and Conditionals, lastly,  Break and Continue keywords.

## Table of contents

- [Overview](#overview)
  - [How to use the project](#how-to-use-the-project)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Useful resources](#useful-resources)
- [Author](#author)

## Overview

### How to use the project

#### Step 1: Setting up Initial Requirements:

1. Python 3.11 and above — Follow [this link](https://www.python.org/downloads/) to download Python for your operating system. You can refer to these tutorials on YouTube for the same — Windows, Mac-OS, Ubuntu (it’ll be somewhat similar for other Linux distributions).

2. pip — pip has been included with the Python installer since versions 3.4 for Python 3 and 2.7.

3. Install pipenv using pip — pip install pipenv

#### Step 2: Setting up Python Virtual Environment using pipenv:

1. Install required dependencies using pipenv — pipenv install
2. Activate Python Virtual Environment — pipenv shell
3. Run the program — python main.py

### Screenshot
![image](https://user-images.githubusercontent.com/108392678/236621176-61e76181-354d-4184-b18b-12bb5116827b.png)


### Links

- Github: [Code](https://github.com/marventures/python-bank-app)

## My process

### Built with

- [Python](https://www.python.org/) - python.org
- [Pipenv](https://pipenv.pypa.io/en/latest/) - Python Virtual Environment.

### What I learned

- Python OOP
- Python Classes and Instances
- Python OOP Inheritance
- Python OOP Abstraction using Abstract Classes and Methods
- Control Flow and Conditionals
- Break and Continue keywords

  Here is a code snippet:

```py
# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod


# Class Bank (Abstract Bank Class)
class Bank(ABC):

    def basicinfo(self):
        print('This is a generic bank')
        return 'Generic bank: 0'

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass


# Class Swiss (A specific type of bank than derives from class Bank)
class Swiss(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.bal = 1_000

    def basicinfo(self):
        print('\n')
        print('This is your current Swiss Bank account')
        return f'Swiss Bank Amount: ${self.bal}'

    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal -= amount
            print(f'Withdrawn amount: ${amount}')
            print(f'New balance: ${self.bal}')
        else:
            print('Insufficient funds! Please try again.')
        return self.bal

    def deposit(self, amount):
        self.bal += amount
        print(f'Deposited amount: ${amount}')
        print(f'New Balance: ${self.bal}')
        return self.bal
```

### Useful resources

- [OOP in Python](https://www.geeksforgeeks.org/python-oops-concepts/) - This helped me understand the concept of OOP in Python.
- [Abstract Classes](https://www.geeksforgeeks.org/abstract-classes-in-python/) - This helped me understand the use abstract methods and classes in Python.
- [Pipenv Setup](https://python.plainenglish.io/setting-up-a-basic-django-project-with-pipenv-7c58fa2ec631) - This helped me setup my python virtual env

## Author

- Website - [Marvin Morales Pacis](https://marvin-morales-pacis.vercel.app/)
- LinkedIn - [@marventures](https://www.linkedin.com/in/marventures/)
- Twitter - [@marventures11](https://www.twitter.com/marventures11)
