
from flask import Flask
from flask import request
import urllib
from flask_restful import Resource, Api, reqparse
import wikipedia
import petfinder
import requests
from flask_cors import CORS
from model.ModelManager import mManager
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
            args = parser.parse_args()
	    url= args['url']
	    location = args['location']
	    result=mManager().queryModel(url)
            if result  ==  'Model cannot identify the breed':
                     data['model_error'] = 'Model cannot identify the breed'
                     return data
            if '_' in result:
               breed = result.replace("_"," ").title()
            else:
               breed = result.title()
	    #breed = args['breed']
            # Download the image from the url
            #urllib.urlretrieve(url,"image.png")
            
            # Search Wikipedia for info
            try:
	        search = wikipedia.summary(breed, sentences =5)
            except Exception:
                   data['breed'] = breed
                   data['wikipedia_error'] = 'cannot find info about ' + breed
                   return data
            # search for pets
            try:
 	       pet = api.pet_getrandom(animal="dog", location=location,breed=breed, output = "basic")
            except Exception:
                   data['breed'] = breed
                   data['breed_info'] = search
                   data['petfinder_error'] = 'Cannot find a similar dog for adoption'
                   return data

            # Package Info in dict/json object
  	       
            
            data['breed'] = breed
            data['name'] = pet['name']
	    data['shelterId'] = pet['shelterId']
            data['sex'] = pet['sex']
            data['age'] = pet['age']	
            data['size'] = pet['size']     
            data['breed_info'] = search
            data['shelter Contact'] = pet['contact']
            data['photos'] = pet['photos']
         
            return data

        except Exception as e:
            return {'error': str(e)}

api.add_resource(getJson, '/')
	
		

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

