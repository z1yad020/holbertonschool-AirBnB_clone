#!/usr/bin/python3
"""FileStorage class"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes and deserializes to/from JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        obj_class = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file """

        serialized = {}
        for key, value in FileStorage.__objects.items():
            serialized[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized, file)

    def reload(self):
        """deserializes the JSON file to __objects"""

        try:
            with open(FileStorage.__file_path) as file:
                deserialized = json.load(file)
                for obj_values in deserialized.values():
                    class_name = obj_values["__class__"]
                    del obj_values["__class__"]
                    # if isinstance(class_name, str)
                    # and type(eval(class_name)) == type:
                    self.new(eval(class_name)(**obj_values))
        except FileNotFoundError:
            return
