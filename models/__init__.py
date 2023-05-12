#!/usr/bin/python3
"""Create a unique FileStorage instance of our application"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()