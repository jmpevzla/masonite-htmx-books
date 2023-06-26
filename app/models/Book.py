""" Book Model """

from masoniteorm.models import Model


class Book(Model):
    """Book Model"""

    __fillable__ = ['title', 'author', 'price', 'description']
