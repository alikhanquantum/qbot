import time
import math
from motor import Motor, motor2040

mR = Motor([10,11], direction=1)
mL = Motor([6,7], direction=0)

def enbleMotors():
    mR.enable()
    mL.enable()

def disableMotors():
    mR.disable()
    mL.disable()

def forward():
    mR.full_positive()
    mL.full_positive()
    
def turnLeft():
    mR.full_positive()
    mL.full_negative()
    
def turnRight():
    mR.full_negative()
    mL.full_positive()
    
def backward():
    mR.full_negative()
    mL.full_negative()

# enbleMotors()
# #forward()
# turnLeft()
# time.sleep(2)
# #backward()
# turnRight()
# time.sleep(2)
# disableMotors()
        

    


