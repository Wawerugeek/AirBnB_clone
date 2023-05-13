#!/usr/bin/python3
"""class review that inherits BaseModel"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Has two attributes"""
    place_id = ""
    user_id = ""
    text = ""