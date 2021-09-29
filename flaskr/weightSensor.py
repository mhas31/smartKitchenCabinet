import serial

class WeightSensor:
    def __init__(self, baudrate = 9600):

        # for windows:
        self.ser = serial.Serial('com7', baudrate)
        # for linux with usb-to-serial
        # self.ser = serial.Serial('/dev/ttyUSB0', baudrate)
    
    def readLast(self):

        #clear buffer
        self.ser.flushInput()
        val = ''

        for i in range(3):
            val = self.ser.readline()
        
        strArray = val.split()

        listVal = []

        for v in strArray:
            listVal.append(float(v))

        return listVal
