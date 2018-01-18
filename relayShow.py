import RPi.GPIO as GPIO
import time
import sys

R1 = 21
R2 = 20
R3 = 16
R4 = 26
R5 = 6
R6 = 13
R7 = 12
R8 = 5
R9 = 19
R10 = 22
R11 = 17
R12 = 24
R13 = 27
R14 = 23
R15 = 4
R16 = 25

relays = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16]
def main():
	for relay in relays:
		off(relay)
	for relay in relays:
		on(relay)
		time.sleep(0.1)
	for relay in relays:
		off(relay)
		time.sleep(0.1)
	time.sleep(0.1)
	return 0


def on(target):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(target, GPIO.OUT)
	GPIO.output(target, GPIO.HIGH)

def off(target):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(target, GPIO.IN)
	

main()
