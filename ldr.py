import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set pin for the photocell
photocell_pin = 23

def measure_light_intensity(duration=1):
    GPIO.setup(photocell_pin, GPIO.OUT)
    GPIO.output(photocell_pin, GPIO.LOW)
    time.sleep(0.1)  # discharge capacitor

    GPIO.setup(photocell_pin, GPIO.IN)
    start_time = time.time()
    count = 0

    # Measure the number of transitions from low to high
    while (time.time() - start_time) < duration:
        if GPIO.input(photocell_pin):
            count += 1
            while GPIO.input(photocell_pin):
                pass  # Wait for the signal to go low again to count the next transition

    # Calculate the average transitions per second (intensity)
    intensity = count / duration
    return intensity

try:
    while True:
        intensity = measure_light_intensity()
        print("Photocell Intensity:", intensity)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
