# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:34:40 2021

@author: Administrator
"""

def get_tags(url):
    page=requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib')
    tags=[]
    find_tag=soup.findAll('div', attrs = {'class':'ab ac ae af ag dj ai aj'})
    length=len(find_tag)
    if length<2:
        tags.append("null")
        tags.append("null")
        tags.append("null")
        tags.append("null")
        tags.append("null")
        return tags
    get_tag=find_tag[length-2].findAll('li')
    for i in range(len(get_tag)):
        tags.append(get_tag[i].get_text())
    return tags


import requests
from bs4 import BeautifulSoup
import csv
page = requests.get("https://www.hashmapinc.com/blog")
soup = BeautifulSoup(page.content, 'html5lib')
table = soup.find('div', attrs = {'id':'comp-k5vm4ggw'}) 
row=table.findAll("div",attrs={'class':'_3Rcdf'})
heading=[]
for i in row:
    rr=i.findAll("div",attrs={'data-testid':"inline-content"})
    for j in rr:
        justforfun=[]
        date=j.findAll("span",attrs={'style':"color:#545454"})
        for i in range(len(date)):
            justforfun.append(date[i].get_text())
        irl=j.a['href']
        tags=get_tags(irl)
        p=j.find("p",attrs={'style':"font-size:20px"})
        s=p.get_text()
        justforfun.append(s)
        #justforfun.append(irl)
        data=justforfun+tags
        heading.append(data)
        print(heading)
    
    
    
print(heading)   
 
header=['date','author','title','tag1','tag2','tag3','tag4','tag5']
filename = 'hashmap_data_tags.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for head in heading:
        writer.writerow(head)