import serial,sys
import time
ser = serial.Serial(sys.argv[1],115200)  
ser.setDTR(False)
time.sleep(0.1)
ser.setRTS(False)
ser.rtscts = False
time.sleep(1) # wait esp32 wakeup  

#your code here

ser.close()
