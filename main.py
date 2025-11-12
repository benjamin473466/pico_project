import machine
import machine
import sys
import time

# Small startup message so we can confirm main.py actually ran
print("main.py starting")

# On Pico boards the on-board LED is usually on GP25
led = machine.Pin(25, machine.Pin.OUT)


try:
    while True:
        led.toggle()
        time.sleep(0.5)
except Exception as e:
    # Print exception details to the serial console for debugging
    print("Exception in main:", e)
    try:
        sys.print_exception(e)
    except Exception:
        pass
    led.toggle()
    time.sleep(0.5)
