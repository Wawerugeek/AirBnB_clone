#!/urs/bin/python3

"""Unittest module to test the module for storage"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Testing all methods for fileStorage class

    Args:
        unittest (_type_): property of unitetts_
    """
    def setUp(self):
        """File saving"""
        with open ("file_test.json", "w"):
            FileStorage.__file_path = "file_test.json"
            FileStorage.__objects = {}

    def tearDown(self):
        """Remove the created file"""
        FileStorage.__file_path = "file.json"
        try:
            os.remove("file_test.json")
        except FileNotFoundError:
            pass
    
    def test_all(self):
        """THis test the all method of class"""
        self.assertIs(self.fs.all(), FileStorage.__objects)

    def test_save(self):
        """The test for the save method of FileStorage"""
        F_path = FileStorage.__file_path

        if os.path.exists(F_path):
            try:
                os.remove(F_path)
            except Exception:
                raise Exception("error: could not remove {}".format(F_path))
        
        self.fs.save()
        self.assertTrue(os.path.exists(F_path))

    def test_m_doc(self):
        """test wheher the module has documentation"""
        self.assertTrue(len(FileStorage.__doc__) > 0)
    
    def test_c_doc(self):
        """test whther the class has documentation"""
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_instance(self):
        """verify storage"""
        from models import storage
        self.assertEqual(storage, FileStorage)

    

