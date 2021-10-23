# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 10:08:58 2021

@author: Administrator
"""

import csv

with open('hashmap_data_tags.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data=list(csv_reader)

del data[0]
tag_list=[]
for j in range(len(data)):
    for i in range(3,8):
        tag_list.append(data[j][i])

tag_set=set(tag_list)
tag_list=list(tag_set)

medium_list=[]

import requests
from bs4 import BeautifulSoup
for i in range(len(tag_list)):
    tag_list[i]=tag_list[i].lower()
    tag_list[i]=tag_list[i].replace(" ", "")
    
url='https://medium.com/tag/'
page=requests.get(url+tag_list[0])
page

for i in tag_list:
    page=requests.get(url+i)
    medium=[]
    if page.status_code == 200:
        medium.append(i)
        soup = BeautifulSoup(page.content, 'html5lib')
        table = soup.findAll('div', attrs = {'class':'l aj'})
        #length=len(table)
        #length=length-2
        for i in range(len(table)-2,len(table)):
            an=table[i].get_text()
            an=an.rstrip('WStories')
            medium.append(an)
    else:
        medium.append(i)
        medium.append(0)
        medium.append(0)
    print(medium)    
    medium_list.append(medium)
    
    
print(medium_list)
test_list=medium_list

def value_to_float(x):
    if len(x) > 1:
        return float(x.replace('K', '')) * 1000
    return 1000.0
    
for i in medium_list:
    if type(i[1]) == float or type(i[1]) == int:
        continue        
    if 'K' in i[1]:
        i[1]=value_to_float(i[1])
        
for i in medium_list:
    if type(i[2]) == float or type(i[2]) == int:
        continue
    if 'K' in i[2]:
        i[2]=value_to_float(i[2])
    print(i[1],i[2])


header=['tags','stories','writers']
filename = 'medium_data_tags.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for head in medium_list:
        writer.writerow(head)        
    