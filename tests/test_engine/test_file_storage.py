#!/usr/bin/python3

import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import json

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Run this method before each test to set up a clean state
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "test_file.json"

    def tearDown(self):
        # Run this method after each test to clean up
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all_method_returns_dictionary(self):
        file_storage = FileStorage()
        result = file_storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method_adds_object_to_objects(self):
        file_storage = FileStorage()
        obj = BaseModel()
        file_storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, file_storage._FileStorage__objects)

    def test_save_method_serializes_to_file(self):
        file_storage = FileStorage()
        obj = BaseModel()
        file_storage.new(obj)
        file_storage.save()

        # Read the contents of the file to verify serialization
        with open(file_storage._FileStorage__file_path, 'r') as file:
            content = file.read()
            self.assertIn(obj.id, content)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

if __name__ == '__main__':
    unittest.main()

