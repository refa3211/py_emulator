from pynput.mouse import Controller, Button, Listener

from mss import mss


def on_click(x, y, button, pressed):
    if pressed:
        print(f'mouse clicked at {x}, {y}')


with Listener(on_click=on_click) as listener:
    listener.join()

on_click()