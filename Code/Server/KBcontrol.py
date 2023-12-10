import time
from Motor import *
# from ADC import *
from picamera2 import Picamera2
import time
import RPi.GPIO as GPIO
from Command import COMMAND as cmd

import tty
import sys
import termios

GPIO.setwarnings(False)
Buzzer_Pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(Buzzer_Pin,GPIO.OUT)
class Buzzer:
    def run(self,command):
        if command!="0":
            GPIO.output(Buzzer_Pin,True)
        else:
            GPIO.output(Buzzer_Pin,False)

class Light:
    def run(self):
        orig_settings = termios.tcgetattr(sys.stdin)
        
        tty.setcbreak(sys.stdin)
        try:
            # self.adc=Adc()
            self.PWM=Motor()
            self.PWM.setMotorModel(0,0,0,0)
            self.B=Buzzer()
            while True:
                # L = self.adc.recvADC(0)
                # R = self.adc.recvADC(1)
                lastkey = sys.stdin.read(1)[0]
                if lastkey == 'w':
                    self.PWM.setMotorModel(1000,1000,1000,1000)
                elif lastkey == ' ':
                    self.PWM.setMotorModel(0,0,0,0)
                    self.B.run('0')
                elif lastkey == 's':
                    self.PWM.setMotorModel(-1000,-1000,-1000,-1000)
                elif lastkey == 'a':
                    self.PWM.setMotorModel(-1600,-1600,2000,2000)
                elif lastkey == 'd' :
                    self.PWM.setMotorModel(2000,2000,-1600,-1600)
                elif lastkey == 'b' :
                    self.B.run('1')
                elif lastkey == 'W':
                    self.PWM.setMotorModel(2000,2000,2000,2000)
                elif lastkey == 'S':
                    self.PWM.setMotorModel(-2000,-2000,-2000,-2000)
                elif lastkey == 'A':
                    self.PWM.setMotorModel(-2100,-2100,2500,2500)
                elif lastkey == 'D' :
                    self.PWM.setMotorModel(3000,3000,-2400,-2400)
                lastkey = ' '
                
                '''picam2 = Picamera2()
                picam2.start'''

                    
                    
        except KeyboardInterrupt:
           led_Car.PWM.setMotorModel(0,0,0,0)
           led_Car.B.run('0')
           termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)

if __name__=='__main__':
    print ('Program is starting ... ')
    led_Car=Light()
    led_Car.run()
    


        
    

