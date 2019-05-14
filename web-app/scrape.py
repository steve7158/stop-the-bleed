#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:47:21 2019

@author: steve
"""
import requests
import bs4
res=requests.get('http://127.0.0.1:5000/')
print(type(res))
res.text
import lxml

soup=bs4.BeautifulSoup('<p id="question"></p>', features="xml")
h1=soup.select('<p id="question"></p>')
tag=soup.b
print(tag.string)
print(h1)
