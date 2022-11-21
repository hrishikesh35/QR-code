import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import pybase64

#  START

cap = cv2.VideoCapture(0)

names = []

# FUNCTION FOR ATTENDANCE

fob = open('attendance.txt','a+')
def enterData(z):
    if z in names: 
        pass
    else:
        names.append(z)
        z = ''.join(str(z))
        fob.write(z+'\n') 
        return names
        
print('Reading code...')

# FUNCTION DATA PRESENT OR NOT

def checkData(data):
    data = str(data)
    if data in names:
        print('Already present')
    else:
        print('\n'+str(len(names)+1)+'\n'+'Present Done...')
        enterData(data)
        
        
while True:
    _,frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        checkData(obj.data)
        time.sleep(1)
        
    cv2.imshow('Frame',frame)

#  CLOSE
    if cv2.waitKey(1) & 0xff == ord('q'):
        cv2.destroyAllWindows()
        break

fob.close()



