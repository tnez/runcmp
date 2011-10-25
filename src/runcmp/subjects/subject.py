'''
Created on Oct 3, 2011

@author: tnesland
'''

import os.path as op

class Subject(object):
    '''
    classdocs
    '''

    def __init__(self, ID=None, directory=None, time_point=None):
        '''
        Constructor
        Params:
        - (optional) ID: subject ID as string
        - (optional) directory: subject directory
        - (optional) time_point: time_point directory
        '''
        self.ID = ID
        self.directory = directory
        self.time_point = None
        
    def is_valid(self):
        '''
        Does the subject have valid ID and directory structure?
        '''
        return self.ID and self.can_find_rawdata()
    
    def can_find_rawdata(self):
        '''
        Can we find the expected RAWDATA directory given our existing parameters?
        '''
        return op.isdir(op.join(self.working_dir(),'RAWDATA'))
    
    def working_dir(self):
        '''
        Return the working dir, either subject/ or subject/tp/
        '''
        # if we have a time point value
        if(self.time_point):
            return op.join(self.directory, self.time_point)
        # else return 
        return self.directory
        
        
