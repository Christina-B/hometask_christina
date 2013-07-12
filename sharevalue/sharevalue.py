#!/usr/bin/env python
import urllib2, sys

def show_share_value(str1):
	req = urllib2.Request('http://download.finance.yahoo.com/d/quotes?s='+str1+'&f=l1')
	try:	res = urllib2.urlopen(req)	#open URL
	except URLError as e:
		print e.reason
	print "The share value for %s is %s" % (str1, res.read())
	
		
arg1 = list(sys.argv)		#take the command line argument
string = arg1[1]		#take the 2nd argument in string
show_share_value(string)	#call to function


