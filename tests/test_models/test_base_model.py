#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test BaseModel"""

    def test_to_dict1(self):
        """test to_dict method"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        obj = my_model.to_dict()

        new_model = BaseModel(**obj)

        self.assertDictEqual(obj, new_model.to_dict())

    def test_to_dict2(self):
        """test to_dict method"""
        model = BaseModel()
        model.name = "My First Model"
        model.my_number = 89
        obj = model.to_dict()

        new_model = BaseModel(**obj)

        self.assertNotEqual(model, new_model)

    def test_to_dict3(self):
        """test to_dict method"""
        obj = {
            '__class__': 'BaseModel',
            'name': 'Test Model',
            'value': 'Model'
        }
        bm = BaseModel(**obj)

        self.assertDictEqual(obj, bm.to_dict())

    def test_str(self):
        """test __str__ method"""
        obj = {
            '__class__': 'BaseModel',
            'id': '1234',
            'name': 'Test Model',
            'value': 'Model',
        }
        bm = BaseModel(**obj)

        self.assertEqual(
            "[BaseModel] (1234) {'__class__': 'BaseModel', 'id': \
'1234', 'name': 'Test Model', 'value': 'Model'}",
            bm.__str__()
        )

    def test_datetime_raise(self):
        """test datetime ValueError"""
        obj = {
            '__class__': 'BaseModel',
            'id': '1234',
            'name': 'Test Model',
            'value': 'Model',
            'created_at': 'asskrr'
        }
        with self.assertRaises(ValueError):
            bm = BaseModel(**obj)