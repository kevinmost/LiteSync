from flask import Flask, render_template
import datetime
import traceback
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

@app.route("/readPin/<int:pin>")
def readPin(pin):
   try:
      GPIO.setup(pin, GPIO.IN)
      if GPIO.input(pin) == True:
         return "Pin " + str(pin) + " is high"
         # response = "Pin number " + pin + " is high!"
      else:
         return "Pin " + str(pin) + " is low"
         # response = "Pin number " + pin + " is low!"
   except:
      traceback.print_exc()
      return "There was an error reading pin" + str(pin)
      #response = "There was an error reading pin " + pin + "."

   #templateData = {
   #   'title' : 'Status of Pin' + pin,
   #   'response' : response
   #   }

   #return render_template('pin.html', **templateData)
   return 0

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
