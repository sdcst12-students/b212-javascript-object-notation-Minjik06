#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

import json
class max():
    def file1a(self):
        filename1='task01a.txt'

        file=open(filename1, "r")

        fileData1=file.read()

        file1=json.loads(fileData1)
        return file1

    def file2a(self):
        filename2='task01b.txt'

        file2=open(filename2, "r")

        fileData2=file2.read()

        file2=json.loads(fileData2)
        return file2

    def file3a(self):
        filename3='task01c.txt'

        file3=open(filename3, "r")

        fileData3=file3.read()

        file3=json.loads(fileData3)
        return file3

    def cal1(self):
        a=self.file1a()
        max1=0
        for i in range(len(a)):
            if max1<a[i]:
                max1=a[i]
        print(f"max (file: task01a.txt)-> {max1}")
        return max1

    def cal2(self):
        a=self.file2a()
        max1=0
        for i in range(len(a)):
            if max1<a[i]:
                max1=a[i]
        print(f"max (file: task01b.txt)-> {max1}")
        return max1

    def cal3(self):
        a=self.file3a()
        max1=0
        for i in range(len(a)):
            if max1<a[i]:
                max1=a[i]
        print(f"max (file: task01c.txt)-> {max1}")
        return max1

    def __init__(self):
        self.cal1()
        self.cal2()
        self.cal3()


m=max()



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