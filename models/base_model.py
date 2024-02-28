#!/usr/bin/python3

"""
Base of EVERYTHING
"""

import uuid, models
from datetime import datetime as dt


class BaseModel():
    """
    Base of classes
    """

    def __init__(self, *args, **kwargs):
        """
        constructor
        """
        if kwargs:
            for k, v in kwargs.items():
                if k in ("created_at", "updated_at"):
                    self.__dict__[k] = dt.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k != "__class__":
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        saving updated time
        """
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """
        to dictionary
        """
        sdic = self.__dict__.copy()
        sdic["__class__"] = self.__class__.__name__
        sdic["created_at"] = self.created_at.isoformat()
        sdic["updated_at"] = self.updated_at.isoformat()
        return sdic
