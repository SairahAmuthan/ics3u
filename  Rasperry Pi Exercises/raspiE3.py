#lights:n 3, 5   buzzer: 8, 10
from gpiozero import LED, Buzzer, Button
from sys import exit
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

button_Y = Button(10)

GPIO.setup(9,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

global Buzz
Buzz = GPIO.PWM(buzzer,440)

   
button_Y.wait_for_press()
user_input = input("Enter 5 random numbers with spaces between each. ")
num_played = input("Enter the number of times you wish to play the frequencies. ")
num_played = int(num_played) + 1
list_frequencies = user_input.split(" ")
#global pressed_exit
#pressed_exit = False

#def quit_program():
    #pressed_exit = True
    #rint(pressed_exit)
    #sys.exit("Program stops")

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
        #GPIO.add_event_detect(9,GPIO.RISING,callback=quit_program)
            
for number in range(1, num_played):
    #if not pressed_exit:
        play_frequencies(list_frequencies)
    #else:
        #sys.exit("Stop")
    
