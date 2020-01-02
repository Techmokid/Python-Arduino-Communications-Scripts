#My arduino Mega 2560 is connected to COM11 by default. I think Arduino Uno is COM3
#If unsure, the arduino IDE will tell you if you go to "Tools", "Port: "
#provided that your arduino is plugged in of course



#Arduino library functions:
#------------------------------------------------------------------
#arduino.begin(baudrate)
#arduino.setPort(portName)
#arduino.writeLine(stringToSend)
#arduino.readLine()

#ALTERNATIVE ACCEPTED SYNTAX:
#arduino.begin(baudrate,portName)

#E.g.
#arduino.setPort("COM11")
#arduino.begin(9600)
#
#is the same as typing:
#arduino.begin(9600,"COM11")

#NOTE:  write(stringToSend) and readChar() are also functions, but should not be called under
#       normal operation as they are more advanced features without the same functionality

#WARNING: Starting Arduino communications with arduino.begin() restarts the arduino, keep
#that in mind if you are doing something important, as the arduino will reboot. This is
#really handy in most situations, but a real pain in some specific cases.



import arduino,time

#Restart the arduino and open communications
arduino.begin(115200,"COM11")

#Write "Hello World!" to the arduino.
arduino.writeLine("Hello World!")

#Print to the screen whatever the arduino returned.
print(arduino.readLine())

#Pause for 3 seconds so the user can read what the arduino returned
time.sleep(3)
