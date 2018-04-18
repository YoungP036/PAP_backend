import wikipedia


class WikiSearch():
           def  __init__(self,breed):
	        self.breed = breed


           def wikiSearch:
               try:
		  search = wikipedia.summary(breed)
               except Excpetion:
                     return "wiki_failed"


           return search


