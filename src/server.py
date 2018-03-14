from flask import Flask
from flask import request

#GET IMAGE FROM URL
# import requests
# url = 'http://google.com/favicon.ico'
# r = requests.get(url, allow_redirects=True)
# open('google.ico', 'wb').write(r.content)

#breedSearch POST test, curl --data "www.imgurl.io/img" 127.0.0.1:5000/breedSearch
    #should return www.imgurl.io/img" to client, in the future it would be a breed string
#wikiInfo GET test, curl 127.0.0.1:5000/getWikiInfo/labrador
    #should return {breed: labrador} to client, in the future it would be a buncha wiki info
#get_PFinfo GET test, curl 127.0.1:5000/getPFinfo/lab/100/200
    #should return {breed: lab, lat:100, long:200} to client. in the future it would be some json list or something

application = Flask(__name__)

#routing rule and logic of breedSearch
#currently it just extracts URL from data section and sends the URL back to sender
#test Success case: you post with URL in body, and get that same URL back
@application.route('/breedSearch',methods=['POST'])
def breedSearch():
	print("req.form: " + str(request.form['URL']))
	URL=request.form['URL']
	#TODO get img from url
	#TODO get wiki
	#TODO maybe petfinder
	#TODO query model with img
	print("Breed search activated!")
	# dbg='{URL : %s}' % URL
	# print(dbg)
	return '{URL : %s}' % URL

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
