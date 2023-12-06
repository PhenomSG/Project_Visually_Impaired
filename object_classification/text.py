#!/usr/bin/env python
import numpy as np
import sys
import cv2
import os

from gtts import gTTS
import os

print ("Enter the Text :")
#str=input()
str=input()
print (str)
#while True:
    
#mtext = 'welcome to india welcome to india welcome to india '
lag = 'en'
myobj = gTTS(text=str, lang=lag, slow =False)
myobj.save("test.mp3")
os.system("mpg321 test.mp3")
