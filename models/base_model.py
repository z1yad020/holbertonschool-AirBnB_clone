#!/usr/bin/python3

"""
Base of EVERYTHING
"""

#import uuid
from datetime import datetime


class BaseModel():
    """
    Base of classes
    """

    def __init__(self):
        """
        constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        saving updated time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        to dictionary
        """
        sdic = self.__dict__.copy()
        sdic["__class__"] = self.__class__.__name__
        sdic["created_at"] = self.created_at.isoformat()
        sdic["updated_at"] = self.updated_at.isoformat()
        return sdic
