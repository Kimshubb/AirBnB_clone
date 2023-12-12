#!/usr/bin/python3
''' base model that defines all common attributes and methods for other classes
'''
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
class BaseModel:
    """Base model class"""
    storage = FileStorage()

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            self.storage.new(self)

    def __str__(self):
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, getattr(self, id, None),self.__dict__)

    def save(self):
        from models.__init__ import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        model_dict = {}
        for key, value in self.__dict__.items():
            if not callable(value):
                model_dict[key] = value
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = type(self).__name__

        if isinstance(model_dict['created_at'], datetime):
            model_dict['created_at'] = model_dict['created_at'].isoformat()

        if isinstance(model_dict['updated_at'], datetime):
            model_dict['updated_at'] = model_dict['updated_at'].isoformat()

        return model_dict
