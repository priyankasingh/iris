# http://blog.humaneguitarist.org/2012/03/23/easy-calls-to-opencalais-with-python-daggummit/ this code is based on: http://www.flagonwiththedragon.com/2011/06/08/dead-simple-python-calls-to-open-calais-api/
 
import urllib, urllib2
 
#########################
##### set API key and REST URL values.
 
myCalaisAPI_key = '9aguj5vvwhq23gqpuamy9ene' # your Calais API key.
calaisREST_URL = 'http://api.opencalais.com/enlighten/rest/' # this is the older REST interface.
# info on the newer one: http://www.opencalais.com/documentation/calais-web-service-api/api-invocation/rest
 
# alert user and shut down if the API key variable is still null.
if myCalaisAPI_key == '':
  print "You need to set your Calais API key in the 'myCalaisAPI_key' variable."
  import sys
  sys.exit()
 
#########################
##### set the text to ask Calais to analyze.
 
# text from: http://www.usatoday.com/sports/football/nfl/story/2012-03-22/Tim-Tebow-Jets-hoping-to-avoid-controversy/53717542/1
sampleText = '''
Does Python have a ternary conditional operator? If not available, is it possible to simulate one concisely using other language constructs?
'''
 
#########################
##### set XML parameters for Calais.
 
# see "Input Parameters" at: http://www.opencalais.com/documentation/calais-web-service-api/forming-api-calls/input-parameters
calaisParams = '''
<c:params xmlns:c="http://s.opencalais.com/1/pred/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <c:processingDirectives c:contentType="text/txt"
      c:enableMetadataType="GenericRelations,SocialTags"
      c:outputFormat="Text/Simple"/>
  <c:userDirectives/>
  <c:externalMetadata/>
</c:params>
'''
 
#########################
##### send data to Calais API.
 
# see: http://www.opencalais.com/APICalls
dataToSend = urllib.urlencode({
    'licenseID': myCalaisAPI_key,
    'content': sampleText,
    'paramsXML': calaisParams
})
 
#########################
##### get API results and print them.
 
results = urllib2.urlopen(calaisREST_URL, dataToSend).read()
print results