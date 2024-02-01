#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    pass
    def __init___(self):
        self._name = None
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if(type(name) in (str)) and (1 < len(name) < 25):
            self._name = name
        else:
            print("Name nust be string between 1 and 25 characters")

    name = property(get_name, set_name)

fido = Dog()