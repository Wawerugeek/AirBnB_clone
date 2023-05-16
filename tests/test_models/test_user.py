#!/usr/bin/python3
"""Test cases for user class"""
import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """test cases for user"""
    obj = User()
    def setUp(self):
        """Set up initial values"""
        self.obj.email = ""
        self.obj.password = ""
        self.obj.first_name = ""
        self.obj.last_name = ""

    def test_subclass(self):
        """Test if class is subclass"""
        self.assertEqual(issubclass(User, BaseModel), True)
        
    def test_type(self):
        """Test type of object"""
        self.assertEqual(type(self.obj.email), str)
        self.assertEqual(type(self.obj.password), str)
        self.assertEqual(type(self.obj.first_name), str)
        self.assertEqual(type(self.obj.last_name), str)

if __name__ == '__main__':
    unittest.main()
