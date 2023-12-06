#!/usr/bin/python3
import argparse
import subprocess
import sys
import requests

SESSION = '<session-id>'
useragent = 'https://github.com/jonathanpaulson/AdventOfCode/blob/master/get_input.py by jonathanpaulson@gmail.com'

parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2023)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}" -A \'{useragent}\''
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')

# Save the output to a text file named 'inputfile.txt'
with open('inputfile.txt', 'w') as file:
    file.write(output)

print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)