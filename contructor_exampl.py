import unittest
from unittest import TestCase

class Person:
    def __init__(self, name):
        if not name:
            raise Exception("Name is required")
        self.name = name

class PersonTest(TestCase):
    def test_that_a_person_requires_a_name(self):
        self.assertRaises(Exception, Person, "")

if __name__ == '__main__':
    unittest.main()    
