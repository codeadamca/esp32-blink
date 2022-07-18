# Print all available modules
# help('modules')

from time import sleep
# from machine import Pin

from machine import Pin
led = Pin(2, Pin.OUT)

while True:

    led.value(1)
    sleep(0.5)

    print(led.value())

    led.value(0)
    sleep(0.5)

    print(led.value())