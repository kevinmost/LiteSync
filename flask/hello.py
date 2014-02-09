from flask import Flask, render_template
import datetime
import traceback
import time
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : 'HELLO!',
        'time': timeString
        }
    # return render_template('main.html', **templateData)
    return "dicks"
@app.route("/timer/<int:seconds>/<int:pin>")
def timer(seconds, pin):
    time.sleep(seconds)
    changePinStatus(pin)
    return "Pin " + str(pin) + " changed"

@app.route("/sense/<int:threshold>")
def sense(threshold):
    level = readPin(12) + (2 * readPin(16)) + (4 * readPin(18))
    GPIO.setup(19, GPIO.OUT)
    if (level > threshold and threshold <= 7 and threshold >= 0):
        GPIO.output(19, True)
        return "Threshold was " + str(threshold) + ". Level detected was " + str(level) + "."
    else:
        GPIO.output(19, False)
        return "No stop pls"

@app.route("/changePinStatus/<int:pin>", methods=['GET', 'POST'])
def changePinStatus(pin):
    try:
        GPIO.setup(pin, GPIO.IN)
        response = GPIO.input(pin)
        GPIO.setup(pin, GPIO.OUT)
        if  response == True:
            GPIO.output(pin, False)
            newResponse = False
        elif response == False:
            GPIO.output(pin, True)
            newResponse = True
    except:
        return "It didn't work"

    templateData = {
        'title' : 'Status of Pin ' + str(pin),
        'response' : newResponse
    }
    return render_template('pin.html', **templateData)

@app.route("/readPin/<int:pin>")
def readPin():
    try:
        GPIO.setup(pin, GPIO.IN)
        return int(GPIO.input(pin))

@app.route("/readPinDebug/all")
def readPinAllDebug():
    pin_statuses = ""
    for pin in range(1,26):
        GPIO.setup(pin, GPIO.IN)
        pin_statuses += "Pin " + str(pin) + " is " + str(GPIO.input(pin))
    return pin_statuses

@app.route("/readPinDebug/<int:pin>")
def readPinDebug(pin):
    try:
        GPIO.setup(pin, GPIO.IN)
        if GPIO.input(pin) == True:
            response = "Pin number " + str(pin) + " is high!"
        else:
            response = "Pin number " + str(pin) + " is low!"
    except:
            response = "There was an error reading pin " + str(pin) + "."

    templateData = {
        'title' : 'Status of Pin ' + str(pin),
        'response' : response,
        'pinURL' : "/changePinStatus/" + str(pin)
        }

    return render_template('pin.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
