#!/usr/bin/python3
from collections import defaultdict
import regex as re
file_path = 'inputfile.txt' 

# Read multiline text input from a file
with open(file_path, 'r') as file:
    multiline_text = file.read()
# multiline_text='''twone
# '''

ip = list(map(str, multiline_text.split('\n')))
# print(ip)
d = dict()
for res in ip[-2::-1]:
    game, outcomes = map(str, res.split(':'))
    gameID = int(game.split()[1].strip())
    outcomes=list(map(str, outcomes.split(';')))
    d[gameID]=outcomes
ans = 0
for id, res in d.items():
    counts=defaultdict(int)
    for outcome in res:
        colors = outcome.split(',')
        for color in colors:
            num, name = map(str, color.strip().split())
            counts[name]=max(counts[name],int(num))
    if counts['red']<=12 and counts['green']<=13 and counts['blue']<=14:
        ans+=int(id)


print(ans)

# print(d)

