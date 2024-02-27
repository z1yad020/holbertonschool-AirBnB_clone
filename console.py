#!/usr/bin/python3
"""Console - entry point of the project"""


import cmd
from models.base_model import BaseModel

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
    def emptyline(self):
        """Does nothing if empty line"""
        pass

    def do_create(self, arg):
        """Creates a class instance and prints id"""
        args = arg.split()
        class_name = args[0]
        if not args:
            print("** class name missing **")
        elif class_name is not "BaseModel":
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)




if __name__ == '__main__':
    HBNBCommand().cmdloop()
