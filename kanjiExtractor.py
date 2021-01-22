import re
f=open("kanji_tbody.html", encoding="utf8")

f.seek(0,2)
end=f.tell()
f.seek(0)

keyNames=['nr','New','Old','Radical','Strokes','Grade','Year_added','English_meaning','Readings']
iterator=0
x="jouyouKanji=["

iterator=1

while(f.tell()<end):
 x=x+u"\n\t{\n"

 for i in range(0,11):
  if i==0:
   m=f.readline()  
  
 
  if i<10:
   m=f.readline()
   
   if i!=9:
    g=str.rstrip(m)
    g=re.sub('\</td>','',g)
    g=re.sub('\</tr>','',g)
    g=re.sub('<td.*?>','',g)
    g=re.sub('<a.*?>','',g)
    g=re.sub('\<tr>','',g)
    g=re.sub('\</a>','',g)
    g=str.rstrip(g)
   
    x=x+"\t\t"+keyNames[i]+":'"+g+"',\n"
   else:
    x=re.sub(',\s$','',x)
	
 x=x+"\n\t}"
 if f.tell()!=end:
  x=x+","
x=x+"\n];"

m=open("results.txt","w",encoding="utf8")
m.write(x)
