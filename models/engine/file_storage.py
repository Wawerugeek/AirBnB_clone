#!/usr/bin/python3
"""this module is used to store our first object"""
import json
import os.path


class FileStorage():
    """this class serializes instances to a JSON file
    and deserializes JSON file to instances (python)
    it has two class attributes and four methods
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """this returns the dictionary __object"""
        return (FileStorage.__objects)

    def new(self, obj):
        """_sets in __objects to obj with key <obj class name>.id

        Args:
            obj (__object): sets in object with description (path:__file.path)
        """
        c_name = obj.__class__.__name__
        id = obj.id
        i_key = c_name + "." + id
        FileStorage.__objects[i_key] = obj

    def save(self):
        """serializes objects to json file"""
        obj_dict = {}

        for key in FileStorage.__objects:
            obj_dict[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, "w", encoding='utf-8') as f_path:
            json.dump(obj_dict, f_path)

    def reload(self):
        """deserializes json file to __objects
        only if json file.json exits, otherwise
        do nothing"""
        '#check if the file exists if yes deserialize'
        from models.user import User
        from models.base_model import BaseModel
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        from models.place import Place

        R_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "Review": Review,
            "Amenity": Amenity,
            "Place": Place

        }

        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding='utf-8') as file:
            objects = json.load(file)
            FileStorage.__objects = {}
            for k in objects:
                c_name = k.split(".")[0]
                FileStorage.__objects[k] = R_dict[c_name](**objects[k])
