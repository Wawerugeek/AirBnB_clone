#!/usr/bin/python3
"""This module contains the entry point of the command interpreter:"""
import cmd 
from models import storage
from models.base_model import BaseModel
import json

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'
    c_dict = {'BaseModel': BaseModel}
    
    def do_EOF(self, arg):
        """This indicates the end of file """
        return True

    def do_quit(self, arg):
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
    
    def do_create(self, args):
        """creates a new instance of BaseModel.

        Args:
            args (class name): the class name to create
        """
        if not args:
            print("** class name missing **")
            return 
        
        try:
            cls = eval(args)
        
        except NameError:
            print ("** class doesn't exist ** ")
            return 
        
        objs = cls()
        storage.new(objs)
        storage.save()
        print(objs.id)

    def do_show(self, args):
        """Prints the str rep of an instance based on cls name and ud

        Args:
            args (class name): show [class name] [id]
        """
        my_list = args.split()

        if len(my_list) == 0:
            print("** class name missing **")
            return
        
        if my_list[0] not in HBNBCommand.c_dict.keys():
            print("** class doesn't exist **")
            return
         
        if len(my_list) == 1:
            print("instance id is missing")
            return 
        
        objs_dict = storage.all()
        key = f"{my_list[0]}.{my_list[1]}"
        if key in objs_dict:
            instance_rep = str(objs_dict[key])
            print(instance_rep)
        
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """deletes an instance based on the class name and id

        Args:
            args (_type_): destroy [class name] [id]
        """
        my_list = args.split()

        if len(my_list) == 0:
            print("** class name missing **")
            return
        
        if my_list not in HBNBCommand.c_dict.keys():
            print("** class doesn't exist **")
            return
        
        if len(my_list) == 1:
            print("** instance id missing **")
            return 
        
        storage.reload()
        objs_dict = storage.all()
        key = f"{my_list[0]}.{my_list[1]}"
        if key in objs_dict:
            del objs_dict[key]
            storage.save()
        
        else:
            print("** no instance found **")

    
        
        


if __name__=='__main__':
    HBNBCommand().cmdloop()