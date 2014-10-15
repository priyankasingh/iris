#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
#all these imports are standard on most modern python implementations
 
#open the xml file for reading:
file = open('users.xml','r')
#convert to string:
data = file.read()
#close file because we dont need it anymore:
file.close()
#parse the xml you got from the file
dom = parseString(data)
#retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
xmlTag = dom.getElementsByTagName('row')[0].toxml()
#strip off the tag (<tag>data</tag>  --->   data):
#xmlData=xmlTag.getAttribute('Id')
#print out the xml tag and data in this format: <tag>data</tag>
print xmlTag
#just print the data
#print xmlData

sed -n 1000,2000p posts.xml >post2.xml
head -n1000 posts.xml > post1000.xml

http://linux.101hacks.com/unix/split/

split -d -l 200000 posts.xml post

$ screen -X -S [session # you want to kill] quit

<?xml version="1.0" encoding="utf-8"?>
<votes>

</votes>

CREATE  TABLE IF NOT EXISTS `Test`.`sof_answers` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `post_id` INT NULL ,
  `parent_id` INT NULL ,
  `creation_date` DATETIME NULL ,
  `score` INT NULL ,
  `body` LONGTEXT NULL ,
  `title` VARCHAR(500) NULL ,
  `owner_user_id` INT NOT NULL ,
  `tags` VARCHAR(500) NULL ,
  `comment_count` INT NULL ,
  `body_annotation` LONGTEXT NULL ,
  `title_annotation` LONGTEXT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB

INSERT into Test.sof_answers 
(post_id,parent_id,creation_date,score,body,owner_user_id,comment_count,body_annotation)
SELECT post_id, parent_id,creation_date,score,body,owner_user_id,comment_count,body_annotation
FROM Test.sof_posts WHERE post_type_id =1
LIMIT 10;

INSERT into Test.sof_questions 
(post_id, accepted_answer_id, creation_date,score,view_count,body,owner_user_id,title,tags,answer_count, comment_count,favourite_count,body_annotation, title_annotation)
SELECT post_id, accepted_answer_id, creation_date,score,view_count,body,owner_user_id,title,tags,answer_count, comment_count, favourite_count,body_annotation, title_annotation
FROM Test.sof_posts WHERE post_type_id =1 and post_id>376188
LIMIT 20000;

ALTER Table Test.sof_answers
	PARTITION BY RANGE (id) (
	 PARTITION p01 VALUES LESS THAN (400000)
	  DATA DIRECTORY = "/export/1/mysql"
	  INDEX DIRECTORY = "/export/1/mysql",
	 PARTITION p02 VALUES Less Than MAXVALUE
	  DATA DIRECTORY = ""
	  INDEX DIRECTORY = ""
);
	  