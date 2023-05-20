import motors1 as mt
import time
from machine import Pin,UART
uart1 = UART(1, baudrate=115200, tx=Pin(8), rx=Pin(9))

def runWireless():
    uart1.write('hello')  # write 5 bytes
    while True:
        if uart1.any():
            command = uart1.read()
            if command == b'forward':
                mt.forward()
                time.sleep(2)
                mt.disableMotors()
            else:
                uart1.write('hello1')
            print(command)
