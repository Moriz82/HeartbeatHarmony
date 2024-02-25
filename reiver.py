from gpiozero import DigitalInputDevice
from signal import pause

# Assuming the IR receiver is connected to GPIO pin 8
ir_receiver = DigitalInputDevice(23)

def on_receive():
    print("IR signal received")

# Define a callback function to handle IR signal reception
ir_receiver.when_activated = on_receive

print("Listening for IR signals...")
pause()  # Keeps the script running to continue listening for signals
