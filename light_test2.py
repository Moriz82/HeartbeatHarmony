from gpiozero import DigitalInputDevice
import time

IR_rec_pin = 23

ir_rec = DigitalInputDevice(IR_rec_pin)
pulse_count = 0
start_time = time.time()

# Adjust the time interval to check the value more frequently
check_interval = 0.1  # seconds

# List to store data
data = []

try:
    while True:
        ir_value = ir_rec.value
        if ir_value == 1:
            pulse_count += 1
        if time.time() - start_time >= check_interval:
            print(pulse_count)
            # Append the timestamp and pulse count to the data list
            data.append((time.time(), pulse_count))

            pulse_count = 0
            start_time = time.time()
except KeyboardInterrupt:
    pass
finally:
    ir_rec.close()

# Save the data to a text file
with open("plotted_data.txt", "w") as file:
    for timestamp, count in data:
        file.write(f"{timestamp}\t{count}\n")
