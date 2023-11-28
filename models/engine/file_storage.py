#!/usr/bin/python3
import json

'''Defines FileStorage class'''
class FileStorage:
    '''serializes instances to JSON and deserializes JSON files to instances
    Attributes - __file_path(str): name of JSON file to save objects to
                __objects(dict): store all objects 
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''return __objects dict'''
        return FileStorage.__objects

    def new(self, obj):
        '''create new object sets in __objects obj with key <obj_class_name>.id'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        setattr(FileStorage, key, obj)
        
    def save(self):
        '''Serialize __objects to JSON file __file_path'''
        with open(FileStorage.__file_path, "w") as file:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, file)

    def reload(self):
        '''Deserialize JSON file __file_path to __objects if it exists'''
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o)
        except FileNotFoundError:
             return
