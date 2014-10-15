#!/usr/bin/python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import re
import urllib2

base_url = "http://stackoverflow.com"
program_url = base_url + "/questions/tagged/eclipse-wtp?sort=votes&pagesize=50"

soup = BeautifulSoup(urllib2.urlopen(program_url))

for page in soup.findAll("span",{'class': 'page-numbers'}):
	a = page.string
	
print a

pages = range(1, int(a) + 1)
for p in pages:	
	url = '%s&page=%s' % (program_url,p)
	print url
	
	soup2 = BeautifulSoup(urllib2.urlopen(url))
	
	for link in soup2.findAll("a",{'class' : 'question-hyperlink'}):
		tag_url = base_url + link.get('href')
		tag = link.string
#		print tag.encode('utf-8') , tag_url