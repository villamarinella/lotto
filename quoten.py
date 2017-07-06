# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup

url ="http://www.dielottozahlende.net/lotto/6aus49/lottoquoten.php"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

def find_str(s, char):
    index = 0
    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index
            index += 1
    return -1

def insertChar(mystring, position, chartoinsert ):
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring  

for script in soup(["script", "style"]):
    script.extract()    # rip it out
text = soup.get_text()
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text1 = '\n'.join(chunk for chunk in chunks if chunk)

such1="Lottoquoten 6 aus 49 aktuelle Ziehungen Lottoquoten und Lottogewinne "
pos1=find_str(text1,such1)
text=text1[pos1:(pos1+600)]
text1=""
#print text
datum=text[86:96]
print datum
such1="Gewinnklasse 1"
pos1=find_str(text,such1)
such2="Gewinnklasse 2"
pos2=find_str(text,such2)
such3="Gewinnklasse 3"
pos3=find_str(text,such3)
such4="Gewinnklasse 4"
pos4=find_str(text,such4)
such5="Gewinnklasse 5"
pos5=find_str(text,such5)
such6="Gewinnklasse 6"
pos6=find_str(text,such6)
such7="Gewinnklasse 7"
pos7=find_str(text,such7)
such8="Gewinnklasse 8"
pos8=find_str(text,such8)
such9="Gewinnklasse 9"
pos9=find_str(text,such9)

gk1= text[pos1:pos2]
gk2=text[pos2:pos3]
gk3= text[pos3:pos4]
gk4 =text[pos4:pos5]
gk5 =text[pos5:pos6]
gk6 =text[pos6:pos7]
gk7 =text[pos7:pos8]
gk8 =text[pos8:pos9]
gk9=text[pos9:pos9+57]

gk1_1=insertChar(gk1,14, ' ')    
posa=find_str(gk1_1,'er')
gk1_2=insertChar(gk1_1,posa+2, ' ')    
posb=find_str(gk1_2,'hl')
gk1_3=insertChar(gk1_2,posb+2, ' ') 
print gk1_3

gk2_1=insertChar(gk2,14, ' ')    
posa=find_str(gk2_1,'er')
gk2_2=insertChar(gk2_1,posa+2, ' ')    
posb=find_str(gk2_2,'ge')
gk2_3=insertChar(gk2_2,posb+2, ' ') 
print gk2_3

gk3_1=insertChar(gk3,14, ' ')    
posa=find_str(gk3_1,'er')
gk3_2=insertChar(gk3_1,posa+2, ' ')    
posb=find_str(gk3_2,'hl')
gk3_3=insertChar(gk3_2,posb+2, ' ') 
print gk3_3

gk4_1=insertChar(gk4,14, ' ')    
posa=find_str(gk4_1,'er')
gk4_2=insertChar(gk4_1,posa+2, ' ')    
posb=find_str(gk4_2,'ge')
gk4_3=insertChar(gk4_2,posb+2, ' ') 
print gk4_3

gk5_1=insertChar(gk5,14, ' ')    
posa=find_str(gk5_1,'er')
gk5_2=insertChar(gk5_1,posa+2, ' ')    
posb=find_str(gk5_2,'hl')
gk5_3=insertChar(gk5_2,posb+2, ' ') 
print gk5_3

gk6_1=insertChar(gk6,14, ' ')    
posa=find_str(gk6_1,'er')
gk6_2=insertChar(gk6_1,posa+2, ' ')    
posb=find_str(gk6_2,'ge')
gk6_3=insertChar(gk6_2,posb+2, ' ') 
print gk6_3

gk7_1=insertChar(gk7,14, ' ')    
posa=find_str(gk7_1,'er')
gk7_2=insertChar(gk7_1,posa+2, ' ')    
posb=find_str(gk7_2,'hl')
gk7_3=insertChar(gk7_2,posb+2, ' ') 
print gk7_3

gk8_1=insertChar(gk8,14, ' ')    
posa=find_str(gk8_1,'er')
gk8_2=insertChar(gk8_1,posa+2, ' ')    
posb=find_str(gk8_2,'ge')
gk8_3=insertChar(gk8_2,posb+2, ' ') 
print gk8_3

gk9_1=insertChar(gk9,14, ' ')    
posa=find_str(gk9_1,'er')
gk9_2=insertChar(gk9_1,posa+2, ' ')    
posb=find_str(gk9_2,'hl')
gk9_3=insertChar(gk9_2,posb+2, ' ') 
print gk9_3



