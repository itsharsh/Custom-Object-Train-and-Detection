import serial
# serialPort = "/dev/ttyUSB0"  # For Linux
serialPort = "COM6"  # For Windows
baudRate = 9600

ser = serial.Serial(
    port=serialPort,
    baudrate=baudRate,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS
)

print(ser.is_open)

print(ser.name)         # check which port was really used

#0-Manual, 1-Automatic
MR_Bit = '1'

#0-Disable, 1-Enable
LE_Bit = '1'
TCE_Bit = '0'
ZCE_Bit = '0'

PE_Bit = '0'
TE_Bit = '0'
ZE_Bit = '0'
FE_Bit = '0'

#0-Right/Down/Out, 1-Left/Up/In
PLR_Bit = '0'
TUD_Bit = '0'
ZIO_Bit = '0'
FIO_Bit = '0'

data = FIO_Bit+ZIO_Bit+TUD_Bit+PLR_Bit+FE_Bit + \
    ZE_Bit+TE_Bit+PE_Bit+ZCE_Bit+TCE_Bit+LE_Bit+MR_Bit

print(data)
data = int(data, 2)
print(data)

ser.write(data)
ser.close()
