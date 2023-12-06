#!/usr/bin/python3
import regex as re
file_path = 'inputfile.txt' 

# Read multiline text input from a file
with open(file_path, 'r') as file:
    multiline_text = file.read()
# multiline_text='''twone
# '''
ans=0

digits = {'one':'o1e', 'two':'t2o', 'three':'t3e', 'four':'f4r', 'five':'f5e', 'six':'s6x', 'seven':'s7n', 'eight':'e8t', 'nine':'n9e'}

ip = list(map(str, multiline_text.split('\n')))
# print(ip)
for word in ip[-2::-1]:
    for key, value in digits.items():
        word = word.replace(str(key), str(value))
    temp = [int(match) for match in re.findall(r'\d', word)]
    print(temp)
    # if temp==[]:
    #     break
    num = 10*temp[0] + temp[-1]
    ans+=num
print(ans)