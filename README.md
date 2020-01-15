# Lightstick
This is a partially complete solution to drive dotstar LED strips from MIDI data.  Much of this code was tested and fixed on a stage between rehearsals.  It works, but can be a little buggy.

## Installation
The installation is fairly similar to micboard.


Install git, python3-pip, and Node.js
```
$ sudo apt-get update
$ sudo apt-get install git python3-pip
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install nodejs
```

Download lightstick
```
$ git clone https://github.com/karlcswanson/lightstick.git
```

Install lightstick software dependencies via npm and pip
```
$ cd lightstick/
$ npm install --only=prod
$ pip3 install -r py/requirements.txt
```

build the lightstick frontend and run lightstick
```
$ npm run build
$ python3 py/lightstick.py
```

Edit `User` and `WorkingDirectory` within `lightstick.service` to match your installation and install it as a service.
```
$ sudo cp lightstick.service /etc/systemd/system/
$ sudo systemctl start lightstick.service
$ sudo systemctl enable lightstick.service
```
