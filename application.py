from flask import Flask
from flask import request

application = Flask(__name__)

#routing rule and logic of breedSearch
#currently it just extracts URL from data section and sends the URL back to sender
#test Success case: you post with URL in body, and get that same URL back
@application.route('/breedSearch',methods=['POST'])
def breedSearch():
    URL=request.form.keys()[0]#this line may change based on exactly how the incoming format is    
    #TODO get img from url
    #TODO query model with img
    return '{URL : %s}' % URL
    # return '{BREED : %s' % search_result

# routing rule and logic for wiki search
application.add_url_rule('/getWikiInfo/<breed>','wiki',(lambda breed: getWikiInfo(breed)))
def getWikiInfo(breed):
    #TODO wiki API get first 1 or 2 paragraphs from wiki
    #TODO package to send
    return '{breed: %s}' % breed
    # return '{results: %s}' % formatted_results

#routing and logic for petfinder search
#requires breed name, and lat/longitude(or city state? doesnt matter atm)
application.add_url_rule('/getPFinfo/<breed>/<lat>/<long>','pf',(lambda breed,lat,long: get_PFinfo(breed,lat,long)))
def get_PFinfo(breed='null',lat='null', long='null'):
    #TODO petfinder API to pull search results
    #TODO package to send
    return '{breed: %s , lat: %s, long: %s}'% (breed,lat,long)
    # return '{results: %s}' % formatted_results

#routing rule and logic for home page
#TODO get web_squad html's, should return their landing page
application.add_url_rule('/', 'index', (lambda: homePage()))   
def homePage(username = "World"):
    return 'TODO homepage'
    # return render_template('index.html')


if __name__ == "__main__":
    application.debug = True
    application.run()
