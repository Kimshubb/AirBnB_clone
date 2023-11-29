#!/usr/bin/python 3
from models.engine.file_storage import FileStorage
'''create unique FileStorage instance for the application'''
storage = FileStorage()
'''call the reload method on storage variable'''
storage.reload()
