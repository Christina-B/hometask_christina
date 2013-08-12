import pwd

database = pwd.getpwall()
for info in database:
	string = str(info)
	index = string.find("nologin")
	if index == -1:
		print "%s can login" %(info[0])



	
