#!/usr/bin/python3
from __future__ import annotations
import os
import json


'''Defines FileStorage class'''
class FileStorage:
    '''serializes instances to JSON and deserializes JSON files to instances
    Attributes - __file_path(str): name of JSON file to save objects to
                __objects(dict): store all objects 
    '''
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        if not os.path.exists(FileStorage.__file_path):
            self.save()

    def all(self, cls=None):
        '''return __objects dict filtered by class'''
        if cls:
            return {key: obj for key, obj in FileStorage.__objects.items() if isinstance (obj, cls)}
        else:
            return FileStorage.__objects

    def new(self, obj):
        '''create new object sets in __objects obj with key <obj_class_name>.id'''
        if not hasattr(obj, 'id'):
            obj.id = str(uuid.uuid4())
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj
        
    def save(self):
        '''Serialize __objects to JSON file __file_path'''
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w+") as file:
            json.dump(objdict, file)

    def reload(self):
        '''Deserialize JSON file __file_path to __objects if it exists'''
        from models.__init__ import storage
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    cls = globals().get(cls_name)
                    if cls:
                        instance_id = value.get("id")
                        inst_key = "{}.{}".format(cls_name, instance_id)
                        if inst_key not in storage.all(cls):
                            instance = cls(**value)
                            storage.new(instance)

        except FileNotFoundError:
             pass
