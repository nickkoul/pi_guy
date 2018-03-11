import RPi.GPIO as GPIO
import time
import flask

app = flask.Flask(__name__)

#Clockwise ~3.75 X deg/ms
#Stop ~7.1
#CounterClockwsie ~11.25
# 1.18s per revolution going clockwise, 1.18/360 = 0.00327s/deg

@app.route('/')
def hello_world():
    return 'Hello World'
@app.route('/blinds/')
@app.route('/blinds/<int:next_pos>')
def rotate_to(next_pos=0):
    if next_pos<0 or next_pos>180:
        content = "Error, Next Position must be between 0 and 180"
        return flask.make_response((content,400))

    status_file = open("status.txt", "r")
    cur_pos = int(status_file.read())
    status_file.close()

    angle_diff = next_pos - cur_pos # if cur_pos > next_pos we move counter clockwise (negative)
    print("Current Position: %d Goal Position: %d Delta: %d" %(cur_pos, next_pos, angle_diff) )

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12, 50)

    pulsewidth = 11.25
    rot_speed = 0.00320
    if angle_diff > 0:
        pulsewidth = 3.75

    rotation_time = abs(angle_diff) * rot_speed
    p.start(pulsewidth)

    time.sleep(rotation_time)

    p.stop()
    GPIO.cleanup()

    status_file = open("status.txt", "w")
    status_file.write(str(next_pos))
    status_file.close()

    return flask.make_response(("",200))
