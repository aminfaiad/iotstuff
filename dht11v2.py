import adafruit_dht
import gpiozero
import time


dht = adafruit_dht.DHT11(adafruit_dht.Pin(21))




'''
try:
    while True:
        # Get the current distance in meters
        distance = sensor.distance
        print(f"Distance: {distance:.2f} meters")
        
        # Sleep for a while before taking another measurement
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program stopped by user.")
'''
