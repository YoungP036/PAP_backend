from src.inference.classify import classify
import json
import requests
import random
from datetime import datetime
import os


class mManager:
	#@PARAMS
	#the only parameter you need to pass is the URL of the firebase link
	def queryModel(self, URL):
                t1=0.3
                t2=0.6
                t3=0.8
                path=self.getImage(URL)
                if not path is 'download_error' and not path is 'save_error':
                        data=classify('file', path)
                        os.remove(path)
                        #using the data returned by the model, select the top 5 results and package them into dictionary

                        i=0
                        for index,row in data.iterrows():
                                if i==0:
					p1=row['prob']
					b1=row['breed']
				elif i==1:
					p2=row['prob']
				i+=1

			prob=p1
			#if top prob is below threshold, return unknown
			if p1 < t1:
				breed = 'Model cannot identify the breed'
			#else check to make sure they are sufficiently far apart
			else:
				dif=p1-p2
				if dif<0.2:
					breed = 'Model cannot identify the breed'
				else:
					breed = b1
			return breed,prob
                else:
                        return 'download_error'
	
	def getImage(self, URL):
		r = requests.get(URL, allow_redirects=True)
		random.seed(datetime.now())
		rand=random.randint(0,2147483647)
		path=str(rand)+'.jpg'
		open(path, 'wb').write(r.content)
		return path
