if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result= []
for a in range(x+1):
    for b in range(y+1):
      for c in range(z+1):
        if (a+b+c) != n:
            result.append([a,b,c])
print(result)


#!/bin/python3

import json
import turtle
import urllib.request

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())
people = data['number']
names = data['people']
print('Number of people in space >>>',people)
for i in names:
  print(i['name'],'in',i['craft'])

url2 = 'http://api.open-notify.org/iss-now.json'
response2 = urllib.request.urlopen(url2)
data2 = json.loads(response2.read())
position = data2['iss_position']
print('The longitude is >>>', position['longitude'])
print('The latitude is >>>', position['latitude'])
