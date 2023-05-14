#!/usr/bin/python3
"""Unittests for Review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Class to test the Review class"""
    def setUp(self):
        """Sets up the objects for the tests"""
        self.review = Review()

    def tearDown(self):
        """Tears down the objects used for the tests"""
        del self.review

    def test_inheritance(self):
        """Tests if Review class is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """Tests the attributes of Review"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_save(self):
        """Tests the save method of Review"""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)
