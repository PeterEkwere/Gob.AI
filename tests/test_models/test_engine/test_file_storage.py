#!/usr/bin/python3
"""Unittest for File storage engine"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """test FileStorge object"""

    def test_new(self):
        """test new function"""
        model = BaseModel()
        model.name = "My First Model"
        model.my_number = 89
        storage = FileStorage()
        storage.new(model)
        obj = storage.all()

        self.assertIs(obj[f"BaseModel.{model.id}"], model)