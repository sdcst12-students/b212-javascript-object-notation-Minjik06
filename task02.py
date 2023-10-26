#!python3
import requests
import json

# we can use requests to retrieve json encoded data from the internet
# there are different methods that we can retrieve the data with: POST and GET
# You can google the difference between POST and GET requests

# Use the json encoded data that is retrieved from this website and print out the weekly menu
# You will need to decipher the json decoded data to determine what information the 
# dictionary object contains

class menu():
    def menu1(self):
        req = requests.get('http://sdcaf.hungrybeagle.com/menu.php')
        data = req.text
        data=json.loads(data)
        return data

    def menu2(self):
        a=self.menu1()
        print(*a.keys())
        print("---------------")
        c=list(a['menu'][0].keys())
        for i in range(len(a['menu'])):
            for j in range(len(c)):
                k=c[j]
                print(f"{k} : {a['menu'][i][k]}")
            print()
    
    def __init__(self):
        self.menu2()  
    
m=menu()

