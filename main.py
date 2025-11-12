import machine
import time

# On Pico boards the on-board LED is usually on GP25
led = machine.Pin(25, machine.Pin.OUT)










while True:
    led.toggle()
    time.sleep(0.5)
