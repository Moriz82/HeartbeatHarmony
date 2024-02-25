from gpiozero import DigitalInputDevice
from signal import pause
import time

# Assuming the IR receiver is connected to GPIO pin 8
ir_receiver = DigitalInputDevice(23)

def on_receive():
    # Get the current Unix timestamp
    timestamp = time.time()
    # Get the strength of the received signal
    strength = ir_receiver.value
    print("IR signal received - Strength:", strength, "Timestamp:", timestamp)

# Define a callback function to handle IR signal reception
ir_receiver.when_activated = on_receive

print("Listening for IR signals...")
pause()  # Keeps the script running to continue listening for signals
