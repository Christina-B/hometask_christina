Assignment 1
---------------
Problem- Generate a program in python which will produce the same output as the mount command.

Description

1. The file is opened in read mode using f = open("/proc/mounts"). The default
   mode is read.
2. Each line of the file is read
   For each line a function call is made to function func
   The function func is responsible for converting the string which is 
   passed to it into a list.
   The last two elements of the list are deleted.
   Then on,type,( and ) are added to the list.
   The list is then converted into string and printed on the console.
3. After the operation is complete file is closed.

	Click the link below to see the program

	`link <https://github.com/Christina-B/hometask_christina/blob/master/mount%20v2/mount.py>`_

	Execute the program using following command
		$ chmod +x mount.py

		$ ./mount.py
