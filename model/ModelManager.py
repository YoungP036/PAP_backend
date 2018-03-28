from src.inference.classify import classify
import json
import requests
import random
from datetime import datetime
import os


class mManager:
	#@PARAMS
	#the only parameter you need to pass is the URL of the firebase link
	#
	#Returns a STRING formatted as a json object would be with the top 5 results
	#ie. {"wire-haired_fox_terrier": 0.0005762370419688523, "doberman": 0.00038512199535034597, 
	# "otterhound": 0.004826174583286047, "irish_terrier": 0.010737168602645397, "giant_schnauzer": 0.0005427176365628839, 
	# "airedale": 0.9818733930587769}
	def queryModel(self, URL):
		path=self.getImage(URL)
		data=classify('file', path)
		os.remove(path)
		#using the data returned by the model, select the top 5 results and package them into dictionary
		
		i=0
		for index,row in data.iterrows():
			if i<=0:
				r=row['breed']
				i+=1

		#package dictionary into JSON string
		#results=json.dumps(r)
		return r
	
	def getImage(self, URL):
		r = requests.get(URL, allow_redirects=True)
		random.seed(datetime.now())
		rand=random.randint(0,2147483647)
		path=str(rand)+'.jpg'
		open(path, 'wb').write(r.content)
		return path
