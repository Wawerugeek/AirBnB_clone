#!/usr/bin/python3
"""This module contains the entry point of the command interpreter:"""
import cmd 

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'
    
    def do_EOF(self):
        """This indicates the end of file """
        return True

    def do_quit(self):
        """_summary_

        Args:
            arg (string): for the user

        Returns:
            TRue: to exit the program
        """
        return True
    
    def emptyline(self):
        """empty line should do nothing"""
        pass
    
if __name__=='__main__':
    HBNBCommand().cmdloop()