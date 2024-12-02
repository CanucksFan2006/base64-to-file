import base64
import tkinter as tk
from tkinter import filedialog as fd
import magic as mag
from mimetypes import guess_extension as ge
import os
mag=mag.Magic(mime=True)
root=tk.Tk()
root.title="Convert base 64 text to a usable file"
def convert(file):
    with open(file,"r") as s, open("final","wb+") as final:
        while True:
                chunk=s.read(4)
                if not chunk:
                    break
                else:
                    final.write(base64.b64decode(chunk))
    mimetype=mag.from_file("final")
    ext=ge(mimetype)
    try:
        os.rename("final",f"final{ext}")
    except:
        os.remove("final.txt")
        os.rename("final",f"final{ext}")
    t.config(text=f"The mimetype for the decoded file is {mimetype}\nThe decoded file was written to final{ext} in the same directory as this code")
def test():
    fp=fd.askopenfilename(title="Choose the file with base 64 text",filetypes=[("Text files","*.txt")])
    if fp:
        convert(fp)
    else:
        print("No file selected")
t=tk.Label(text=f"Select a file that contains only base 64\nIf you select a normal file, this code will not work")
t.grid(row=0,column=0)
my_button=tk.Button(root,command=test,text="Select a file that contains only base 64")
my_button.grid(row=1,column=0)
tk.mainloop()