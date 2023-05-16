#!/usr/bin/python3
"""
Unit tests for the Place class
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""
    objs = Place()
    def setUp(self):
        """Resets the Place attributes"""
        self.objs.number_rooms = 0
        self.objs.number_bathrooms = 0
        self.objs.max_guest = 0
        self.objs.price_by_night = 0
        self.objs.latitude = 0.0
        self.objs.city_id = ""
        self.objs.user_id = ""
        self.objs.name = ""
        self.objs.description = ""
        self.objslongitude = 0.0
        self.objs.amenity_ids = []

    def test_m_docstring(self):
        """Tests that the module has a docstring"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_c_docstring(self):
        """Tests that the class has a docstring"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_attribute_types(self):
        """Tests that all attributes of Place have the correct type"""
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, list)

    def test_instance_inheritance(self):
        """Tests that a Place instance is also a BaseModel instance"""
        place = Place()
        self.assertIsInstance(place, BaseModel)

if __name__ == '__main__':
    unittest.main()
