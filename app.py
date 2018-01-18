#!flask/bin/python
from flask import Flask
import RPi.GPIO as GPIO
from flask_cors import CORS

	
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/on/<int:relay_id>')
def relay_on(relay_id):
	on(map_GPIO(relay_id))
	return str(GPIO.gpio_function(map_GPIO(relay_id)) == GPIO.OUT)

@app.route('/off/<int:relay_id>')
def relay_off(relay_id):
	off(map_GPIO(relay_id))
	return str(GPIO.gpio_function(map_GPIO(relay_id)) == GPIO.IN)

def on(target):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(target, GPIO.OUT)
	GPIO.output(target, GPIO.HIGH)

def off(target):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(target, GPIO.IN)

def map_GPIO(target):
	if (target == 1): return 21
	elif (target == 2): return 20
	elif (target == 3): return 16
	elif (target == 4): return 26
	elif (target == 5): return 6
	elif (target == 6): return 13
	elif (target == 7): return 12
	elif (target == 8): return 5
	elif (target == 9): return 19
	elif (target == 10): return 22
	elif (target == 11): return 17
	elif (target == 12): return 24
	elif (target == 13): return 27
	elif (target == 14): return 23
	elif (target == 15): return 4
	elif (target == 16): return 25
	else: return 0

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("35"), debug=True)
