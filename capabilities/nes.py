import RPi.GPIO as GPIO
import time

# Controller 1
LATCH_1 = 17
CLOCK_1 = 27
DATA_1  = 22

# Controller 2
LATCH_2 = 5
CLOCK_2 = 6
DATA_2  = 13

GPIO.setmode(GPIO.BCM)

# Setup controller 1
GPIO.setup(LATCH_1, GPIO.OUT)
GPIO.setup(CLOCK_1, GPIO.OUT)
GPIO.setup(DATA_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup controller 2
GPIO.setup(LATCH_2, GPIO.OUT)
GPIO.setup(CLOCK_2, GPIO.OUT)
GPIO.setup(DATA_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def read_controller(latch, clock, data):
    buttons = []

    # latch button states
    GPIO.output(latch, True)
    time.sleep(0.00001)
    GPIO.output(latch, False)

    for i in range(8):
        buttons.append(GPIO.input(data))
        GPIO.output(clock, True)
        time.sleep(0.00001)
        GPIO.output(clock, False)

    return buttons


try:
    while True:
        c1 = read_controller(LATCH_1, CLOCK_1, DATA_1)
        c2 = read_controller(LATCH_2, CLOCK_2, DATA_2)

        print("P1:", c1, "| P2:", c2)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
