import time
import serial
import threading
# serialPort = "/dev/ttyUSB0"  # For Linux
serialPort = "COM17"  # For Windows
baudRate = 115200

# 0-Manual, 1-Automatic
MR_Bit = '0'

# 0-Disable, 1-Enable
LE_Bit = '0'
TCE_Bit = '0'  # Thermal Camera
ZCE_Bit = '0'

PE_Bit = '0'
TE_Bit = '0'
ZE_Bit = '0'
FE_Bit = '0'

# 0-Right/Down/Out, 1-Left/Up/In
PLR_Bit = '0'   # Depends on PE_Bit
TUD_Bit = '0'   # Depends on TE_Bit
ZIO_Bit = '0'   # Depends on ZCE_Bit
FIO_Bit = '0'   # Depends on ZCE_Bit


def ledOn():
    global LE_Bit
    LE_Bit = '1'


def ledOff():
    global LE_Bit
    LE_Bit = '0'


def thermalOn():
    global TE_Bit
    TE_Bit = '1'


def thermalOff():
    global TE_Bit
    TE_Bit = '0'


def panOn():
    global PE_Bit
    PE_Bit = '1'


def panOff():
    global PE_Bit
    PE_Bit = '0'


def tiltOn():
    global TE_Bit
    TE_Bit = '1'


def tiltOff():
    global TE_Bit
    TE_Bit = '0'


def zoomOn():
    global ZCE_Bit
    ZCE_Bit = '1'


def zoomOff():
    global ZCE_Bit
    ZCE_Bit = '0'


def panLeft():
    global PE_Bit, PLR_Bit
    PE_Bit = '1'
    PLR_Bit = '1'


def panRight():
    global PE_Bit, PLR_Bit
    PE_Bit = '1'
    PLR_Bit = '0'


def tiltUp():
    global TE_Bit, TUD_Bit
    TE_Bit = '1'
    TUD_Bit = '1'


def tiltDown():
    global TE_Bit, TUD_Bit
    TE_Bit = '1'
    TUD_Bit = '0'


def zoomIn():
    zoomOn()
    global ZE_Bit, ZIO_Bit
    ZE_Bit = '1'
    ZIO_Bit = '1'


def zoomOut():
    zoomOn()
    global ZE_Bit, ZIO_Bit
    ZE_Bit = '1'
    ZIO_Bit = '0'


def focusIn():
    zoomOn()
    global FE_Bit, FIO_Bit
    FE_Bit = '1'
    FIO_Bit = '1'


def focusOut():
    zoomOn()
    global FE_Bit, FIO_Bit
    FE_Bit = '1'
    FIO_Bit = '0'


def initSerial():
    try:
        return serial.Serial(
            port=serialPort,
            baudrate=baudRate,
            # parity=serial.PARITY_ODD,
            # stopbits=serial.STOPBITS_TWO,
            # bytesize=serial.EIGHTBITS,
            timeout=1
        )
        time.sleep(1)
    except serial.serialutil.SerialException as e:
        print("Could not open COM Port")


def sendDataToSerial(ser, data):
    print("Sending \"{}\" on port {}.... Written {} Bytes".format(
        data, ser.name, ser.write(str(data).encode())))


def receiveDataFromSerial(ser):
    try:
        i = 0
        while True:
            data = ser.readline()
            if(data):
                print("\t\t\t\t\t\tArduino Raw data received : {}".format(data))
                try:
                    if(int(data, 10) == ptzControl()):
                        i += 1
                except ValueError as e:
                    print("\t\t\t\t\t\tReceived from Arduino: {}".format(
                        data.decode('utf-8')))
                # if i % 2 == 0:
                #     ledOn()
                # else:
                #     ledOff()

                if i == 1:
                    panLeft()
                elif i == 2:
                    panRight()
                elif i == 3:
                    tiltUp()
                elif i == 4:
                    tiltDown()
                elif i == 5:
                    zoomIn()
                elif i == 6:
                    zoomOut()
                elif i == 7:
                    focusIn()
                elif i == 8:
                    focusOut()
                elif i == 9:
                    thermalOn()
                elif i == 10:
                    thermalOff()
                elif i == 11:
                    ledOn()
                elif i == 12:
                    ledOff()
                    i = 1

            sendDataToSerial(ser, ptzControl())
            time.sleep(0.1)
    except:
        print("Exiting Serial Read...")
        exit()


def ptzControl():
    data = FIO_Bit+ZIO_Bit+TUD_Bit+PLR_Bit+FE_Bit + \
        ZE_Bit+TE_Bit+PE_Bit+ZCE_Bit+TCE_Bit+LE_Bit+MR_Bit

    decData = int(data, 2)
    # print("Binary Data: {}, Decimal data : {}".format(data, decData))
    return decData


if __name__ == "__main__":
    ser = initSerial()
    if(ser):
        receiveDataFromSerialThread = threading.Thread(
            target=receiveDataFromSerial, args=(ser,))

        receiveDataFromSerialThread.start()
        receiveDataFromSerialThread.join()
        print("Program Completed")
