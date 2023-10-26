from tkinter import *
from tkhtmlview import HTMLLabel
import requests
import json
 

req = requests.get('https://open-meteo.com/en/docs')
data = req.text
data=json.dumps(data)
#data=json.loads(data)

tk = Tk()
 
tk.geometry("400x400")
 
html = HTMLLabel(tk, html=data)
 
html.pack(pady=20, padx=20)
 
tk.mainloop()