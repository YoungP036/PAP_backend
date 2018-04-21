import petfinder


class pManager:
        # Instantiate the client with your credentials.
        def queryPetFinder(self,breed,location):
            try:
                api = petfinder.PetFinderClient(api_key='90999df88cd81af6e271a7a661ee5bf6', api_secret='57d9d3da742d84021f892c623667db77')
                found = 0
                 # Search for pets.
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

                    return  pet['name'],pet['contact'],pet['sex'],pet['size'],pet['age'],pet['photos']
            except Exception as e:
                    return str(e) 
