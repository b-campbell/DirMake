import os, shutil

def dirmake(dirname, replace=False):
	if not os.path.exists(dirname):
		print("mkdir")
		# make a new directory with the given name
		os.mkdir(dirname)
	else:
		if (replace):
			print("replace directory")
			# replace the directory (i.e. delete the contents of the old one)
			for f in os.listdir(dirname):
				try:
					if os.path.isdir(dirname): shutil.rmtree(dirname)
					os.mkdir(dirname)
				except Exception as e:
					print(e)
		else:
			print("make new directory")
			# make a new directory with an original name
			s = 0
			dname = dirname
			# count from NAME(1) to NAME(n), stop at first unique directory name
			while (os.path.exists(dname)):
				s += 1
				dname = dirname + '(' + str(s) + ')'
			os.mkdir(dname)
			return dname
	return dirname