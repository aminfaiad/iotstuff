import adafruit_dht
import gpiozero
import time


# dht = adafruit_dht.DHT11(adafruit_dht.Pin(20))


###Light sensor
### GELAP  =180 - 255
### Sederhana 80-180
### Cerah  < 80
sensor = gpiozero.DistanceSensor(echo=12, trigger=6)
try:
    while True:
        # Get the current distance in meters
        distance = sensor.distance
        print(f"Distance: {distance:.2f} meters")
        
        # Sleep for a while before taking another measurement
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program stopped by user.")
