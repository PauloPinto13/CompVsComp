#ultrasonicSensor.py

import RPi.GPIO as GPIO
from time import sleep,time
from pygame import mixer

TRIGGER_PIN = 26
ECHO_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)
sleep(2) # let the circuit settle

def send_trigger_pulse():
    GPIO.output(TRIGGER_PIN,True)
    sleep(0.001)
    GPIO.output(TRIGGER_PIN,False)

def wait_for_echo(value,timeout):
    count = timeout
    while GPIO.input(ECHO_PIN) != value and count > 0:
        count -= 1
def get_distance():
    send_trigger_pulse()
    wait_for_echo(True,1000)
    start = time()
    wait_for_echo(False,1000)
    finish = time()
    pulse_len = finish - start
    distance_cm = pulse_len * 343 * 100/2
    return distance_cm
def play_sound():
    mixer.init()
    mixer.music.load("/usr/lib/python2.7/dist-packages/pygame/examples/data/car_door.wav")
    mixer.music.play()
    while mixer.music.get_busy(): # wait until the sound ends
        sleep(0.01)

    mixer.music.load("/usr/share/scratch/Media/Sounds/Human/Footsteps-1.wav")
    mixer.music.play()
    while mixer.music.get_busy(): # wait until the sound ends
        sleep(0.01) 
def main():
    try:
        while True:
            print("STarting the main block")
            distance = get_distance()
            print("distance in cm is " + str(distance))
            if distance < 20.0:
                play_sound()
            sleep(0.5)
    except KeyboardInterrupt:
        
        print("Exiting...")
        sleep(1)
    finally:
        print("Clean up")
        GPIO.cleanup()
main()
              
              
              
