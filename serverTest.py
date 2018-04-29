import requests

count = 0
while (count < 100):
      r = requests.post("http://18.188.145.20", data={'location': 19104, 'url':'http://photos.petfinder.com/photos/pets/40708150/1/?bust=1516322759&width=500&-x.jpg'})
      print(r.status_code, r.reason,count)
      count = count + 1
print("Good bye")
