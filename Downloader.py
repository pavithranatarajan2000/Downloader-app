from __future__ import unicode_literals  
import youtube_dl
import urllib
import shutil
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import requests
 
 
window = tk.Tk()

window.title("Download Your interesting youtube video & PDF")
window.minsize(600,400)

window.configure(bg='blue')
 
def Youtube():
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([name.get()])
 
label = ttk.Label(window, text = "Enter Your url")
label.grid(column = 0, row = 0)

def PDF():
    filename = Path('PDF1.pdf')
    url = name.get()
    response = requests.get(url)
    filename.write_bytes(response.content)
print("1ist is: ")
print("1.YOUTUBE VIDEO")
print("2.PDF DOWNLOAD")
option=int(input("Enter 1 or 2: "))

if(option==1):
    label = ttk.Label(window, text = "Enter Your url")
    label.grid(column = 0, row = 0)
    name = tk.StringVar()
    nameEntered = ttk.Entry(window, width = 15, textvariable = name)
    nameEntered.grid(column = 0, row = 1)
    button1 = ttk.Button(window, text = "Download_video", command = Youtube)
    button1.grid(column= 0, row = 2)
elif(option==2):
    label = ttk.Label(window, text = "Enter Your url")
    label.grid(column = 0, row = 0)
    name = tk.StringVar()
    nameEntered = ttk.Entry(window, width = 15, textvariable = name)
    nameEntered.grid(column = 0, row = 1)
    button1 = ttk.Button(window, text = "Download_PDF", command = PDF)
    button1.grid(column= 0, row = 2)
else:
    print("Sorry!! there is no such kind of option")
 
window.mainloop()
