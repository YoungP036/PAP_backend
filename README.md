# Pic-a-Pup Backend Server

This server is was implemented for an Ubuntu 16.04.04 LTS system. We used an AWS EC2 instance.
We implement using a Flask, Uwsbi, and Nginx stack. The language we choose is Python 2.7.12. 
All python dependencies are enumerated in the requirements.txt file.

## Features

	The job of this server is to service requests from clients sent using HTTP POST. When it receives
	an image URL, it will download the image from that URL and send it through our dog breed identifier 
	AI. If the AI returns a dog breed with high enough confidence the server will then query wikipedia
	to get some basic information on that breed. Finally it will query PetFinder in order to find an 
	available dog of that breed in the nearby area. That data will then be encapsulated into one JSON 
	object and returned to the client.

## Installation

	1. git clone http://github.com/YoungP036/PAP_backend.git
	2. sudo apt-get install python python-pip nginx-full uwsgi
	3. cd /path/to/PAP_backend	
	4. sudo pip install -r requirements.txt
	5. sudo pip install petfinder wikipedia flask flask_cors

## Start Server

	1. cd /path/to/PAP_backend
	2. service nginx restart
	3. uwsgi uwsgi.ini
	4. cat *.log and examine the most recent entries to verify proper server startup

## Stop Server

	1. cd /path/to/PAP_backend
	2. uwsgi --stop app.pid
	3. fuser -k 3033/tcp

## Server Requests

	Requests from clients to this server should be made using HTTP POST. In the data section should be two 
	key-value pairs, 'url':'www.website.com' and 'location':'<zipcode>'. The URL must be to an image file 
	of type png or jpg. In response the server will send a JSON object with a subset of the following keys, 
	'breed', 'prob', 'contact', 'name', 'sex', 'age', 'size', 'shelter_contact', 'photos', 'breed_info',
	'petfinder_error', 'model_error', 'wikipedia_error', and 'server_error'.
