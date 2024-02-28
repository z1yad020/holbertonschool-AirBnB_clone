#!/usr/bin/python3
"""Console - entry point of the project"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand"""

    prompt = "(hbnb) "
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
    }

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
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instance = self.classes[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """String representation of an instance"""

        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance of the class"""

        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = f"{args[0]}.{args[1]}"
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()

    def do_all(self, arg):
        """ Print string representation of all instances"""

        args = arg.split()
        objects = storage.all()
        if len(args) == 0:
            for obj in objects.values():
                print(obj)
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    print(obj)

    def do_update(self, arg):
        """Updates an instance"""

        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = objects[key]
                a_name = args[2]
                a_type = type(getattr(obj, a_name, ""))
                a_value = a_type(args[3].strip('"'))
                setattr(obj, a_name, a_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
