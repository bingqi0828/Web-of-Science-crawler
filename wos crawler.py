#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
from lxml import etree
import ssl
import xlwt

tweets=[]
tweet={
    'title'
    }

def loadPage(url):
###############key part
    context=ssl._create_unverified_context()

    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15"}
    request=urllib.request.Request(url,headers=headers)
    html=urllib.request.urlopen(request,context=context).read()
    content=etree.HTML(html)

    link_list=content.xpath('.//div[@class="result-item-content"]/h2/a/@href')
################## key part
    for link in link_list:
        fulllink="https://www.sciencedirect.com" +link
        loadImage(fulllink)

def loadImage(link):
    context=ssl._create_unverified_context()

    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15"}
    request=urllib.request.Request(link,headers=headers)
    html=urllib.request.urlopen(request,context=context).read()
    content=etree.HTML(html)
    result=content.xpath(".//div/strong/text()")
    return result

"""
link="https://www.transit.dot.gov/ntd/national-transit-database-ntd-glossary"
result=loadImage(link)
"""
        


