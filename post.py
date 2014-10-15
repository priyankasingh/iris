#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib2
import xml.etree.ElementTree as xml

#Parse XML directly from the file path
tree = xml.parse("post.xml")

#Get the root node
row = tree.findall("row")

for i in row:
	c_id = i.attrib.get("Id")
	p_id = i.attrib.get("PostTypeId")
	a_id = i.attrib.get("AcceptedAnswerId")
	pr_id = i.attrib.get("ParentId")
	score = i.attrib.get("Title")
                
	print c_id
	print score
	print "--------------"