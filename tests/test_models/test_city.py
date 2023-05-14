#!/usr/bin/python3
"""Test module for city class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """tests for methods and behaviour of city class"""
    def setUp(self) -> None:
        return super().setUp()
    
    def test_m_doc(self):
        """module documentation"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_c_doc(self):
        """test class documentation"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_Isnstance(self):
        """Is class instance of basemodel"""
        from models.base_model import BaseModel
        city = City()
        self.assertIsInstance(city, BaseModel)