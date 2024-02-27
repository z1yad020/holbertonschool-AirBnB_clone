#!/usr/bin/python3

import json 
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        obj_class = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class, obj.id)] = obj

    def save(self):
        serialized = {}
        for key, value in FileStorage.__objects.items():
            serialized[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized, file)
    
    def reload(self):
        try:
            with open(FileStorage.__file_path) as file:
                loaded = json.load(file)
                for o in loaded.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
