from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/blinds/')
@app.route('/blinds/<int:angle>')
def change_blinds(angle=0):
    url = "http://10.0.0.130:5000/blinds/" + str(angle)
    response = requests.get(url)
    print(response)
    return url
