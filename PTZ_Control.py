import serial
# serialPort = "/dev/ttyUSB0"  # For Linux
serialPort = "COM17"  # For Windows
baudRate = 115200


def sendDataToSerial(data):
    try:
        ser = serial.Serial(
            port=serialPort,
            baudrate=baudRate,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.EIGHTBITS
        )
        print(ser.is_open)
        print(ser.name)         # check which port was really used

        ser.write(data)
        ser.close()

    except serial.serialutil.SerialException as e:
        print("Could not open COM Port")


#0-Manual, 1-Automatic
MR_Bit = '1'

#0-Disable, 1-Enable
LE_Bit = '1'
TCE_Bit = '0'  # Thermal Camera
ZCE_Bit = '0'

PE_Bit = '1'
TE_Bit = '0'
ZE_Bit = '0'
FE_Bit = '0'

#0-Right/Down/Out, 1-Left/Up/In
PLR_Bit = '0'   # Depends on PE_Bit
TUD_Bit = '0'   # Depends on TE_Bit
ZIO_Bit = '0'   # Depends on ZCE_Bit
FIO_Bit = '0'   # Depends on ZCE_Bit

data = FIO_Bit+ZIO_Bit+TUD_Bit+PLR_Bit+FE_Bit + \
    ZE_Bit+TE_Bit+PE_Bit+ZCE_Bit+TCE_Bit+LE_Bit+MR_Bit

print("Binary Data: {}".format(data))
data = int(data, 2)
print("Decimal Data to sent: {}".format(data))

sendDataToSerial(data)
