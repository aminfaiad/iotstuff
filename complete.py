import time
import random
import json
import requests
import cv2
from adafruit_dht import DHT11
from gpiozero import DistanceSensor

# Define constants
FARM_TOKEN = f"farm_{random.randint(1000, 9999)}"
READ_INTERVAL = 10  # seconds
API_SENSOR_URL = "http://www.example.com/api"
API_IMAGE_URL = "http://www.example.com/image"

# Pin definitions
PIN_PH_SENSOR = 0  # Replace with your analog pin for pH sensor
PIN_SALINITY_SENSOR = 1  # Replace with your analog pin for salinity sensor
PIN_LIGHT_SENSOR = 2  # Replace with your analog pin for light sensor
PIN_DHT_SENSOR = 4  # GPIO pin connected to DHT11
ULTRASONIC_TRIGGER_PIN = 23  # GPIO pin for ultrasonic sensor trigger
ULTRASONIC_ECHO_PIN = 24  # GPIO pin for ultrasonic sensor echo

# Initialize sensors
dht_sensor = DHT11(PIN_DHT_SENSOR)
distance_sensor = DistanceSensor(echo=ULTRASONIC_ECHO_PIN, trigger=ULTRASONIC_TRIGGER_PIN)

def getAnalog(pin):
    """
    Mock function to simulate reading analog value from pin.
    Replace this with the actual method to read analog values.
    """
    return random.randint(0, 255)

def capture_image():
    """
    Captures an image using OpenCV and saves it to a file.
    """
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    if ret:
        filename = "sensor_image.jpg"
        cv2.imwrite(filename, frame)
        camera.release()
        return filename
    else:
        camera.release()
        raise RuntimeError("Failed to capture image from webcam.")

def measure_distance():
    """
    Measures distance using the gpiozero library for the ultrasonic sensor.
    """
    return round(distance_sensor.distance * 100, 2)  # Convert from meters to cm

def read_sensors():
    """
    Reads all sensors and returns the data as a dictionary.
    """
    try:
        ph_value = getAnalog(PIN_PH_SENSOR)
        salinity = getAnalog(PIN_SALINITY_SENSOR)
        light_intensity = getAnalog(PIN_LIGHT_SENSOR)
        dht_sensor.measure()
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
        sonic_distance = measure_distance()
        return {
            "farm_token": FARM_TOKEN,
            "ph_value": ph_value,
            "temperature": temperature,
            "salinity": salinity,
            "light_intensity": light_intensity,
            "sonic_distance": sonic_distance,
        }
    except Exception as e:
        print(f"Error reading sensors: {e}")
        return None

def send_sensor_data(data):
    """
    Sends sensor data as JSON to the API.
    """
    try:
        response = requests.post(API_SENSOR_URL, json=data)
        print(f"Sensor data sent: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending sensor data: {e}")

def send_image(filename):
    """
    Sends an image to the API.
    """
    try:
        with open(filename, "rb") as img_file:
            files = {"image": img_file}
            response = requests.post(API_IMAGE_URL, files=files)
            print(f"Image sent: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending image: {e}")

def main():
    """
    Main loop to read sensors and send data periodically.
    """
    while True:
        sensor_data = read_sensors()
        if sensor_data:
            send_sensor_data(sensor_data)
            try:
                image_file = capture_image()
                send_image(image_file)
            except Exception as e:
                print(f"Error capturing or sending image: {e}")
        time.sleep(READ_INTERVAL)

if __name__ == "__main__":
    main()
