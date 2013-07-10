#!/usr/bin/env python
f = open("/proc/mounts")	#open file default mode is read mode
print f.read() 			# Read the contents of file print it on console
f.close()			# Close the file after reading
