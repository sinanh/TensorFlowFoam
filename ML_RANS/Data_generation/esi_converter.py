"""
This script converts ESI OpenFOAM output to be compliant with TensorFlowFoam.
Put your folders containing U, Cy, Cx, and nut files under a directory called train

"""

import os
from shutil import copyfile


filenames = {"U":"U", "Cy":"cy", "Cx":"cx", "nut":"nut"}
curdir = ""
count = 0 

CUR_DIR = os.getcwd()

for subdir, dirs, files in os.walk(r'train'):
    for filename in files:
        if curdir != subdir:
            curdir = subdir
            count += 1
            
        filepath = subdir + os.sep + filename

        if filename in filenames:
            copyfile(filepath, f"{CUR_DIR}/{filenames[filename]}_{count}")
        
os.system("python3 training_data_maker.py ESI")
            