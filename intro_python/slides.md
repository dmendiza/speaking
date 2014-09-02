# Alamo City Python Group Intro&nbsp;to&nbsp;Python

---

# About Me

Douglas Mendizabal

* GitHub - [https://github.com/dmend](https://github.com/dmend)

![Rackspace](http://i.imgur.com/p76BF6u.jpg)

* Project Meniscus - [http://projectmeniscus.org/](http://projectmeniscus.org)

![DenimGroup](http://i.imgur.com/S0snBzk.gif)

---

# What is Python? 

* Open Source Programming Language
    * created by Guido van Rossum
* Object Oriented
* Interpreted
* Dynamically Typed
    * Duck typed

![Duck-typed!](http://i.imgur.com/ylHoaIi.gif)

---

# What is Python? ...

* Portable
	+ Linux, Mac OS X, Windows*
* Multiple Implementations
    + CPython
    + Jython
    + IronPython
    + PyPy
* Interactive

		!python
		>>> import this

---

# Where to get it?

If you have a *nix OS you may already have it

     $ python -V
     Python 2.7.3

You can download from [http://python.org/](http://python.org/)

# 2 or 3?

Python 3 is not backwards compatible with Python 2 :(

---

# Syntax

*   No curly braces
*   Code blocks are determined by white space (indentation)
*   No semicolon to end lines
*   Parentheses are mostly optional
*   Variables do not need to be declared and can hold any type

    	!python
    	>>> foo = 'bar' # no need to declare foo before assignment
	    >>> foo
		'bar'
		>>> foo = 1 # assign int to same variable
		>>> foo
		1

*	[PEP-8](http://www.python.org/dev/peps/pep-0008/) - Do it in style!

---

# Types

## Booleans

*   True
*   False
*   bool()

##  Numbers
*   int
*   float
*   decimal.Decimal
*   complex(x, y)

---

# Data Structures

## list
Think arrays, but they are mutable, resizable, and can hold any type
    
    !python
    [1, 2, 'string', "b", 'c']

## str
Unlike lists, strings are immutable, so string operations return new strings

Raw strings 

    !python
    r"Raw string won't escape \n new line and other special chars."

Unicode strings 

	!python
	u'You are using unicode right? ಠ_ಠ'

---

# Data Structures

## tuple
Read only lists.  They are immutable

	!python
	(1, 2, 'a', 'b')
	("only-one",) # one element tuples require a comma

## sets

	!python
	{1, 2, 3}

## dictionaries

    !python
    >>> mydict = {'key1': 'value1', 
                  'key2': 'value2'}
	>>> mydict['key1']
	'value1'
	>>> mydict.get('key2')
	'value2'

---

# Functions

Functions are first class objects
	
	!python
	def foo(x):
	    return x * 2
	>>> foo
	<function foo at 0x10d4b8d70>
	>>> foo(3)
	6

Anonymous functions

	!python
	lambda x: x * 2

Don't use mutable types as default arguments!

	!python
	def foo(bar=[]):  # Don't do this!
	    bar.append('foo')
	    return bar

---

# Objects

	!python
	class AddressBook(object):
	    def __init__(self, name, phone):
	        self.name = name
	        self.phone = phone
	    def foo(self):
	        print self.name

	>>> john = AddressBook('John Doe', '210-555-0000')

---

# Exception Handling
	
	!python
	try:
	    some_function()
	except Exception:
	    print 'Error'
	else:
	    do_stuff()
	finally:
	    always_do_this_stuff()


	raise ValueError('Error foo(): error description here')

---

# List Comprehensions

Don't do this:

	!python
	result = []
	for x in range(10):
	    if x % 3 == 0:
	        result.append(x)
Do this:

	!python
	result = [x for x in range(10) if x % 3 == 0]

---

# Tuple unpacking

Don't do this:

	!python
    temp = a
	a = b
	b = temp

Do this:

	!python
	a, b = b, a

---

# Packages
	
	mypackage/
		__init__.py
		my_module.py
		submodule/
			__init__.py
			util.py

	>>> import mypackage
	>>> from mypackage.my_module import *

---

# Package Management

## PyPI - [https://pypi.python.org/pypi](https://pypi.python.org/pypi)

## setuptools

	$ python setup.py install

	$ easy_install mypackage

## distribute

	$ pip install mypackage

---

# Virtual Environments
Package management for mutiple projects

	pip install virtualenvwrapper

---

# Pythonbrew
Manage multiple python versions

[https://github.com/utahta/pythonbrew](https://github.com/utahta/pythonbrew)

---

# Testing

![DosXX Testing](http://i.imgur.com/y7Hm9.jpg)

*	unittest
*	mock
*	nosetests
*	Tox

---

# Windows Tools
## Compilers

* [Visual C++ 2008 Express](https://www.dreamspark.com/Product/Product.aspx?productid=34) - for Python 2.7
* [Visual C++ 2010 Express](http://www.microsoft.com/visualstudio/eng/products/visual-studio-express-products) - for Python 3.3

## Python Tools for Visual Studio

* [Visual Studio 2012 Shell](http://www.microsoft.com/visualstudio/eng/products/visual-studio-express-products)
* [Python Tools for Visual Studio](http://pytools.codeplex.com/)

---

# Questions?
