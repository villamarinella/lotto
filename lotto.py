from bs4 import BeautifulSoup
import requests
from time import *
from ttk import Frame, Button, Style
from Tkinter import Tk, BOTH
import tkMessageBox as box
from Tkinter import *
import subprocess
import tkFont
import sys
import netifaces as ni
## place this with sudo crontab -e
## 00 20 * * * python lotto.py
def zeig_lotto():
    global treffer,ausgabe
    meine = [1,8,18,30,48,49]  ## Lottozahlen
    sz=1  ## Superzahl
    msz=0
    response = requests.get("http://www.dielottozahlende.net/")
    soup = BeautifulSoup(response.content, "html.parser")
    ziehung = soup.find("div", {"class", "lottozahlen-ziehung"})
    numbers = ziehung.findAll("li")
    #print numbers
    treffer=0
    for index, number in enumerate(numbers):
        wert=int(number.text)
        if index < 6:
           if wert in meine:
              treffer=treffer+1
        else:
	  if wert==sz:
	    msz=sz
        print("{0}. Zahl: {1}".format(index+1, number.text))
    if msz==sz:
          ausgabe=str(treffer)+"  Richtige + Superzahl"
          print str(treffer)+"  Richtige + Superzahl"
    else:
         ausgabe=str(treffer)+"  Richtige "
         print str(treffer)+"  Richtige "
def main():
            zeig_lotto()
            if treffer >=3:
                root = Tk() 
                root.geometry("400x200+400+400")
                mausgabe="\n\n\n"+"     "+ausgabe
                w = Label(root, text=mausgabe, font=("Helvetica", 16))
                w.pack()           
                mainloop()

if __name__ == '__main__':
    main()
