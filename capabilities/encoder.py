import RPi.GPIO as GPIO
import time

CLK = 24
DT = 25
SW = 16

GPIO.setmode(GPIO.BCM)

GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0
last_clk = GPIO.input(CLK)

print("Encoder test started")

try:
    while True:
        clk_state = GPIO.input(CLK)

        # Rotation
        if clk_state != last_clk and clk_state == 1:
            if GPIO.input(DT) != clk_state:
                counter += 1
                print(f"Increased | Value: {counter}")
            else:
                counter -= 1
                print(f"Decreased | Value: {counter}")

        last_clk = clk_state

        # Button
        if GPIO.input(SW) == 0:
            print("Pressed")
            time.sleep(0.3)

        time.sleep(0.001)

except KeyboardInterrupt:
    GPIO.cleanup()
