from gpiozero import LED
import time

led = LED(17)

while True:
	led.on()
	time.sleep(0.05)
	led.off()
	time.sleep(0.05)
