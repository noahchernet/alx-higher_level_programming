#!/usr/bin/python3

"""Module base
Contains class Base
"""
import json


class Base:
    """
    The base for all other classes in this project
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)
    """

    __nb_objects = 0  # Count the number of objects created from this class

    def __init__(self, id=None):
        """Class initializes here
        If id is None, it is set to __nb_objects after it's incremented

        __id_passed (bool): used to check if the arg id was passed, useful
        in modifying __nb_objects
        """
        if id is not None:
            self.id = id
            self.__id_passed = True
        else:
            #  __nb_objects is incremented only when id is None
            Base.__nb_objects += 1
            self.id = self.__nb_objects
            self.__id_passed = False

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of the list of dictionaries
        passed"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the list of objects to a file with cls' class name (
        clsName.json) in JSON format"""

        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
                return
            for i in range(len(list_objs)):
                if i == 0:
                    f.write("[")
                if i + 1 != len(list_objs):
                    eol = ", "
                else:
                    eol = "]"
                f.write(Base.to_json_string(list_objs[i].to_dictionary()) +
                        eol)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of objects stored in json_string. Deserializes
        json_string"""
        if json_string is None or json_string == [] or json_string == "":
            return []
        return json.loads(json_string)

    def __del__(self):
        """Deletes this object
        __nb_objects is decreased by 1 only if the object had id initialized
        to None"""
        if (not self.__id_passed) and Base.__nb_objects > 0:
            Base.__nb_objects -= 1
        del self
