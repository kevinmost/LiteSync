from flask import Flask, render_template
import datetime
import traceback
import time
import RPi.GPIO as GPIO
app = Flask(__name__)

pinout_state = False

def dicks():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(18, GPIO.IN)
    GPIO.setup(21, GPIO.IN)
    GPIO.setup(22, GPIO.OUT)


@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : 'HELLO!',
        'time': timeString
    }
    # return render_template('main.html', **templateData)
    return "LiteSync"

@app.route("/thresholdLoop/<int:threshold>")
def thresholdLoop(thresholdLoop):
    dicks()
    while(True):
        sense(threshold)

@app.route("/timer/<int:seconds>")
def timer(seconds):
    dicks()
    time.sleep(seconds)
    changePin()
    return "Pin " + str(pin) + " changed"
def changePin():
    dicks()
    global pinout_state = not global pinout_state
    GPIO.output(22, global pinout_state)

@app.route("/sense/<int:threshold>")
def sense(threshold):
    dicks()
    level = GPIO.input(12) + (2 * GPIO.input(16)) + (4 * GPIO.input(18))
    if (level > threshold and threshold <= 7 and threshold >= 0):
        global pinout_state = True
    else:
        global pinout_state = False
    GPIO.output(22, global pinout_state)
    return "Threshold was " + str(threshold) + ". Level detected was " + str(level) + "."

@app.route("/readPin")
def readPin():
    dicks()
    return "Pin 17: " + str(GPIO.input(17)) + ". Pin 18: " + str(GPIO.input(18)) + ". Pin 21: " + str(GPIO.input(21))

    # templateData = {
    #     'title' : 'Status of Pin ' + str(pin),
    #     'response' : response,
    #     'pinURL' : "/changePinStatus/" + str(pin)
    #     }

    # return render_template('pin.html', **templateData)

if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0', port=5000, debug=True)
