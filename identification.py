import os
from posixpath import join # provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
base_dire=os.path.dirname(os.path.abspath(__file__))# im looking of the path of our program
imag_dir=os.path.join(base_dire,"image")# lookin for the img which we hve in the folder named image
for root,dir,files in os.walk(imag_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path=os.path.join(root,file)#that s for the path 
            label=os.path.basename(os.path.dirname(path)).replace(" ","-").lower()# we can replace os.path.dirname(path)by root
            print(label,path)# and like that we disply all the img path and the labels s in our file



