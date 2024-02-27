#!/usr/bin/python3
"""BaseModel class"""


import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """The BaseModel of the project"""

    def __init__(self, *args, **kwargs):
        """Initializing attributes"""

        self.id = str(uuid4())
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Updating with current datetime"""

        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """Returns string representation"""

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """Returns dictionary representation"""

        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
