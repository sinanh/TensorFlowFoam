import argparse
import numpy as np
from distutils.dir_util import copy_tree
import os 
import pathlib


PATH = pathlib.Path(__file__).parent.absolute()

parser = argparse.ArgumentParser(description='Changes velocity(U) in inlet condition.')
parser.add_argument('start', metavar='s', type=float, help='start velocity')
parser.add_argument('finish', metavar='f', type=float, help='finish velocity')
parser.add_argument('step', metavar='t', type=float, help='finish velocity')

args = parser.parse_args()


case_num = 0



for i in np.arange(args.start, args.finish, args.step):
    #Open a folder for each case, and copy org to case[i]
    # Case[i]
    case_num += 1
    case_dir = f"{case_name}/Case{case_num}"
    os.system("pwd")
    copy_tree("org/", case_dir)


    # Change U
    print(f"changing velocity to {i}")
    f = open(case_dir+"/0/U","r")
    lines = f.readlines()
    lines[25] =f"        value           uniform ({i} 0 0);\n"
    f = open(case_dir+"/0/U","w")
    f.writelines(lines)
    f.close()
    
    #Exec BlockMesh
    os.chdir(case_dir)
    os.system("pwd")
    os.system("blockMesh")

    #Exec Potentialfoam
    os.system("potentialFoam")

    #simpleFoam | tee log.simpleFoam
    os.system("simpleFoam | tee log.simpleFoam")

    # change to parent directory
    os.chdir(PATH)
  

if __name__ == '__main__':
    # Create a design directory
    case_name = input("enter case name:")
    os.mkdir(case_name)
    
 

