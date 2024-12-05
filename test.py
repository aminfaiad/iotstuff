import gpiozero
import adafruit_dht
import smbus2
import requests

def analogToPh(val):
    pass
def analogToSalinity(val):
    pass
def analogToLux(val):
    pass



pin_a_phsensor=0
pin_a_salinity=1
pin_a_light=2
pin_dht=0
pin_ultrasonic_echo=0
pin_ultrasonic_trig=0


dhtcomp = adafruit_dht.DHT11(pin_dht)
bus = smbus2.SMBus(1)
dhtcomp.measure()
#dhtcomp.temperature
#dhtcomp.humidity

def getAnalog(pin):
    if pin <0 or pin > 3 :
        print("Bad pin")
        return
    global bus
    data = bus.read_i2c_block_data(0x48,pin,3)
    data = data[1]
    return data

