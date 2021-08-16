import time
import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)

psupply = 26
relay = 16

io.setup(psupply, io.IN, io.PUD_DOWN)
pc_on = io.input(psupply)

if pc_on:
    print("PC is already ON")
    exit()
else:
    print("PC is OFF")
    print("Turn on now?")
    key = input('y/n?: ')
    if key == 'y':
        io.setup(relay, io.OUT)
        io.output(relay, 1)
        time.sleep(.1)
        io.output(relay, 0)
        time.sleep(2)
        pc_on = io.input(psupply)
        if pc_on:
            print("PC is ON!")
            io.cleanup()
            exit()
        else:
            print("Error: No voltage detected...")
            io.cleanup()
            exit()
    if key == 'n':
        exit()
    else:
        print('You must enter "y" or "n"')
