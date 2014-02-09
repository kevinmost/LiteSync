from flask import Flask
import RPi.GPIO as GPIO
app = Flask(__name__)


@app.route("/")
def hello():
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18, False)
	time.sleep(2)
	GPIO.output(18, True)
	time.sleep(2)
	return "Welcome to LiteSync!"

if __name__ == "__main__":
	app.run()