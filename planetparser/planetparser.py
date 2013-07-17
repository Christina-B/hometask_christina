
from bs4 import BeautifulSoup
from urllib2 import urlopen

def planet_parse():
	url = urlopen("http://planet.fedoraproject.org")
	soup = BeautifulSoup(url)
	i = 1
	for x, y in zip(soup.select(".blog-entry-author > a"),	 
			soup.select(".blog-entry-title > a")):
		print i
		print "Title:", y.string 	#for selects and displays the 							#ressult
		print "Author:", x.string
		print
		i = i + 1
if __name__ ==  "__main__":
	planet_parse()
	exit(0)
