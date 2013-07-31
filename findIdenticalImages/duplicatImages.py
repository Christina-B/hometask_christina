from PIL import Image, ImageChops
from PIL.ExifTags import TAGS
import glob
import sys

def compare_images(imag1, image2):					#Compares two images
	res = ImageChops.difference(imag1, imag2).getbbox() is None
	return res
	

argument_list = list(sys.argv[1:])
files = list()
if len(argument_list) == 0:
	print "No command line arguments found"
	sys.exit()

for argument in argument_list:
	pathname = argument + "/*.jpg"
	temporary_files = glob.glob(pathname)	#List all the files with .jpg extension
	for f_name in temporary_files:
		files.append(f_name)

leng = len(files)
if leng == 0:
	print "No images present in the directory"
elif leng == 1:
	print "Only one image of jpg type so cannot compare"
else:
	cnt = 1
	for file_name in files:			#Logic for opening image and comparing the images
		name1 = file_name
		imag1 = Image.open(name1)
		filess = files[cnt:]
		for remainin_files in filess:
			name2 = remainin_files
			imag2 = Image.open(name2)
			result = compare_images(imag1, imag2)
			if result == True:
				print "%s and %s are Identical" %(name1, name2)
				flag = 1
			
		cnt += 1
	if flag != 1
		print "No duplicate images found"



