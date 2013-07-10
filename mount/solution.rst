Assignment 1
---------------
Problem- Generate a program in python which will produce the same output as the mount command.

The problem is solved in 3 steps

1. Open file present at path /proc/mounts in read mode
		f=open("/proc/mounts")
2. Read the file using f.read() and print it on the console.
3. Finally close the file after read is complete using
		f.close()

	Click the link below to see the program

	`link <https://github.com/Christina-B/hometask_christina/blob/master/mount/mount.py/>`_

	Execute the program using following command
		$ chmod +x mount.py

		$ ./mount.py
