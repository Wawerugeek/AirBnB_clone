#!/usr/bin/python3
"""This Base Model defines all common attributes/methods for other classes
used for the entire project.The class called "BaseModel" is the representation
of an object/instance."""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """This class defines all attributes/methods for other classes.
    """
    today = datetime.now()

    def __init__(self, *args, **kwargs):
        """ Initialize the BaseModel instance attributes

        ARGS: *args
        **kwargs: key : value // attribute name : attribute value
        """
        if kwargs:
            d_format = "%Y-%m-%dT%H:%M:%S.%f"
            kw_dict = kwargs.copy()
            del kw_dict['__class__']
            '#__class__ should not be added as attribute so del'
            '#iterate through the dict to change key to datetime obj'
            for key in kw_dict:
                if (key == "created_at" or key == "updated_at"):
                    kw_dict[key] = datetime.strptime(kw_dict[key], d_format)
            self.__dict__ = kw_dict
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.today
            self.updated_at = self.today
            storage.new(self)
            '#if a new instance we call new() on storage'

    def __str__(self):
        """the string representation of how class will print"""
        return (f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """this public instance method updates the public instance varaiable
        (updated_at) with the current date"""
        self.updated_at = self.today
        storage.save()

    def to_dict(self):
        """this method will generate a dictionary representation of an instance
        """
        # create a copy before modification.
        m_dict = dict(self.__dict__)
        
        m_dict["__class__"] = self.__class__.__name__
        m_dict["created_at"] = self.created_at.isoformat()
        m_dict["updated_at"] = self.updated_at.isoformat()
        
        return m_dict
