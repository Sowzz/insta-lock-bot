from pynput.mouse import Controller, Button

mouse = Controller()

while 1:
    print(mouse.position)