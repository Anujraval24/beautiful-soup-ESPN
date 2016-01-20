from bs4 import BeautifulSoup
import requests
import urllib2

f=open("bs4-espn.txt","w")
x=0
while(x<500):
   soup=BeautifulSoup(urllib2.urlopen("http://games.espn.go.com/ffl/tools/projections?startIndex="+str(x)).read(),'html')

   tables=soup.find("table",{'class':"playerTableTable tableBody"})
   for row in tables.findAll('tr')[2:]:
      #kr= row.findAll('tr')[2:]
   
      #print kr[0].text
      
      col=row.findAll('td')
      try:
         name=col[0].a.string.strip()
         f.write(name + '\n')
      except:
         pass

   x=x+40


#for kr in data2:
#   print kr.find_all("h4",{"class":"store-name"})[0].text
#   print kr.find_all("span",{"class":"desk-add jaddt"})[0].text

