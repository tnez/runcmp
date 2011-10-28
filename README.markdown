
# runcmp

A small bit of python to drive the Connectome Mapper
<http://www.cmtk.org/connectomemapper> in a gui-less manner.

# Usage

## Required Arguments: 

    -p:'path-to-pickle-file', --pickle-file='...' : load the configuration
        stored in the given pickle file

## Optional Arguments:

    -b:'number-of-b-values', --b-values='...' : number of b-values included
        in scans

    -d:'path-to-project-directory', --project-dir='...' : this directory
        should contain all subject directories that you wish to run;
        this script will iterate over all child directories. Extraneous,
        non-subject, directories will cause errors *

    -h, --help : display this dialog

    *TODO* -m, comma-sperated list of keys and values "key1,value1,key2,value2..."

    -s: subject id

    *TODO* -t: test run, ie set values and output but do not actually run cmp

    -v:'path-to-vector-file', --vector-file='...' : the bvec file

    --version : display the current version of this software

    -w: working directory *

    * either a subject xor working directory must be specified

## Examples:

Iterate over a specified directory full of subject directories, using
a given pickle-file, gradient-map, and specify 4 b-values.

    python runcmp.py -p $HOME/pickle_files/my-pickle-file.pkl
                     -d $HOME/data/my-project
                     -v $HOME/data/my-project/bvec -b 4

Run the specified subject timepoint whilst providing metadata to be
used at processing time.

    python runcmp.py -p $HOME/pickle_files/my-pickle-file.pkl -s 317
                     -m "group,control,tp,1"
                     -w $HOME/data/my-project/317/timepoints/1
