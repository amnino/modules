import requests
from bs4 import BeautifulSoup as BS
name =[]
datae=[]
site = 'http://www.livepriceofgold.com/india-gold-price.html'
page = requests.get(site)
data = page.content
soup = BS(data, 'html.parser')
table=soup.find("table",{'class':'data-table-2'})
#a = soup.find_all('div').find('table')
rows=table.find_all('tr')
for row in rows:
    name.append(row.find_all('td')[2].text)
#gold10g = float(name[1])
#print(gold10g)
for i in name[3]:
    if i != ' ':
        if i == '.':
            datae.append(i)
            continue
        datae.append(int(i))
str0 = ''.join(str(x) for x in datae)
output = float(str0)
gold10g = output/1000
print('Price for 10 gm gold in INR >>>',gold10g)
