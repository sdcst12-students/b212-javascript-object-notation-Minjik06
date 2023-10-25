#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

import json
filename1='task01a.txt'

file=open(filename1, "r")

fileData1=file.read()


max1=0
for i in range(len(fileData1)):
    print(fileData1[i])
print(max1)



"""class sum:
    def file(self):

        filename1='task03.txt'

        file=open(filename1, "r")

        fileData1=file.read()

        sp2 = fileData1.split("\n")

        print(sp2)
        return sp2

    def maxS(self):
        a=self.file()
        max=0
        total=0
        for i in range(len(a)):
            if a[i]!='':
                total+=int(a[i])
            elif a[i]=='':
                if total>max:
                    max=total
                    total=0
                total=0
        print()
        print(max)
        return max
    
    def __init__(self):
        self.maxS()

s=sum()"""