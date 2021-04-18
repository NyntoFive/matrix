#!/usr/bin/env python
# coding: utf-8
import os
import json
from requests_html import AsyncHTMLSession, HTMLSession

import pandas as pd


def list_files():
    files = [ file for file in os.listdir() if 'file' in file ]
    if not files:
        return "Empty"
    return files

# In[5]:


print(files)


# In[22]:


with open('1file.json','r') as f:
    data=json.load(f)
fields=['name', 'description', 'mainImage', 'images', 'url', 'offers', 'breadcrumbs', 'probability', 'mpn']
all_fields=['name', 'description', 'mainImage', 'images', 'url', 'additionalProperty', 'offers', 'sku', 'breadcrumbs', 'probability', 'mpn']
#for field in fields:
  #  test=data[0]

    #test[field]=data[0]['product'][field]

item=Product()


# In[20]:


from django.db import models


for file in files:
    with open(file, 'r') as f:
        data=json.load(f)
    for row in data:
        new = Product()
        new.objects.create(sku = row['product']['mpn'],
            description = row['product']['description'],
            mainImage = row['product']['mainImage'],
            images = row['product']['images'],
            url = row['product']['url'],
            price = row['offers'][0]['price'],
            category = row['breadcrumbs'][2]['name'])
        new.save()

        


# In[ ]:


b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')

