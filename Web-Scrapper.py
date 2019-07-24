# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:45:18 2019

@author: Sucheth
"""

import requests
import bs4

res=requests.get('Enter the website which you want to scrape')
soup=bs4.BeautifulSoup(res.text,'lxml')

for link in soup.find_all('section',{'class':'enter class name '})://you can also enter id etc..
    print(link.text)
   
    
