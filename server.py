from flask import Flask
from flask import request
from API.petfinderManager import pfManager
from model.ModelManager import mManager
#breedSearch POST test, curl --data "www.imgurl.io/img" 127.0.0.1:5000/breedSearch
    #should return www.imgurl.io/img" to client, in the future it would be a breed string
#wikiInfo GET test, curl 127.0.0.1:5000/getWikiInfo/labrador
    #should return {breed: labrador} to client, in the future it would be a buncha wiki info
#get_PFinfo GET test, curl 127.0.1:5000/getPFinfo/lab/100/200
    #should return {breed: lab, lat:100, long:200} to client. in the future it would be some json list or something

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
    #TODO wiki API get first 1 or 2 paragraphs from wiki
    #TODO package to send
    return '{breed: %s}' % breed
    # return '{results: %s}' % formatted_results

#routing and logic for petfinder search
#requires breed name, and lat/longitude(or city state? doesnt matter atm)
application.add_url_rule('/getPFinfo/<breed>/<zipcode>','pf',(lambda breed,zipcode: get_PFinfo(breed,zipcode)))
def get_PFinfo(breed='null',zipcode='null'):
    return pfManager().getPFData(breed,zipcode)

#routing rule and logic for home page
#TODO get web_squad html's, should return their landing page
application.add_url_rule('/', 'index', (lambda: homePage()))   
def homePage(username = "World"):
    return 'TODO homepage'

if __name__ == "__main__":
    application.debug = True
    application.run()
