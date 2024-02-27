#!/usr/bin/python3
"""FileStorage class"""


import json
from models.base_model import BaseModel


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
                loaded = json.load(file)
                for o in loaded.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return