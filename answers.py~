import MySQLdb

db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Rakhee7",
        db="Test")

cursor = db.cursor()

query = """SELECT id, post_id,accepted_answer_id, title, tags, title_annotation FROM sof_questions LIMIT 5;"""

cursor.execute(query)
numrows = int(cursor.rowcount)

rows = cursor.fetchall()


for i in range (numrows):
	postid = rows[i][1]
	answerid = rows[i][2]
	title = rows[i][3]
	tags = rows[i][4]
	tit_a = rows[i][5]
	print answerid

	if answerid !=0	:
		cursor.execute("""SELECT post_id,parent_id
			FROM sof_posts WHERE post_id ='%s';""" %(answerid))

		rows2 = cursor.fetchone()
		
		pid = rows2[0]
		prid = rows2[1]

		query2 = """INSERT into sof_answers
			(post_id,parent_id,title,tags,title_annotation)
			VALUES ('%s','%s','%s','%s','%s')
			"""% (pid,prid,c,title,tags,tit_a)

		cursor.execute(query2)	
		db.commit()
		print "Insert Successful"
