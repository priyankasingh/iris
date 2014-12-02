import urllib, urllib2
import MySQLdb

db = MySQLdb.connect(
	host="localhost",
	user="root",
	passwd="Rakhee7",
	db="Test")

cursor = db.cursor()

query = """SELECT body, id FROM sof_questions WHERE id > 814234 LIMIT 5000;"""

cursor.execute(query)
numrows = int(cursor.rowcount)

rows = cursor.fetchall()
#post = rows[0]

for i in range (numrows):
	pid = rows[i][1]
	#print pid
	#text = rows[i][0]
	text2 = urllib.quote(rows[i][0])

	url = "http://spotlight.dbpedia.org/rest/annotate/"
	#data = rows[i][0]
	data = "disambiguator=Document&confidence=0.2&support=20&text=" + text2
	#A Dictionary of Algorithms and Data Structures"
	headers = { "Accept" : "application/rdf+xml", "content-Type" : "application/x-www-form-urlencoded"}

	try:
		req = urllib2.Request(url, data, headers)
		response = urllib2.urlopen(req)
		page = response.read()
		#print page
		#print "*******************************"
		query2 = """UPDATE red_posts SET
			body_annotation = '%s' WHERE id = '%s'
			""" % (page, pid)
		try:
			cursor.execute(query2)
			db.commit()
			print "Update Successful"
		except:
			pass
	except:
		pass
