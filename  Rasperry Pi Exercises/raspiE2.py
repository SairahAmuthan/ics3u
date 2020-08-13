#lights:n 3, 5   buzzer: 8, 10
from gpiozero import LED, Buzzer
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer = 15
GPIO.setup(buzzer, GPIO.OUT)


led_A = LED(22)
led_B = LED(27)
led_A.off()
led_B.off()


global Buzz
Buzz = GPIO.PWM(buzzer,440)

   
user_input = input("Enter 5 random numbers with spaces between each. ")
list_frequencies = user_input.split(" ")


def play_frequencies(list_frequencies):
   
    for frequency in list_frequencies:
        frequency = int(frequency)
         
        if frequency >= 200 and frequency <= 1000:
            led_A.blink()
            
            Buzz.start(50)
            Buzz.ChangeFrequency(frequency)
            sleep(1)
            Buzz.stop()
            sleep(1)
            
            led_A.off()
        else:
            led_B.blink() 
            sleep(2)
            led_B.off()
            
play_frequencies(list_frequencies)