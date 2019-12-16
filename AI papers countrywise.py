import requests
import lxml.html as lh
import pandas as pd

book={}
my_list=[]

for m in range(1996,2019):
  url='https://www.scimagojr.com/countryrank.php?category=1702&year={}'.format(m)
  #Create a handle, page, to handle the contents of the website
  page = requests.get(url)
  #Store the contents of the website under doc
  doc = lh.fromstring(page.content)
  #Parse data that are stored between <td>..</td> of HTML
  tr_elements = doc.xpath('//td') 

  col={}  
  

  for i in range(21):
    l=2+i+i*8
    t=[tr_elements[l:l+2]]
    for a,b in t:
      name=a.text_content()
      number=b.text_content()
      col[name]=number
      my_list.append([m,name,number])
      #print([m,name,number])

  book[m]=col
