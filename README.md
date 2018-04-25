This server is was implemented for an Ubuntu or Ubuntu based linux environment. 

Installation

	1. git clone http://github.com/YoungP036/PAP_backend.git
	2. cd PAP_backend
	3. sudo pip install -r requirements.txt
	4. sudo apt-get install nginx-full uwsgi

Start Server

	1. cd /path/to/PAP_backend
	2. service nginx restart
	3. uwsgi uwsgi.ini
	4. cat *.log and examine the most recent entries to verify proper server startup

Stop Server

	1. cd /path/to/PAP_backend
	2. uwsgi --stop app.pid
	3. fuser -k 3033/tcp
