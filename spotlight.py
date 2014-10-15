#import urllib
import urllib2

url = "http://spotlight.dbpedia.org/rest/annotate/"
data = "disambiguator=Document&confidence=0.2&support=20&text=A Dictionary of Algorithms and Data Structures"
headers = { "Accept" : "text/xml",
        "conthent-Type": "application/x-www-form-urlencoded"}
        
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page