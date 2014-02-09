from flask import Flask
import RPi.GPIO as GPIO
app = Flask(__name__)

@app.route("/")
def hello():
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18, False)
    return "Hello World!"

if __name__ == "__main__":
    app.run()