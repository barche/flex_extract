#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 12:11:00 2020
@author: sbucci
"""
###########################################
## Check for availables flexpart files   ##
###########################################

# how to use:
# python check_file_list.py -i <inputdir> -o <outputfile> -sd YYYYMMDDHH -ed YYYYMMDDHH -fr <frequency> -pr <prefix> 

#input dir is where you have the files stored
#outputfile is the txt file in which you want to list the eventual missing files
#frequency examples: '1H' (ERA5), '3H' (ERA-Interim) 
#prefix examples: 'EA' (ERA5), 'EI' (ERA-Interim)
###########################################

import argparse
# --------------------------------------------------------------------------
# add parser
def get_args():
        parser = argparse.ArgumentParser()

        parser.add_argument("-fr","--frequency",help="time step of the meteo files",required=False)

        parser.add_argument("-pr","--prefix",help="file prefix, indicating the type of meteo files",required=False)

        parser.add_argument("-in","--inputdir", help="Directory of the input meteorological data",required=True)

        parser.add_argument("-o","--outputfile", help="text file in which you want to list the missing data",required=True)

        parser.add_argument("-sd","--startdate",metavar="YYYYMMDDHH",required=True)

        parser.add_argument("-ed","--enddate",metavar="YYYYMMDDHH",required=True)

        args = vars(parser.parse_args())

        return args

args = get_args()

#------------------------------------------------------------------------
# set args
# -----------------------------------------------------------------------

input_dir = args["inputdir"] #DIR == input_dir
outputfile = args["outputfile"] #available_dir
start_date = args["startdate"]
end_date = args["enddate"]
freq=args["frequency"]
prefix=args["prefix"]

#In case the user does not specify the reanalysis we suppose it is ERA5
if args["frequency"] is None: freq='1H'
if args["prefix"] is None: prefix='EA'

if prefix=='EA':
    fmt='%Y%m%d%H'
else:
    fmt='%y%m%d%H'

from datetime import datetime
import pandas as pd
import os
import codecs

dates=datetime.strptime(start_date,'%Y%m%d%H')
datee=datetime.strptime(end_date,'%Y%m%d%H')
out=outputfile+'.txt'
i=0
myfile=codecs.open(out, "w", "utf-8")  # better not shadow Python's built-in file
dater = pd.date_range(dates,datee,freq=freq)
for date in dater:
    date=date.to_pydatetime()
    filename=prefix+date.strftime(fmt)
    if not os.path.exists(os.path.join(input_dir,filename)):
        print(filename)
        i=i+1
        myfile.write(filename+"\n")
if i==0: 
    print("Congratulations, no files missing!")
    myfile.write("Congratulations, no files missing!")
else:
    print("you miss "+str(i)+" files!")
myfile.close()             
