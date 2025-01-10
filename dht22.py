import Adafruit_DHT
import time

# Set sensor type and GPIO pin
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 15  # Replace with the GPIO pin you are using

# Calibration offsets
TEMP_OFFSET = 1.0  # Adjust as needed (in °C)
HUMIDITY_OFFSET = 2.0  # Adjust as needed (in %)

# Temperature warning threshold (in °C)
TEMP_WARNING_THRESHOLD = 30.0  # Set the temperature threshold

def read_dht22():
    try:
        # Read temperature and humidity from the sensor
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        
        if humidity is not None and temperature is not None:
            # Apply calibration offsets
            calibrated_temp = temperature + TEMP_OFFSET
            calibrated_humidity = humidity + HUMIDITY_OFFSET
            
            print(f"Calibrated Temp: {calibrated_temp:.1f}°C, Calibrated Humidity: {calibrated_humidity:.1f}%")
            
            # Check if the temperature exceeds the threshold
            if calibrated_temp > TEMP_WARNING_THRESHOLD:
                print(f"Warning: Temperature is above {TEMP_WARNING_THRESHOLD}°C!")
        else:
            print("Failed to retrieve data from the sensor")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        read_dht22()
        time.sleep(2)  # Wait for 2 seconds before the next readingimport Adafruit_DHT
import time

# Set sensor type and GPIO pin
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 15  # Replace with the GPIO pin you are using

# Calibration offsets
TEMP_OFFSET = 1.0  # Adjust as needed (in °C)
HUMIDITY_OFFSET = 2.0  # Adjust as needed (in %)

# Temperature warning threshold (in °C)
TEMP_WARNING_THRESHOLD = 30.0  # Set the temperature threshold

def read_dht22():
    try:
        # Read temperature and humidity from the sensor
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        
        if humidity is not None and temperature is not None:
            # Apply calibration offsets
            calibrated_temp = temperature + TEMP_OFFSET
            calibrated_humidity = humidity + HUMIDITY_OFFSET
            
            print(f"Calibrated Temp: {calibrated_temp:.1f}°C, Calibrated Humidity: {calibrated_humidity:.1f}%")
            
            # Check if the temperature exceeds the threshold
            if calibrated_temp > TEMP_WARNING_THRESHOLD:
                print(f"Warning: Temperature is above {TEMP_WARNING_THRESHOLD}°C!")
        else:
            print("Failed to retrieve data from the sensor")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        read_dht22()
        time.sleep(2)  # Wait for 2 seconds before the next reading
