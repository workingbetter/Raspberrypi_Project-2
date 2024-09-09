from gpiozero import LED, Button

led = LED(17)       # define LED pin according to BCM Numbering
button = Button(18) # define Button pin according to BCM Numbering

def loop():
    while True:
        if button.is_pressed:  # if button is pressed
            led.on()        # turn on led
            print("Button is pressed, led turned on >>>") # print information on terminal 
        else : # if button is relessed
            led.off() # turn off led 
            print("Button is released, led turned off <<<")    

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        print("Ending program")
