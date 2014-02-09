from flask import Flask, render_template, request
import datetime
import traceback
import time
import RPi.GPIO as GPIO
app = Flask(__name__)

def pinout_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(18, GPIO.IN)
    GPIO.setup(21, GPIO.IN)
    GPIO.setup(22, GPIO.OUT)
    global pinout_state
    if pinout_state is None:
        pinout_state = False


@app.route("/")
def hello():
    templateData = {
        'timeDependentURL' : '/'
    }
    # return render_template('main.html', **templateData)
    return render_template('mainMenu.html', **templateData)

@app.route("/timer", methods=['GET', 'POST']) #Time-dependent
def timer():
    pinout_init()
    time.sleep(float(request.form['time']))
    changePin()
    return "Pin changed"

def changePin():
    pinout_init()
    pinout_state = not pinout_state
    GPIO.output(22, pinout_state)

@app.route("/sense", methods=['GET', 'POST']) #Light-dependent
def sense():
    pinout_init()
    threshold = int(request.form['threshold'])
    level = GPIO.input(17) + (2 * GPIO.input(18)) + (4 * GPIO.input(21))
    if (level > threshold and threshold <= 7 and threshold >= 0):
        pinout_state = True
    else:
        pinout_state = False
    GPIO.output(22, pinout_state)
    templateData = {
        'pinout_state': pinout_state
    }
    return render_template('pinStatus.html', **templateData)

@app.route("/readPin")
def readPin():
    pinout_init()
    return "Pin 17: " + str(GPIO.input(17)) + ". Pin 18: " + str(GPIO.input(18)) + ". Pin 21: " + str(GPIO.input(21))

    # templateData = {
    #     'title' : 'Status of Pin ' + str(pin),
    #     'response' : response,
    #     'pinURL' : "/changePinStatus/" + str(pin)
    #     }

    # return render_template('pin.html', **templateData)

if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0', port=5000, debug=True)
