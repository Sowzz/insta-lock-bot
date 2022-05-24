from pynput.mouse import Controller, Button
import time

time.sleep(6)
mouse = Controller()

mouse.position = (592, 1000)
mouse.press(Button.left)
mouse.release(Button.left)

mouse.position = (708, 813)
mouse.press(Button.left)
mouse.release(Button.left)
