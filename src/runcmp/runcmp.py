'''
Created on Oct 3, 2011

@author: tnesland
'''

import sys
import getopt
import os
import os.path as op
import cmp
from cmp.gui import CMPGUI
from subjects import subject

cmpgui = CMPGUI()
    
def main(argv):
    '''
    Run the connectome mapper using the given arguments
    '''
    # initalize all of all command line args to none
    b_values = None
    project_dir = None
    pickle_file = None
    subject_id = None
    vector_file = None
    working_dir = None
    # parse the command line arguments
    try:
        opts, args = getopt.getopt(argv, "b:d:hm:p:s:v:w:", ["b-values", "help", "project-dir",
                                                             "pickle-file", "vector-file", "version"])
    except getopt.GetoptError:
        display_usage()
        sys.exit(2)
    # handle each possible command line argument
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            display_usage()
            sys.exit()
        elif opt == '--version':
            display_version()
            sys.exit()
        elif opt in ("-b", "--b-values"):
            b_values = arg
        elif opt in ("-d", "--project-dir"):
            project_dir = arg
        elif opt in ("-p", "--pickle-file"):
            pickle_file = arg
        elif opt == '-s':
            subject_id = arg
        elif opt in ("-v", "--vector-file"):
            vector_file = arg
        elif opt == '-w':
            working_dir = arg
    # setup params for connectome mapper
    # ...
    # if we are using a batch directory
    if project_dir:
        setup(pickle_file, project_dir, vector_file, b_values)
        # get subjects
        subjects = get_subjects(project_dir)
        # run subjects
        run(subjects)
    # else, if we are using a single subject / timepoint directory
    elif working_dir:
        setup(pickle_file, working_dir, vector_file, b_values)
        my_subject = subject.Subject(subject_id, working_dir)
        run(my_subject)
    # otherwise we don't have the information we need to proceed
    else:
        print "Need to provide either a subject and working directory or a batch directory."
        sys.exit(2)

    # we are done, exit normally
    sys.exit()

    
def display_usage():
    # TODO: access and print usage file
    print "This is on the wish list"

def display_version():
    from info import __version__
    print __version__

def get_subjects(project_dir):
    '''
    Get all subjects in project directory
    '''
    # create an empty subjects array
    my_subjects = []
    # for each path in project directory
    for path in os.listdir(project_dir):
        fullpath = op.join(project_dir,path)
        if(op.isdir(fullpath)):
            my_subjects.append(subject.Subject(path, fullpath))
    return my_subjects

def run(subjects):
    """For each subject, run connectome mapper with our params"""
    # first try to treat as list, will cause exception if only a
    # single subject
    try:
        for s in subjects:
            if(s.is_valid()):
                cmpgui.subject_name = s.ID
                cmpgui.subject_workingdir = s.directory
                cmp.connectome.mapit(cmpgui)
            else:
                print 'ERROR: Subject ' + s.ID + ' is invalid!'
    except TypeError:
        if(subjects.is_valid()):
            cmpgui.subject_name = subjects.ID
            cmpgui.subject_workingdir = subjects.directory
            cmp.connectome.mapit(cmpgui)
        else:
            print 'ERROR: Subject ' + subjects.ID + ' is invalid!'            
        
def setup(pickle_file, project_dir, vector_file=None, b_values=None):
    """Setup configuration for subsequent runs"""
    cmpgui.load_state(pickle_file)
    cmpgui.project_dir = project_dir
    if(vector_file):
        cmpgui.gradient_table_file = vector_file
        cmpgui.gradient_table = 'custom'
    if(b_values):
        cmpgui.nr_of_b0 = b_values

# entry point        
if __name__ == '__main__':
    main(sys.argv[1:])
