#!/usr/bin/python3

import unittest 

def add_numbers(x, y):
    return x + y

class TestAdd_numbers(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-2, 5), 3)
        self.assertEqual(add_numbers(0, 0), 0)

if __name__=='__main__':
    unittest.main()