#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
import models


class TestBaseModel(unittest.TestCase):

    def test_save_method(self):
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()

        self.assertIn("__class__", instance_dict)
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)

    def test_id_attribute(self):
        instance = BaseModel()
        self.assertIsNotNone(instance.id)

    def test_created_at_attribute(self):
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_str_method(self):
        instance = BaseModel()
        string_representation = str(instance)
        self.assertIn("BaseModel", string_representation)
        self.assertIn(instance.id, string_representation)

if __name__ == '__main__':
    unittest.main()

