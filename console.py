#!/usr/bin/python3
"""This module contains the entry point of the command interpreter:"""
import cmd
import shlex
import models
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """the class for cmd"""

    prompt = '(hbnb) '
    c_dict = {
        'BaseModel': BaseModel,
        "Amenity": Amenity,
        "Place": Place,
        "City": City,
        "User": User,
        "State": State,
        "Review": Review
        }

    @staticmethod
    def get_list(c_name):
        """help to retrieve the list objects of a given class"""
        objs = storage.all()
        obj_list = []

        for k, v in objs.items():
            obj_name = k.split('.')[0]
            if obj_name == c_name:
                obj_list.append(str(v))

        return obj_list

    def do_EOF(self, arg):
        """This indicates the end of file """
        print()
        return True

    def do_quit(self, arg):
        """_summary_

        Args:
            arg (string): for the user

        Returns:
            TRue: to exit the program
        """
        return True

    def do_create(self, args):
        """creates a new instance of BaseModel.

        Args:
            args (class name): the class name to create
        """
        my_list = shlex.split(args)

        if len(my_list) == 0:
            print("** class name missing **")
            return

        '#check whether the class name is valid'
        if my_list[0] not in HBNBCommand.c_dict:
            print("** class doesn't exist **")
            return

        '#create new instance of a given class'
        command = HBNBCommand.c_dict[my_list[0]]
        n_instance = command()

        print(n_instance.id)
        storage.save()

    def do_show(self, args):
        """Prints the str rep of an instance based on cls name and ud

        Args:
            args (class name): show [class name] [id]
        """
        my_list = shlex.split(args)

        if len(my_list) == 0:
            print("** class name missing **")
            return

        if my_list[0] not in HBNBCommand.c_dict:
            print("** class doesn't exist **")
            return

        if len(my_list) == 1:
            print("instance id is missing")
            return

        objs_dict = storage.all()
        key1 = f"{my_list[0]}.{my_list[1]}"

        objects = objs_dict.get(key1)
        if objects is None:
            print("** no instance found **")
            return
        print(objects)

    def do_destroy(self, args):
        """deletes an instance based on the class name and id

        Args:
            args (_type_): destroy [class name] [id]
        """
        my_list = shlex.split(args)

        if len(my_list) == 0:
            print("** class name missing **")
            return

        if my_list[0] not in HBNBCommand.c_dict:
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
        '#reload file from storag'
        storage.reload()

        '#get all objects from storage'
        arg_list = shlex.split(args)
        objs_dict = storage.all()
        str_list = []
        if len(arg_list) == 0:
            for obj in objs_dict.values():
                str_list.append(str(obj))
            print(str_list)
            return
        if arg_list[0] not in HBNBCommand.c_dict:
            print("** class doesn't exist **")
            return
        str_list = HBNBCommand.get_list(arg_list[0])
        print(str_list)

    def do_update(self, args):
        """updates an instance based on the class name and id
        by adding or updating attribute

        Args:
            args (_type_): update <class name> <id> <attribute name>
            "<attribute value>"
        """
        my_list = shlex.split(args)
        if len(my_list) == 0:
            print("** class name missing **")
            return

        '#ensure that the classname is valid'
        if my_list[0] not in HBNBCommand.c_dict:
            print("** class doesn't exist **")
            return
        if len(my_list) == 1:
            print("** instance id is missing **")
            return

        key = f"{my_list[0]}.{my_list[1]}"
        objs_dict = storage.all()
        obj = objs_dict.get(key)
        obj_class = HBNBCommand.c_dict[my_list[0]]
        if obj is None:
            print("** no instance found **")
            return
        if len(my_list) == 2:
            print("** attribute name missing **")
            return

        if len(my_list) == 3:
            print("** value missing **")
            return

        attr_name = my_list[2]
        attr_value = my_list[3]

        if hasattr(obj, attr_name):
            attr_value = type(getattr(obj, attr_name))(attr_value)
            setattr(obj, attr_name, attr_value)
            storage.save()

        else:
            setattr(obj, attr_name, attr_value)
            storage.save()

    def do_count(self, args):
        """counts / retrievethe instances of a class
        count <class> or <class>.count"""
        objs = models.storage.all()
        name = args.split('.')[0] if '.' in args else args
        cont = [objs for objs in objs.values() if type(objs).__name__ == name]
        print(len(cont))

    def emptyline(self):
        """empty line should do nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
