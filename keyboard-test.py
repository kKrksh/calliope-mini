import keyboard
import serial
import time

ser = serial.Serial("COM3", 9600)

def on_key_press(event):
    print(f"Key pressed: {event.name}")
    ser.write(f'{event.name}'.encode('utf-8'))

keyboard.on_press(on_key_press)

while True:
    time.sleep(0.1)
