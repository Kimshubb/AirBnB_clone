#!/usr/bin/python3
''' base model that defines all common attributes and methods for other classes
'''
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
                self.__dict__[key] == datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            else: 
                self.__dict__[key] = value

    def __str__(self):
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
