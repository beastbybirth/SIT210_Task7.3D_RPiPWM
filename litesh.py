import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)    #setting BOARD as pin numbering system

#declaring all the pins
led = 12
trigpin = 11
echopin = 7

GPIO.setup(trigpin, GPIO.OUT)   #setting trig pins to output
GPIO.setup(echopin, GPIO.IN)    #setting echo pin to input
GPIO.setup(led, GPIO.OUT)       #initialising the led

pwm = GPIO.PWM(led, 100)    #setting up the instance for pwm
pwm.start(0)

def dist():     #function to calculate the distance
    GPIO.output(trigpin, GPIO.HIGH) 
    time.sleep(0.0001) 
    GPIO.output(trigpin, GPIO.LOW)
    
    
    while GPIO.input(echopin) == 0:
        start = time.time()
        
    while GPIO.input(echopin) == 1:
        stop = time.time()

    totalTime = stop - start        #calculating total time
    
    dist = (totalTime * 34300) / 2  #calculating distance
    
    return dist


while True:
    distance = dist()
    if (distance <= 50):
        pwm.ChangeDutyCycle(50 - distance)  #changing the brightness of led according to distance
        time.sleep(0.5)
        
    else :
        pwm.ChangeDutyCycle(0)      #else turn off the led
    time.sleep(0.001)
        
