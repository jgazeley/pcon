import RPi.GPIO as io
import time

psupply = 26
relay = 16

io.setwarnings(False)
io.setmode(io.BCM)
io.setup(relay, io.OUT)
io.setup(psupply, io.IN, io.PUD_DOWN)

pc_on = io.input(psupply)

def power_button():
    io.output(relay, 1)
    time.sleep(.1)
    io.output(relay, 0)

def voltage_check():
    if pc_on:
        print("PC is ON!")
    else:
        print("Error: no voltage detected...")
