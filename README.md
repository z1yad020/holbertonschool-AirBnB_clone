# The AirBnB Clone Project

## AirBnB Clone Console
Welcome to the AirBnB Clone Console! This is the first step towards building the AirBnB clone project, a full web application that mimics some functionalities of the popular accommodation rental platform, Airbnb.

## Overview
The AirBnB Clone Console is a Python-based command-line interface that allows you to manage AirBnB objects, such as users, states, cities, places, and more. With this console, you can perform various operations on these objects, including creating, retrieving, updating, and deleting them.

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the following actions can be performed:
-   Creating new objects (ex: a new User or a new Place)
-   Retrieving an object from a file, a database etc…
-   Performing operations on objects (count, compute stats, etc…)
-   Updating attributes of an object
-   Destroying an object

## Usage:

The console provides a set of commands to interact with the AirBnB objects. Here are some of the available commands:

-   `help`: Display a list of documented commands and their descriptions.
-   `quit`: Exit the console.
-   `create`: Create a new instance of a specified AirBnB object.
-   `show`: Display information about a specific AirBnB object.
-   `all`: Display information about all AirBnB objects or a specific type.
-   `update`: Update the attributes of a specific AirBnB object.
-   `destroy`: Delete a specific AirBnB object.   

## Examples:

### Interactive Mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-Interactive Mode

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Running Tests

To ensure the proper functionality of the console, run the unit tests using the following command:

`python3 -m unittest discover tests` 

## Learning Objectives:

-   Understand how to create a Python package.
-   Build a command interpreter in Python using the `cmd` module.
-   Implement Unit testing in a large project.
-   Serialize and deserialize a class.
-   Read and write JSON files.
-   Handle datetime objects.
-   Use UUIDs for unique identifiers.
-   Utilize `*args` and `**kwargs` for handling variable arguments.

  
## Authors:

- Aydan Jafarli
- Ziyad Ibrahimov

