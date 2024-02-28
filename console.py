#!/usr/bin/python3
"""Everything about console interpreter"""

import cmd, sys


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Quit cmd"""
        return True

    def do_help(self, arg):
        """documents of commands"""
        super().do_help(arg)

    def do_quit(self, arg):
        """Quit cmd"""
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
