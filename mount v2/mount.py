#!/usr/bin/env python
def func(string):
	str_list = string.split(" ")
	#print str_list
	del str_list[-1]
	del str_list[-1]
	str_list.insert(1,"on")
	str_list.insert(3,"type")
	str_list.insert(5,"(")
	str_list.append(")")
	str1 = " ".join(str_list)
	print str1

f = open("/proc/mounts")
cnt = 1
for x in f:
	if cnt == 1:
		string = x
		cnt = cnt + 1
	else:
		string = x
		#print string
		func(string)
		cnt = cnt + 1
f.close()
	
