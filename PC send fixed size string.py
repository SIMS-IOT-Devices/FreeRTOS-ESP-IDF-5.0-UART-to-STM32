import serial
import time

# Use the COM port of your HW-409
ser = serial.Serial(port='COM5', baudrate=115200)

time.sleep(1) 

# The message must be EXACTLY 22 characters for your current STM32 code
message = "Hello to STM32" # 22 characters total
ser.write(message.encode('utf-8'))

print(f"Sent: {message} ({len(message)} chars)")

# Give the hardware a millisecond to actually push the bits out
time.sleep(0.5)
ser.close()
