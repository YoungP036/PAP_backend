import requests
import json

BASEURL='http://api.petfinder.com/'
KEY='d896a17263ea414415a2a31005dc808b'
class pfManager:
	
	def getPFData(self,breed='null',zip=0):
		if breed is 'null' or zip==0:
			return
		#get supported breed list
		targetURL=self.buildURL('getBreeds',['dog'] )
		print(targetURL)
		raw_breeds=requests.get(targetURL).json()['petfinder']['breeds']['breed']

		found_flag=False
		for x in raw_breeds:
			if breed == x['$t']:
				found_flag=True
			
		if found_flag is False:
			print("DBG breed unknown")
			return
		print("DBG: breed exists")

		# targetURL=self.buildURL('findShelterPet',['dog',breed,str(zip)])
		targetURL=self.buildURL('findPet',['dog',breed,str(zip)])
		print("targetURL: " + targetURL)
		data=requests.get(targetURL).json()['petfinder']
		print(json.dumps(data))
		# for x in data:
			# print(x)
		return json.dumps(data)

	def buildURL(self,request, args=None):
		#builds for retrieving breed list
		if request is 'getBreeds':
			return BASEURL+"breed.list?key=" +KEY+ "&animal=" +args[0]+ "&format=json"
		#builds for retrieving shelter info
		elif request is 'findShelterPet':
			print("searching for %s in %s",args[1],args[2])
			return BASEURL+"shelter.listByBreed?key=" +KEY+ "&animal=" +args[0]+ "&breed=" +args[1]+ "&location=" +args[2]+"&format=json"
		elif request is 'findPet':
			return BASEURL+"pet.find?key=" +KEY+ "&animal=" +args[0]+ "&breed=" +args[1]+ "&location=" +args[2]+ "&format=json"
