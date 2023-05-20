import machine
import time

def measure_distance():
    # Set up the GPIO pins for the HC-SR04 sensor
    trig_pin = machine.Pin(27, machine.Pin.OUT)
    echo_pin = machine.Pin(26, machine.Pin.IN)

    # Send a 10 microsecond pulse to trigger the HC-SR04
    trig_pin.value(0)
    time.sleep_us(2)
    trig_pin.value(1)
    time.sleep_us(10)
    trig_pin.value(0)

    # Wait for the echo pulse to start and stop
    pulse_start = time.ticks_us()
    while echo_pin.value() == 0:
        pulse_start = time.ticks_us()

    pulse_end = pulse_start
    while echo_pin.value() == 1:
        pulse_end = time.ticks_us()

    # Calculate the duration of the echo pulse and convert to distance in cm
    pulse_duration = pulse_end - pulse_start
    distance_cm = pulse_duration * 0.034 / 2

    return distance_cm
print (measure_distance())