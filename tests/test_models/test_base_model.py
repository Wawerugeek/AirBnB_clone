#!/usr/bin/python3
"""Tests for Basemodel class"""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """set up class"""
        FileStorage.__file_path = "file_test.json"
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        """remove"""
        try:
            os.remove("file_test.json")
        except FileNotFoundError:
            pass

    def test_id(self):
        """test the id type"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)

    def test_m_docstring(self):
        """test the module docstring"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_class_docstring(self):
        """test the class docstring"""
        for method in dir(BaseModel):
            self.assertTrue(len(method.__doc__) > 0)

    def test_str_output(self):
        """check the output of the string"""
        my_model = BaseModel()
        expected_output = f"[{my_model.__class__.__name__}] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_output)
    

    def test_datetime_type(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)


    def test_id_uniqueness(self):
        my_first_model = BaseModel()
        my_second_model = BaseModel()
        self.assertNotEqual(my_first_model.id, my_second_model.id)


    def test_to_dict(self):
        """tests for to_dict method"""
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        self.assertIsInstance(my_dict, dict)
        for key, value in my_dict.items():
            if key == "created_at" or key == "updated_at":
                self.assertIsInstance(value, str)
            else:
                self.assertEqual(value, getattr(my_model, key))

    def test_is_instance(self):
        """tests to check whether its an instance of Basemidel"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)


    def test_save(self):
        """tests for the save nethod"""
        my_model = BaseModel()
        previous_updated_at = my_model.updated_at
        my_model.save()
        current_updated_at = my_model.updated_at
        self.assertLess(previous_updated_at, current_updated_at)

    def test_file_permissions(self):
        """check whether the files are executable"""
        self.assertTrue(os.access('models/base_model.py', os.R_OK))
        self.assertTrue(os.access('models/base_model.py', os.W_OK))
        self.assertTrue(os.access('models/base_model.py', os.X_OK))

if __name__ == '__main__':
    unittest.main()
