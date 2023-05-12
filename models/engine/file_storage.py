#!/usr/bin/python3 
"""this module is used to store our first object"""
import json
import os

class FileStorage():
    """this class serializes instances to a JSON file
    and deserializes JSON file to instances (python)
    
    it has two class atrributes and and four methods
    """

    __file_path = "file.json" 
    __objects = {}
    
    def all(self):
        """this returns the dictionary __object"""
        return FileStorage.__objects
    
    def new(self, obj):
        """_sets in __objects to obj with key <obj class name>.id

        Args:
            obj (__object): sets in object with description (path:__file.path)
        """
        c_name = obj.__class__.__name__
        o_id = obj.id
        i_key = f"{c_name}.{o_id}" #generate instance key from obj.id and class name
        FileStorage.__objects[i_key] = obj

    def save(self):
        """serializes objects to json file"""
        obj_dict = {}

        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict() #function from BaseModel

        with open(self.__file_path, "w") as f_path:
            json.dump(obj_dict, f_path)

    
    def reload(self):
        """deserializes json file to __objects
        only if json file.json exits, otherwise
        do nothing"""
        #check if the file exists
        reload_dict = {}
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                object_dict = json.load(file)
                FileStorage.__objects = {}

                for key in object_dict:
                    class_name = key.split(".")[0]
                    FileStorage.__objects[key] = reload_dict[class_name](**object_dict[key])
        else:
            return 
        

