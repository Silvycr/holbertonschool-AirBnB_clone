#!/usr/bin/python3
from models.base_model import BaseModel

"""This is a class with a public
class attributes"""


class User(BaseModel):
    """User class"""
    email = str()
    password = str()
    first_name = str()
    last_name = str()
