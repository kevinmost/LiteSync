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
    return ""

@app.route("/changePinStatus/<int:pin>")
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
        return "fuck you"

    templateData = {
        'title' : 'Status of Pin ' + str(pin),
        'response' : newResponse
    }
    return render_template('pin.html', **templateData)

@app.route("/readPin/all")
def readPinAll():
    pin_statuses = ""
    for pin in range(1,26):
        GPIO.setup(pin, GPIO.IN)
        pin_statuses += "Pin " + str(pin) + " is " + str(GPIO.input(pin))
    return pin_statuses

@app.route("/readPin/<int:pin>")
def readPin(pin):
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
        'response' : response
        }

    return render_template('pin.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
