import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

led = 12
trigpin = 11
echopin = 7

GPIO.setup(trigpin, GPIO.OUT)
GPIO.setup(echopin, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 100)
pwm.start(0)

def dist():
    
    GPIO.output(trigpin, GPIO.HIGH) 
    time.sleep(0.0001) 
    GPIO.output(trigpin, GPIO.LOW)
    
    
    while GPIO.input(echopin) == 0:
        start = time.time()
        
    while GPIO.input(echopin) == 1:
        stop = time.time()

    totalTime = stop - start
    
    dist = (totalTime * 34300) / 2
    
    return dist


while True:
    distance = dist()
    if (distance <= 50):
        pwm.ChangeDutyCycle(50 - distance)
        time.sleep(0.5)
        
    else :
        pwm.ChangeDutyCycle(0)
    time.sleep(0.001)
        
