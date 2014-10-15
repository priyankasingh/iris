"""Return list of items from a sub-reddit of reddit.com."""
 
from urllib2 import urlopen, HTTPError 
from json import JSONDecoder
 
def getitems( subreddit, previd=''):
    """Return list of items from a subreddit."""
    url = 'http://www.reddit.com/r/%s.json' % subreddit
    # Get items after item with 'id' of previd.
    if previd != '':
        url = '%s?after=t3_%s' % (url, previd)
    try:
        json = urlopen( url ).read()
        data = JSONDecoder().decode( json )
        items = [ x['data'] for x in data['data']['children'] ]
    except HTTPError as ERROR:
        print '\tHTTP ERROR: Code %s for %s.' % (ERROR.code, url)
        items = []
    return items
 
if __name__ == "__main__":
 
    print 'Recent items for Programming..................'
    ITEMS = getitems( 'programming' )
    for ITEM in ITEMS:
        print '\t%s - %s' % (ITEM['title'], ITEM['url'])
 
    print 'Previous items for Programming..................'
    OLDITEMS = getitems( 'programming', ITEMS[-1]['id'] )
    for ITEM in OLDITEMS:
        print '\t%s - %s' % (ITEM['title'], ITEM['url'])


# GET LINKS: http://www.reddit.com/r/programming/top.json
# Links after an id: http://www.reddit.com/r/programming/top.json?after=t3_1aja28
# Comment: http://www.reddit.com/r/programming/comments/m5gns.json