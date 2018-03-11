from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/blinds/')
@app.route('/blinds/<int:angle>')
def change_blinds(angle=0):
    return "Rotate Blinds %d Degrees" %(angle)
