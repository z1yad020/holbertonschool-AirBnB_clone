#!/usr/bin/python3
"""Class Review"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review"""

    place_id = ""
    user_id = ""
    text = ""
