import pwd
userlist =  pwd.getpwall()
#print userlist
print type(userlist)
print len(userlist)
for i in userlist:
	print i
	string = str(i)
	findcnt = string.find(nologin)
	print findcnt
	print 
