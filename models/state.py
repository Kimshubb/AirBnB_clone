#!/usr/bin/python3
from models.base_model import BaseModel
"""Class sTATE init"""
class State(BaseModel):
    """State class"""
    name = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
