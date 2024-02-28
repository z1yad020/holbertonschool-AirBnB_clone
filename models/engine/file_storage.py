#!/usr/bin/python3

"""
File stroging to file
"""
import json
from models.base_model import BaseModel

class FileStorage:
    """
    File store and retrive
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return all dic objects"""
        return FileStorage.__objects

    def new(self, obj):
        """save new `obj` to dic"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes `__objects` to the JSON file"""
        dic = {k : v.to_dict() for k, v in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dic, f)

    def reload(self):
        """deserialze from `__file_path` to `__objects`"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            for v in data.values():
                self.new(eval(v["__class__"])(**v))

        except FileNotFoundError:
            pass
