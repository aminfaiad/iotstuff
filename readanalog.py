import gpiozero
import time
import smbus2

BUS = smbus2.SMBus(1)




def readAnalog(pin):
	return (BUS.read_i2c_block_data(0x48,pin,2)[-1] )
