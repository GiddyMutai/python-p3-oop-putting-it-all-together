#!/usr/bin/env python3

class Shoe:
    
    # initializes the attributes
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = self.cobble()

    # size getter and setter methods
    @property
    def size(self):
        """size property"""
        return self._size
    
    @size.setter
    def size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")

    # method to cobble shoe
    def cobble(self):
        # this method when called sets the instance attribute to new
        self.condition = "New"
        print("Your shoe is as good as new!")
        
        