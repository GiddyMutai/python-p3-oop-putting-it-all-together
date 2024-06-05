#!/usr/bin/env python3

class Book:
    # initialize the attributes
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    # methods to set the page_count property
    @property
    def page_count(self):
        """Page count property"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    # method to turn the page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    

    
        