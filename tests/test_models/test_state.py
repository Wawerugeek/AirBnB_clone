#!/usr/bin/python3
"""Unit tests for state class"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """review the implementation of state class"""
    
    def setUp(self):
        """Set up test instance attributes"""
        self.state = State()

    def test_c_doc(self):
        """Check if the class has documentation"""
        self.assertTrue(len(State.__doc__) > 0)
    
    def test_m_doc(self):
        """Check if the module has documentation"""
        self.assertTrue(len(State.__doc__) > 0)

    def test_inheritance(self):
        """Test if State class inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))
        
    def test_attributes(self):
        """Test the attributes of State class"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(type(self.state.name), str)
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        

if __name__ == "__main__":
    unittest.main()