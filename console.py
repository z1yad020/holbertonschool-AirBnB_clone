#!/usr/bin/python3
"""Console - entry point of the project"""


import cmd

class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand"""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True
    def empty_line(self):
        """Does nothing if empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()