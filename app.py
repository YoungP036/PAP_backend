
from flask import Flask
from flask import request
import urllib
from flask_restful import Resource, Api, reqparse
import wikipedia
import petfinder
import requests
from flask_cors import CORS
from model.ModelManager import mManager
from pet import pManager
import json
#

app = Flask(__name__)
api = Api(app)
CORS(app)
	
class getJson(Resource):
    def post(self):
        try:
            # Instantiate the client with your credentials.
            api = petfinder.PetFinderClient(api_key='90999df88cd81af6e271a7a661ee5bf6', api_secret='57d9d3da742d84021f892c623667db77')
            data = {}
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('url', type=str)
	   #parser.add_argument('breed', type=str)
	    parser.add_argument('location', type=str)	

	    #get args in memory
            args = parser.parse_args()
	    url= args['url']
	    location = args['location']

	    #query model
	    result,prob=mManager().queryModel(url)
            if result  ==  'Model cannot identify the breed':
                     data['model_error'] = 'Model cannot identify the breed'
                     return data

	    #format the way wiki wants
            if '_' in result:
               breed = result.replace("_"," ").title()
            else:
               breed = result.title()
            
            # Search Wikipedia for info
            try:
	        search = wikipedia.summary(breed, sentences =5)
            except Exception:
                   data['breed'] = breed
		   data['prob'] = prob
                   data['wikipedia_error'] = 'cannot find info about ' + breed
                   return data

            # search for pets
            try:
                found = 0
                for pet in api.pet_find(
                    animal="dog", location=location, output="basic",
                    breed=breed, count=4,
                ):
                    contact = pet['contact']
                    for key,val in contact.items():
                        if key == 'address1':
                           if val != None:
                              found = 1
                              break
                    if found == 1:
                       break

                data['name'] = pet['name']
                data['sex'] = pet['sex']
                data['age'] = pet['age']
                data['size'] = pet['size']
                data['shelter_contact'] = pet['contact']
                data['photos'] = pet['photos']
                data['breed'] = breed
                data['prob'] = prob 
                data['breed_info'] = search
                return data
            except Exception as e:
                   data['breed'] = breed
		   data['prob'] = prob
                   data['breed_info'] = search
                   data['petfinder_error'] = str(e)
                   return data

            # Package Info in dict/json object
            #data['breed'] = breed
            #data['prob'] = prob 
            #data['name'] = pet['name']
            #data['sex'] = pet['sex']
            #data['age'] = pet['age']	
            #data['size'] = pet['size']     
            #data['breed_info'] = search
            #data['shelter_contact'] = pet['contact']
            #data['photos'] = pet['photos']
         
            #return data

        except Exception as e:
            return {'error': str(e)}

api.add_resource(getJson, '/')
	
		

if __name__ == "__main__":
    app.run(host='0.0.0.0')

