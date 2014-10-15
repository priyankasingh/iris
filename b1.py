#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import re
import urllib2

base_url = "http://stackoverflow.com"
program_url = base_url + "/tags?page="


for page in range(1,3):
	url = "%s%d" % (program_url, page)
	soup = BeautifulSoup(urllib2.urlopen(url))
	
	for link in soup.findAll("a",{'class' : 'post-tag'}):
		tag_url = base_url + link.get('href')
		tag = link.string
		print tag, tag_url
		
		http://stackoverflow.com/questions/2564568/python-mysql-check-for-duplicate-before-insert?answertab=votes#tab-top
		
		
		
#!/usr/bin/python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import re
import urllib2
import MySQLdb

db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Southampton11",
        db="Test")

cursor = db.cursor()

base_url = "http://stackoverflow.com"
program_url = base_url + "/tags?page="


for page in range(1,893):
        url = "%s%d" % (program_url, page)
        soup = BeautifulSoup(urllib2.urlopen(url))

        for link in soup.findAll("a",{'class' : 'post-tag'}):
                tag_url = base_url + link.get('href')
                tag = link.string
                #print tag, tag_url

                query = """INSERT INTO sof_tag (tag, tag_url) 
                        VALUES ('%s', '%s');
                        """ % (tag, tag_url)

                try:
                        cursor.execute(query)
                        db.commit()

                except (ValueError) as e:
              		print e
#                       db.rollback()
#                       db.close()

#db.close()


#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib2
import MySQLdb
from BeautifulSoup import BeautifulSoup


db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Southampton11",
        db="Test")

cursor = db.cursor()

query = """SELECT tag_url FROM sof_tag limit 5;"""

try:
        cursor.execute(query)
        numrows = int(cursor.rowcount)
		rows = cursor.fetchall()
		print rows
		raw
        for i in range (numrows):
                
#               print row[0]
                base_url = row[0]
                program_url = base_url + "?sort=votes&pagesize=50"

                soup = BeautifulSoup(urllib2.urlopen(program_url))

                for page in soup.findAll("span",{'class': 'page-numbers'}):
                        a = page.string

                print a
#               pages = range(1, int(a) + 1)
                pages = range(1, 3)
                for p in pages:
                        url = '%s&page=%s' % (program_url,p)
                        print url

                        soup2 = BeautifulSoup(urllib2.urlopen(url))

                        for link in soup2.findAll("a",{'class' : 'question-hyperlink'}):
                                tag_url = base_url + link.get('href')
                                tag = link.string

                                query2 = """INSERT IGNORE INTO sof_question 
                                        (question, question_url, created_date, modified_date) 
                                        VALUES ('%s', '%s', NOW(), NOW())
                                        ON DUPLICATE KEY UPDATE modified_date = NOW();
                                        """ % (tag, tag_url)

                                cursor.execute(query2)
                                db.commit()


#                               print tag.encode('utf-8') , tag_url     


except (ValueError) as e:
        print e
                 