import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))  #Output the given byte string over the serial port.
    time.sleep(0.05)
    data = arduino.readline()
    return data

    
while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)

    print(value[:-2])   #b'DOOR is Closed'
    # print(value) # printing the value   #b'DOOR is Closed\r\n'
