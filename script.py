# coding: utf-8

import requests 
import time
from bs4 import BeautifulSoup
import json


filename = "jokes.json"	
dictionary = {}
k=1
for i in range(1,12):
	url="http://123hindijokes.com/very-funny-jokes/"+str(i)
	
	source=requests.get(url)
	
	source=BeautifulSoup(source.content,"lxml")

	containers = source.find_all('ul',{'class':'statusList'})
	
	for container in containers:
		jokes=container.find_all("li")
		for joke in jokes:
			j=joke.get_text()
			dictionary[k] = j
			k+=1
			with open(filename,"w") as jokes:
				json.dump(dictionary, jokes, ensure_ascii=False,indent=4)
			time.sleep(1)
	print ("done"+str(i))
	
