from gpiozero import DigitalInputDevice
import time

IR_rec_pin = 23

ir_rec = DigitalInputDevice(IR_rec_pin)
pulse_count = 0
start_time = time.time()

# Adjust the time interval to check the value more frequently
check_interval = 0.1  # seconds

# Open the file in append mode
with open("plotted_data.txt", "a") as file:
    try:
        while True:
            ir_value = ir_rec.value
            if ir_value == 1:
                pulse_count += 1
            if time.time() - start_time >= check_interval:
                # Append the timestamp and pulse count to the file
                file.write(f"{time.time()}, {pulse_count}\n")
                file.flush()  # Ensure data is written immediately
                print(pulse_count)
                pulse_count = 0
                start_time = time.time()
    except KeyboardInterrupt:
        pass
    finally:
        ir_rec.close()
