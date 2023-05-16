#!/usr/bin/python3
"""Tests for amenity modules"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage
import os


class TestAmenity(unittest.TestCase):
    """tests methods and attributes for amenity


    Args:
        unittest (_type_):class of unitest module
    """
    def setUp(self):
        """Reset class attrs to their default values"""
        with open("test_file.json", "w"):
            storage.__file_path = "test_file.json"
            storage.__objects = {}
            Amenity.name = ""
            
    def tearDown(self):
        """removes the created file from the file system"""
        storage.__file_path = "file.json"
        try:
            os.remove("file_test.json")
        except FileNotFoundError:
            pass
    
    def test_m_doc(self):
        """module documentation"""
        self.assertTrue(len(Amenity.__doc__) > 0)
    
    def test_c_doc(self):
        """check for class documentation"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_init(self):
        """Test that a new Amenity object is initialized"""
        self.assertTrue(issubclass(Amenity, BaseModel))

        expected_attrs = {
            "name": str
        }
        "#check that the amenity class has the expected attributes"
        for a_name, a_type in expected_attrs.items():
            self.assertTrue(hasattr(Amenity, a_name))
            self.assertIsInstance(getattr(Amenity, a_name), a_type)

if __name__ == '__main__':
    unnitest.main()

