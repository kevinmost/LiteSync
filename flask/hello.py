from flask import Flask, render_template
import datetime
import traceback
import time
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.set(12, GPIO.IN)
GPIO.set(16, GPIO.IN)
GPIO.set(18, GPIO.IN)
GPIO.set(19, GPIO.OUT)

pin_19_state=False

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

@app.route("/tresholdLoop/<int:threshold>")
def thresholdLoop(tresholdLoop):
    while(True):
        sense(threshold)

@app.route("/timer/<int:seconds>")
def timer(seconds):
    time.sleep(seconds)
    changePin()
    return "Pin " + str(pin) + " changed"
def changePin():
    pin_19_state = not pin_19_state
    GPIO.output(19, pin_19_state)

@app.route("/sense/<int:threshold>")
def sense(threshold):
    level = GPIO.input(12) + (2 * GPIO.input(16)) + (4 * GPIO.input(18))
    if (level > threshold and threshold <= 7 and threshold >= 0):
        pin_19_state = True
    else:
        pin_19_state = False
    GPIO.output(19, pin_19_state)
    return "Threshold was " + str(threshold) + ". Level detected was " + str(level) + "."

@app.route("/readPin")
def readPin():
    return "Pin 12: " + str(GPIO.input(12)) + ". Pin 16: " + str(GPIO.input(16)) + ". Pin 18: " + str(GPIO.input(18))

    # templateData = {
    #     'title' : 'Status of Pin ' + str(pin),
    #     'response' : response,
    #     'pinURL' : "/changePinStatus/" + str(pin)
    #     }

    # return render_template('pin.html', **templateData)

if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0', port=5000, debug=True)
