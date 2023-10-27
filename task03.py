from tkinter import *
from tkhtmlview import HTMLLabel
import requests
import json
 

req = requests.get('https://open-meteo.com/en/docs')
data = req.text
data=json.dumps(data)
data=json.loads(data)

tk = Tk()
 
tk.geometry("500x500")
 
html = HTMLLabel(tk, html=data)
 
html.pack(pady=50, padx=50)
 
tk.mainloop()