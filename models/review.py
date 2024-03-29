#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from os import getenv


class Review(BaseModel, Base):
    """Representation of Review """
    __tablename__ = 'reviews'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024),
                      nullable=False)
        place_id = Column(String(60),
                          ForeignKey('places.id'),
                          nullable=False)
        user_id = Column(String(60),
                         ForeignKey('users.id'),
                         nullable=False)
    else:
        text = ""
        place_id = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
