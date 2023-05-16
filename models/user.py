#!/usr/bin/python3
"""This module contains a class user
that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """_summary_

    Args:
        BaseModel (class): the BaseModel_
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
