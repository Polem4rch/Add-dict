#!/bin/env python3
import argparse
import os

print("               ")

print("Add-dict Rules!")


print("  ------ ")
print("     \   ")
print("      \  ")
print("     .ﾊ,,ﾊ")
print("     ( ﾟωﾟ)")
print("     |つ  つ")
print("     |    |")
print("     |    |")
print("     U    U ")
print("        [FILE CREATED]")


parser = argparse.ArgumentParser(description='usage: python3 dictadd.py -f txtfile -w new word to append ')
parser.add_argument('-f')
parser.add_argument('-w')
parser.add_argument('-p', '--prefix')
args = parser.parse_args()

words = args.w.split(',')
output_name = 'catput.txt'

# delete output before starting
# os.remove(output_name)
with open(args.f) as input, open(output_name, 'w') as output:
    for line in input:
        accum = ''
        for w in words:
            accum += w
            output.write(args.prefix + line.rstrip() + accum + os.linesep)
