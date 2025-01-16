# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht
from datetime import datetime
from pymongo import MongoClient

# MongoDB Configuration
MONGO_URI = "mongodb://root:pklub2025sukses@192.168.196.22:27020"  # Replace with your MongoDB URI
DB_NAME = "test_data"  # Replace with your database name
COLLECTION_NAME = "a0"  # Replace with your collection name

# Initialize the DHT device with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D15)

# Define temperature and humidity offsets
TEMP_OFFSET = 2.0  # Adjust this value to calibrate temperature readings
HUMIDITY_OFFSET = 5.0  # Adjust this value to calibrate humidity readings

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

print("Connected to MongoDB.")

while True:
    try:
        # Read the raw temperature and humidity values
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity

        # Apply offsets
        adjusted_temperature = temperature_c + TEMP_OFFSET
        adjusted_humidity = humidity + HUMIDITY_OFFSET

        # Get current timestamp
        timestamp = datetime.now()

        # Prepare the document to insert into MongoDB
        document = {
            "timestamp": timestamp,
            "temperature_c": adjusted_temperature,
            "humidity": adjusted_humidity
        }

        # Insert the document into the MongoDB collection
        collection.insert_one(document)

        # Print confirmation locally
        print("[{}] Temp: {:.1f} °C    Humidity: {:.1f}% - Data saved to MongoDB.".format(
            timestamp, adjusted_temperature, adjusted_humidity
        ))

    except RuntimeError as error:
        # Errors happen fairly often, DHT sensors can be tricky, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        print("An unexpected error occurred:", error)
        raise error

    # Sample every 1 minute
    time.sleep(6)
