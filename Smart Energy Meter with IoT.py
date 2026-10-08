import time

# Smart Energy Meter
# Example values — replace these with sensor readings

VOLTAGE = 230.0       # Volts
CURRENT = 2.0         # Amps
TIME_INTERVAL = 1     # seconds

energy_kwh = 0.0

while True:
    # Calculate power
    power = VOLTAGE * CURRENT       # Watts

    # Energy consumed in kWh
    energy_kwh += (power * TIME_INTERVAL) / (1000 * 3600)

    print("--------------------------------")
    print("SMART ENERGY METER")
    print("Voltage :", VOLTAGE, "V")
    print("Current :", CURRENT, "A")
    print("Power   :", round(power, 2), "W")
    print("Energy  :", round(energy_kwh, 6), "kWh")
    print("--------------------------------")

    time.sleep(TIME_INTERVAL)
