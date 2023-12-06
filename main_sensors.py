#!/usr/bin/python

# uv sensors, moisture sensor, switch
# also buzze to detect fall

import RPi.GPIO as GPIO     # Library for accessing and controlling the GPIO pins on the Raspberry Pi
import time                 # Time-related functions
import spidev               # SPI (Serial Peripheral Interface) library
import serial               # Library for serial communication
import os                   # Operating system interface
##import geocoder
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=5000

import telepot              # Library for interacting with the Telegram Bot API
def sendmsg(msg):
    bot = telepot.Bot('6516924339:AAFOkmetiNAMLwiaJE6hER1VGAik_m6w5o0')
    bot.sendMessage('6940845171', str(msg))

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 20
GPIO_ECHO = 21


GPIO_TRIGGER1 = 26
GPIO_ECHO1 = 19


GPIO_TRIGGER2 = 13
GPIO_ECHO2 = 6

moisture = 4
buzzer=25
switch = 3


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)


GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)


GPIO.setup(moisture,GPIO.IN)
GPIO.setup(switch,GPIO.IN)

GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer, False)



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)



# this function uses UV Sensors to measure distance
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save ArrivalTime
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

# same as distance function
def distance1():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER1, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime = time.time()
 
    # save ArrivalTime
    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance1 = (TimeElapsed * 34300) / 2
 
    return distance1

# same as distance function
def distance2():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER2, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER2, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO2) == 0:
        StartTime = time.time()
 
    # save ArrivalTime
    while GPIO.input(GPIO_ECHO2) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance2 = (TimeElapsed * 34300) / 2
 
    return distance2


# these functions take input from ADC Sensors and convert it to Volts and Temperature
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
 
# Function to calculate temperature from
# TMP36 data, rounded to specified
# number of decimal places.
def ConvertTemp(data,places):
 
  # ADC Value
  # (approx)  Temp  Volts
  #    0      -50    0.00
  #   78      -25    0.25
  #  155        0    0.50
  #  233       25    0.75
  #  310       50    1.00
  #  465      100    1.50
  #  775      200    2.50
  # 1023      280    3.30
 
  temp = ((data * 330)/float(1023))-8 #40
  temp = round(temp,places)
  return temp


##
##GPIO.output(relay,0)
count=0

'''
The main loop continuously reads data from sensors, checks distances, and performs actions based on sensor readings.
--------------------------------------------------
-> The X and Y levels are read from the ADC, converted to volts, and printed.
-> Distances are measured using ultrasonic sensors, and if they are below a certain threshold, audio alerts are played.
-> If the X or Y levels fall outside a certain range, indicating a person falling down, a message is sent via Telegram, and a buzzer is activated.
-> If the moisture sensor detects moisture or the switch is activated, corresponding audio alerts are played.
-------------------------------------------------
'''

while True:
    
    X_level = ReadChannel(0)
    X_volts = ConvertVolts(X_level,2)

    Y_level = ReadChannel(1)
    Y_volts = ConvertVolts( Y_level,2)

##    Y_level = ReadChannel(1)
##    Y_volts = ConvertVolts(,2)



 

    print ("--------------------------------------------")

    print("X: {}".format(X_level))
    print("Y: {}".format(Y_level))
 


       

    dist = distance()
    print ("Measured Distance at left= %.1f cm" % dist)
    time.sleep(0.1)

    if dist < 20:
        print('left object detected ')
        os.system("mpg321 ls.mp3")


    dist1 = distance1()
    print ("Measured Distance at right = %.1f cm" % dist1)
    time.sleep(0.1)

    if dist1 < 20:
        print('right object detected ')
        os.system("mpg321 rs.mp3")

        
    dist2 = distance2()
    print ("Measured Distance at front = %.1f cm" % dist2)
    time.sleep(0.1)


    if dist2 < 20:
        print('front object detected ')
        os.system("mpg321 fs.mp3")
        
        
    print ("--------------------------------------------")
    time.sleep(1)

    if((X_level>380)or(X_level<300)):
      print('PERSON FELL DOWN')
      GPIO.output(buzzer, True)
      sendmsg('PERSON FELL DOWN at http://www.google.com/maps/?q={},{}'.format('13.0850','77.4844'))
      time.sleep(2)
      GPIO.output(buzzer, False)

    if((Y_level>380)or(Y_level<300)):
      print('PERSON IS FALL DOWN ')
      GPIO.output(buzzer, True)
      sendmsg('PERSON IS FALL DOWN at http://www.google.com/maps/?q={},{}'.format('13.0850','77.4844'))
      time.sleep(2)
      GPIO.output(buzzer, False)
        
    if(GPIO.input(moisture)==False):
        os.system("mpg321 mos.mp3")
        print('Moisture detected')

    if(GPIO.input(switch)==False):
        os.system("mpg321 e.mp3")
        print('Emergency detected')
        GPIO.output(buzzer, True)
        sendmsg('PERSON IS IN EMERGENCY at http://www.google.com/maps/?q={},{}'.format('13.0850','77.4844'))
        time.sleep(2)
        GPIO.output(buzzer, False)

##
