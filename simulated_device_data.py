
import csv
import random
import time
from datetime import datetime
from pathlib import Path

OUTPUT_FILE = Path("simulated_device_data.csv")

def generate_reading():
    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "device_id": "IOT-DEVICE-001",
        "temperature_c": round(random.uniform(20, 40), 2),
        "humidity_percent": round(random.uniform(30, 80), 2),
        "voltage_v": round(random.uniform(210, 240), 2),
        "status": "Normal"
    }

def main():
    fields = [
        "timestamp",
        "device_id",
        "temperature_c",
        "humidity_percent",
        "voltage_v",
        "status"
    ]

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for _ in range(20):
            reading = generate_reading()
            writer.writerow(reading)
            print(reading)
            time.sleep(1)

    print(f"\nSaved 20 readings to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
