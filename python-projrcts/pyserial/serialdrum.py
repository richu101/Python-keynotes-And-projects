import serial
ser = serial.Serial('/dev/ttyACM0')  # open serial port
print(ser.name)
while 1:
    s = ser.read()  
    print(s)