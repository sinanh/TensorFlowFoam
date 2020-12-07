
import argparse

parser = argparse.ArgumentParser(description='Changes velocity(U) in inlet condition.')
parser.add_argument('U', metavar='u', type=float, help='new value for the U')


args = parser.parse_args()
u = args.U
 
f = open("U","r")
lines = f.readlines()
lines[25] =f"        value           uniform ({args.U} 0 0);\n"
f = open("U","w")

f.writelines(lines)
f.close()