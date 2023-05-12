#!/usr/bin/python3 
"""this module is used to store our first object"""
import json

class FileStorage():
    """this class serializes instances to a JSON file
    and deserializes JSON file to instances (python)
    
    it has two class atrributes and and four methods
    """
    def __init__(self):
        """class initialization
        """
        self.__file_path = "file.json" 
        self.__objects = {}
    
    def all(self):
        """this returns the dictionary __object"""
        return FileStorage.__objects
    
    def new(self, obj):
        """_sets in __objects to obj with key <obj class name>.id

        Args:
            obj (__object): sets in object with description (path:__file.path)
        """
        


    def save(self):
        """serializes objects to json file"""
    
    def reload(self):
        """deserializes json file to python objects"""
