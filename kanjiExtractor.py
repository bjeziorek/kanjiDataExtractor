import re

f=open("kanji_tbody.html", encoding="utf8")
f.seek(0,2)
end=f.tell()
f.seek(0)
keyNames=['nr','New','Old','Radical','Strokes','Grade','Year_added','English_meaning','Readings_kana','Readings_romaji']
x="jouyouKanji=["

while(f.tell()<end):
 x=x+u"\n\t{\n"
 for i in range(0,10):
  if i==0:
   m=f.readline()  
  if i<10:
   m=f.readline()
   if i!=9:
    g=str.rstrip(m)
    g=re.sub('</td>','',g)
    g=re.sub('</tr>','',g)
    g=re.sub('<td.*?>','',g)
    g=re.sub('<a.*?>','',g)
    g=re.sub('<tr>','',g)
    g=re.sub('</a>','',g)
    g=re.sub('\'','\\\'',g)
    g=re.sub('<span.*?</span>','',g)
    g=re.sub('<sup.*?</sup>','',g)
    g=str.rstrip(g)
    if keyNames[i]=='Readings_kana':
     z=re.sub('>.*','',g)
     z=re.sub('<br','',z)
     x=x+"\t\t"+keyNames[i]+":'"+z+"',\n"
     i=i+1
     z=re.sub('.*<','',g)
     z=re.sub('br>','',z)
     x=x+"\t\t"+keyNames[i]+":'"+z+"',"
    else:
     x=x+"\t\t"+keyNames[i]+":'"+g+"',\n"
   else:
    x=re.sub(',$','',x)
 x=x+"\n\t}"
 if f.tell()!=end:
  x=x+","
x=x+"\n];"

m=open("results.txt","w",encoding="utf8")
m.write(x)
