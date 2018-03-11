# Blinds

Project Folder for the Blinds sub component

## Setup
1. Clone this repo onto local machine
```
git clone git@github.com:nickkoul/pi_guy.git
```
2. Setup SSH on your Raspberry Pi
```
sudo raspi-config
```
Navigate through the menu and enable SSH access

3. Get IP address for the Pi by running this command on it
```
hostname -I
```
You should be looking for an address along the lines of 10.x.x.x or 192.x.x.x, it should be the first thing printed out to the console

4. Copy the blinds directory from your local machine to your Raspberry Pi
```
sshpass -p <pi password> scp -r pi_guy/blinds/ <pi username>@<pi IP address>:/home/<pi username>
```

5. Run the following commands to get the needed packages for your pi
```
sudo apt-get update
sudo apt-get install python-pip
sudo pip install Flask
```

## Deployment
1. Set Flask env variable
```
export FLASK_APP=blinds.py
```

2. Run Flask Server
```
flask run --host=0.0.0.0
```
