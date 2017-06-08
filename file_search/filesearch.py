import os
import re
import sys
import pprint
search = raw_input("Enter FileName to search: ")
List = []
fcount=0
var = re.compile(search,re.IGNORECASE)
rootdir = raw_input("Enter where to search: (To search in present directory leave as it is)")
if(rootdir==""):
	rootdir='.'
for root, dirs, files in os.walk(rootdir, topdown=True):
    for name in files:
	count=0	
	m = var.search(name)
	if m:
		dest=os.path.join(root,name)
		count=1		
		print('Found at : '+dest[1:])
		fcount+=1
	if count==0:
		for name in dirs:
			m = var.search(name)
			if m:
				dest=os.path.join(root,name)
				count=1		
				print('Found at : '+dest[1:])
				fcount+=1
print('Total Number of Files found : '+str(fcount))
