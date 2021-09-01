from machine import UART
from machine import Pin as pin

ut = UART(0,9600)
command = b'S'

#Define Driver pins
in1 = pin(16,pin.OUT)
in2 = pin(17,pin.OUT)
in3 = pin(18,pin.OUT)
in4 = pin(19,pin.OUT)

#########
ENA = pin(20,pin.OUT)
ENB = pin(21,pin.OUT)

ENA.value(1)
ENB.value(1)
#########

#This Function moves the Robot forward
def forward():
    in1.value(1)
    in2.value(0)
    in3.value(1)
    in4.value(0)

#This Function moves the Robot backward
def backward():
    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(1)

    
#This Function moves the Robot right
def right():
    in1.value(1)
    in2.value(0)
    in3.value(0)
    in4.value(0)

#This Function moves the Robot left
def left():
    in1.value(0)
    in2.value(0)
    in3.value(1)
    in4.value(0)

#This Function stops the Robot
def stopfcn():
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(0)


while True:
    
    if ut.any():
        command = ut.readline()
        print(command)
        if command == b'F':
            forward()
            
        elif command == b'R':
            right()
            
        elif command == b'L':
            left()
            
        elif command == b'B':
            backward()
            
        elif command == b'S':
            stopfcn()
            
        else:
            pass
        



