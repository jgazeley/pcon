import pcon

if pc_on:
    print("PC is already ON")
    exit()
else:
    print("PC is OFF")
    print("Turn on now?")
    key = input('y/n?: ')

    if key == 'y':
        pcon.power_button()
        pcon.time.sleep(2)
        pcon.voltage_check()
        exit()

    if key == 'n':
        exit()
    else:
        print('You must enter "y" or "n"')