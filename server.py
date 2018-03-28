from flask import Flask
from model.ModelManager import mManager

application = Flask(__name__)

#routing rule and logic of breedSearch
@application.route('/breedSearch',methods=['POST'])
def breedSearch():
    URL=request.form['URL']
    results=mManager().queryModel(URL)
    print("Breed search activated!")
    return results

# routing rule and logic for wiki search
application.add_url_rule('/getWikiInfo/<breed>','wiki',(lambda breed: getWikiInfo(breed)))
def getWikiInfo(breed):
    return '{breed: %s}' % breed

#routing and logic for petfinder search
#requires breed name, and lat/longitude(or city state? doesnt matter atm)
application.add_url_rule('/getPFinfo/<breed>/<zipcode>','pf',(lambda breed,zipcode: get_PFinfo(breed,zipcode)))
def get_PFinfo(breed='null',zipcode='null'):
    return pfManager().getPFData(breed,zipcode)

#routing rule and logic for home page
application.add_url_rule('/', 'index', (lambda: homePage()))   
def homePage(username = "World"):
    return 'TODO homepage'

if __name__ == "__main__":
    application.debug = True
    application.run()
