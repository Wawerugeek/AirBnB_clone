#!/usr/bin/python3
"""This module contains the entry point of the command interpreter:"""
import cmd 
import shlex
from models import storage
from models.base_model import BaseModel
import json
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    """the class for cmd"""

    prompt = '(hbnb)'
    c_dict = {
        'BaseModel': BaseModel,
        "Amenity" : Amenity,
        "Place" : Place,
        "City" : City,
        "User" : Review,
        "State" : State,
        "Review" : User
              }
    
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
            #if class name is missing, say its missing
            print("** class name missing **")
            return 
        #split the arguments into a list 
        my_list = shlex.split(args)

        #check whether the class name is valid
        if my_list[0] not in HBNBCommand.c_dict.keys():
            print("** class doesn't exist **")
            return
        #create new instance
        n_instance = HBNBCommand.c_dict[my_list[0]]()
        #save new instance to Json file
        n_instance.save()
        print(n_instance.id)

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
        key1 = f"{my_list[0]}.{my_list[1]}"
        
        try:
            value = objs_dict[key1]
            print(value)
        
        except KeyError:
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

    def do_all(self, args):
        """prints all string rep of all instances based or
        not on the class name

        Args:
            args (_type_): _description_
        """
        #reload file from storage
        storage.reload()

        #get all objects from storage
        objs_dict = storage.all()

        #print all objects if no class name is provided
        if not args:
            print("** class name missing **")
            return
        
        my_list = args.split()
        all_list = []

        if my_list[0] not in HBNBCommand.c_dict:
            print("** class doesn't exist **")

        else:
            #check whether class exists
            for key, value in objs_dict.items():
                obj_name = value.__class__.__name__
                if obj_name == my_list[0]:
                    all_list += [value.__str__()]
                print (all_list)

    def do_update(self, args):
        """updates an instance based on the class name and id
        by adding or updating attribute

        Args:
            args (_type_): update <class name> <id> <attribute name>
            "<attribute value>"
        """
        if not args:
            print("** class name missing **")
            return 
        my_list = args.split()

        #ensure that the classname is valid
        if my_list[0] not in HBNBCommand.c_dict.keys():
            print("** class doesn't exist **")
            return 
        
        #check whether instance id is provided
        elif len(my_list) == 1:
            print("** instance id is missing **")
            return 
        
        #retrieve an instance from storage 
        else:
            objs_dict = storage.all()
            key = f"{my_list[0]}.{my_list[1]}"

            for key, value in objs_dict.items():
                object_name = value(type(self).__name__)
                object_id = value.id

                if object_name == my_list[0] and object_id == my_list[1].strip('"'):
                    if len(my_list) == 2:
                        print("** attribute name missing **")

                    elif len(my_list) == 3:
                        print("** value missing **")
                    
                    else:
                        setattr(value, my_list[2], my_list[3])
                        storage.save()
                        return 
            print ("** no instances found **")
         
if __name__=='__main__':
    HBNBCommand().cmdloop()
