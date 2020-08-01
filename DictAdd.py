# meter txt con palabras, le agregue las palabras extra que queres que tenga y saque un txt nuevo con las palabras del txt original + las nuevas




import argparse

parser = argparse.ArgumentParser(description='add a text file, add some fuzz ')
parser.add_argument('-f')
parser.add_argument('-w')
args = parser.parse_args()
  

with open(args.f) as f:
    lines = f.readlines()
new_lines = [''.join([x.strip(), (args.w), '\n']) for x in lines]
with open('new.txt', 'w') as f:
    f.writelines(new_lines)