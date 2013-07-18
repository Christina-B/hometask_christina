import feedparser
def feedparse():
	res = feedparser.parse("http://planet.fedoraproject.org/rss20.xml")
	for i in range(len(res['entries'])):
		title_aut = res['entries'][i]['title'].split(':')
		print "TITLE=", title_aut[-1]
		print "AUTHOR=",title_aut[0]
		print "------------------------------------------"

if __name__ == '__main__':
	feedparse()
	exit(0)
