import os
import sys
import json

class Shot(object):
    def __init__(self, path, length, name, seria="none", season="n//a", thumbnail=None):
        self.path = path
        self.name = name
        self.length = length
        self.seria = seria
        self.season = season
        self.thumbnail = thumbnail

    @classmethod
    def store_to_jsn(self):

        #TODO store data to json file
        #code here
        pass


    @classmethod
    def load_from_jsn(self):

        #TODO load data from json file
        # code here 
        
        pass


   