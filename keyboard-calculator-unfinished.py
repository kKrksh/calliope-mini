from calliopemini import *

allowed_inputs = [b"1",b"2",b"3",b"4",b"5",b"6",b"7",b"8",b"9",b"0",b"+",b"-",b"*",b"/",b"(",b")"]
uart.init(baudrate=9600)

to_calculate = ""


while True:
    if uart.any():
        key = uart.read(1)
        if key == b'Enter':
            display.scroll(eval(to_calculate))
        elif key == b'Backspace':
            to_calculate = to_calculate[:-1]
        elif key in allowed_inputs:
            to_calculate += key.decode("utf-8")
            display.show(key.decode("utf-8"))
        
            
            