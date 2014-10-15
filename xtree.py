import xml.etree.ElementTree as xml
#Parse XML directly from the file path
tree = xml.parse("users.xml")

#Get the root node
row = tree.findall("row")

for i in row:
	print i.attrib.get("Id")
	print i.attrib.get("Reputation")
	print i.attrib.get("CreationDate")
	print i.attrib.get("EmailHash")
	print i.attrib.get("LastAccessDate")
	print i.attrib.get("WebsiteUrl")
	print i.attrib.get("Location")
	print i.attrib.get("AboutMe")
	print i.attrib.get("Views")
	print i.attrib.get("UpVotes")
	print i.attrib.get("DownVotes")
	
	
#http://effbot.org/zone/element-iterparse.htm#incremental-parsing