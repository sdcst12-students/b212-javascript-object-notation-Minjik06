import json
filename1='task01a.txt'

file=open(filename1, "r")

fileData1=file.read()

file1=json.loads(fileData1)
print(file1)


max1=0
for i in range(len(file1)):
    if max1<file1[i]:
        max1=file1[i]
print(f"max: {max1}")