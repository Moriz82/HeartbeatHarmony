from gpiozero import DigitalInputDevice
import RPi.GPIO as GPIO
import time
import math
import matplotlib.pyplot as plt
import numpy as np

IR_rec_pin = 23

ir_rec = DigitalInputDevice(IR_rec_pin)
pulse_count = 0
start_time = time.time()

plotStart_time = time.time()

x = 0
y = 0

plt.ion()

figure, ax = plt.subplots(figsize=(10,8))
line1, = ax.plot(x,y)

try:
	while True:
		ir_value = ir_rec.value
		if ir_value == 1:
			pulse_count += 1
		if time.time() - start_time >= 1:
			print (pulse_count)
			line1.set_xdata(time.time() - plotStart_time)
			line1.set_ydata(pulse_count)

			figure.canvas.draw()
			figure.canvas.flush_events()

			pulse_count = 0
			start_time = time.time()
except KeyboardInterrupt:
	pass
finally:
	ir_rec.close()

