import petfinder

# Instantiate the client with your credentials.
api = petfinder.PetFinderClient(api_key='90999df88cd81af6e271a7a661ee5bf6', api_secret='57d9d3da742d84021f892c623667db77')

# Query away!
#for shelter in api.shelter_find(location='30127', count=500):
 #   print(shelter['name'])

found = 0
# Search for pets.
for pet in api.pet_find(
    animal="dog", location="19426", output="basic",
    breed="Beagle", count=4,
):
   
    contact = pet['contact']
    for key,val in contact.items():
        if key == 'address1':
           if val != None:
              found = 1
              break    
    if found == 1:
       print("%s - %s - %s - %s - %s" % (pet['id'], pet['name'],pet['contact'], pet['sex'],pet['size']))	
       break



    print("%s - %s - %s - %s - %s" % (pet['id'], pet['name'],pet['contact'], pet['sex'],pet['size']))
