#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
import models
from unittest.mock import patch


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

class TestBaseModelInit(unittest.TestCase):

    def test_init_default_values(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertIsInstance(obj.id, str)
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.updated_at, datetime)

    def test_init_with_arguments(self):
        obj_id = "test_id"
        created_at = "2022-01-01T00:00:00.000000"
        updated_at = "2022-01-02T00:00:00.000000"
        obj = BaseModel(id=obj_id, created_at=created_at, updated_at=updated_at)

        self.assertEqual(obj.id, obj_id)
        self.assertEqual(obj.created_at, datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(obj.updated_at, datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%S.%f"))

    @patch('models.storage.new')
    def test_init_calls_storage_new(self, mock_new):
        obj = BaseModel()
        mock_new.assert_called_with(obj)


class TestBaseModelSave(unittest.TestCase):

    @patch('models.storage.save')
    def test_save_updates_updated_at_and_calls_storage_save(self, mock_save):
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()

        self.assertNotEqual(obj.updated_at, original_updated_at)
        mock_save.assert_called_once()


if __name__ == '__main__':
    unittest.main()
