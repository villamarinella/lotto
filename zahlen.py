#!/usr/bin/python
# -*- coding: utf-8 -*-
# Zahlen bis 02-2017
import csv
import sys
import time
zahl1 = input("1. Zahl: ")
zahl2 = input("2. Zahl: ")
zahl3 = input("3. Zahl: ")
zahl4 = input("4. Zahl: ")
zahl5 = input("5. Zahl: ")
zahl6 = input("6. Zahl: ")
mtreffer= input("Ab wieviel Treffer anzeigen:")
lotto=6*[None]
lotto[0]= str(zahl1 )
lotto[1]= str(zahl2 )
lotto[2]= str(zahl3 )
lotto[3]= str(zahl4 )
lotto[4]= str(zahl5 )
lotto[5] =str(zahl6)
zahlen = 9* [None]
fobj = open("zahlen.csv", "r")
inhalt=csv.reader(fobj, delimiter=',')
for row in inhalt:
   zahlen = row
   i=0
   j=0
   treffer=0
   while True:
      if i >= 6:
	 break
   
      if lotto[j] in zahlen[3:]:
	treffer=treffer+1
	datum=str(zahlen[2])+"."+str(zahlen[1])+"."+str(zahlen[0])
        if treffer >=mtreffer:
	   print 'Am '+datum+" "+str(treffer)+" Treffer"
           print zahlen[3:]
           time.sleep(1) 
        i=i+1
        j=j+1
      else:   
       i=i+1
       j=j+1
fobj.close()

