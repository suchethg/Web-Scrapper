# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:45:18 2019

@author: Sucheth
"""

import requests
import bs4

res=requests.get('https://reva.edu.in/socit/faculty')
soup=bs4.BeautifulSoup(res.text,'lxml')

for link in soup.find_all('section',{'class':'commonWidth centerpart'}):
    print(link.text)
   
    