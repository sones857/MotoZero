#motozero.py
#basic motor control with motozero hat (not board), haa!)
#pinout - https://pinout.xyz/pinout/motozero
#pdf - https://cdn.shopify.com/s/files/1/0176/3274/files/MotoZero_User_Guide_1.1.pdf

from gpiozero import Motor, OutputDevice
from time import sleep

motor1 = Motor(24, 27)
motor1_enable = OutputDevice(5, initial_value=1)

motor2 = Motor(6, 22)
motor2_enable = OutputDevice(17, initial_value=1)

motor3 = Motor(23, 16)
motor3_enable = OutputDevice(12, initial_value=1)

motor4 = Motor(13, 18)
motor4_enable = OutputDevice(25, initial_value=1)

motors = (motor1, motor2, motor3, motor4)

for motor in motors:
    motor.forward()
    sleep(1)
    motor.stop()
    