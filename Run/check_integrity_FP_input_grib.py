'''
simple integrity check of downloaded FLEXPART input files

just checking if python can read them and if the files contain 845 grib
messages (I had some corrupt files before which had 869 messages and FP
was not able to read them)

counts the files in the provided main directory and its sub-directory

you need a working python environment and the eccodes library

usage: python check_integrity_FP_input_grip.py

Andreas Plach, UniWien, October 2020

'''

import os
import datetime as dt
import pygrib
import fnmatch
import re

path = ('/raid61/scratch/aplach/ECMWF_DATA/EA_fields/checked/2001/')

# create a sorted dictionary of all files in main path and
# sub-directories
for (dirpath, dirnames, filenames) in os.walk(path):
    print(dirnames)
    # now loop through the files in sub-directory

    # list of patterns to exclude
    excludes = ['*.tmp', '*.txt']
    excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'
    files = [f for f in filenames if not re.match(excludes, f)]

    # create a file which will contain a list of corrupted files
    corrfile = (dirpath[:-2] + dirpath[-2:] + '_list_of_corrupt_files.txt')

    # write some basic info into the respective files
    corrupt = open(corrfile, 'w')
    corrupt.write(str(dt.datetime.now())+'\n')
    corrupt.write('total number of files in sub-dir: '+str(len(files))+'\n')
    corrupt.write('list of corrupted files in sub-dir below:\n')
    corrupt.write('-----------------------------------------\n')
    corrupt.close()

    for filename in sorted(files):
        # if query to ignore some files
        if(filename[-4:] != '.tmp') and (filename[-4:] != '.txt'):
            print(filename)
            gr = pygrib.open(dirpath + '/' + filename)
            try:
                gr[1]
                if (gr.messages != 845):
                    print('The number of grib messages is not equal to 845; '
                          'there might be problem with the file')
                    corrupt = open(corrfile, 'a')
                    corrupt.write(dirpath + '/' + filename  +'\n')
                    corrupt.close()
            except RuntimeError as e:
                print(e)
                corrupt = open(corrfile, 'a')
                corrupt.write(dirpath + '/' + filename  +'\n')
                corrupt.close()
