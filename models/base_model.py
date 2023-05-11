#!/usr/bin/python3
"""This Base Model defines all common attributes/methods for other classes used for the entire project. 
    The class called "model" is the representation of an object/instance.  
    """
import uuid
from datetime import datetime

class Basemodel():
    """This class defines all attributes/methods for other classes.
    """
    today = datetime.now()

    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4)
        self.created_at = self.today
        self.updated_at = self.today

    def __str__(self):
        """the string representation of how class will print"""
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
        """this public instance method updates the public instance varaiable
        (updated_at) with the current date"""
        self.updated_at = self.today
    
    def to_dict(self):
        """this method will return a dictionary containing all 
        keys/values of __dict__ instances"""
        r_dict = self.__dict__.copy()
        r_dict["__class__"] = self.__class__.__name__
        r_dict["created_at"] = self.created_at.isoformat()
        r_dict["updated_at"] = self.updated_at.isoformat()
        return r_dict
