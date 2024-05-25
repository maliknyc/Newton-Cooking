import numpy as np
from gpiozero import CPUTemperature, Device, OneWireDevice
from time import sleep

'''

Use: DS18B20 temperature sensor connected to Raspberry Pi

T(t) = C*e^(-k*t)+Ta
    t = duration
    k = cooling constant
    C = initial temperature + ambient temperature
    Ta = ambient temperature

'''

# Calculate cooling constant C: the initial temperature of the food item plus the surrounding temperature (oven or water temperature)
def init_cooling(init_temp, amb_temp):
    C = init_temp + amb_temp
    return C

# Calculate cooling constant k: the rate at which the food item cools down or heats up
def find_k(C, second_temp, amb_temp, duration):
    k = -(np.log((second_temp + amb_temp) / C)) / duration
    return k

# Calculate total duration to reach target temperature
def find_total_duration(C, k, targ_temp, amb_temp):
    duration = -(np.log((targ_temp + amb_temp) / C)) / k
    return duration

if __name__ == "__main__":
    
    # Initialize temperature sensor
    Device.pin_factory = None  # Use default pin factory
    sensor = OneWireDevice.from_sensor_file('/sys/bus/w1/devices/28-xxxxxxxxxxxx/w1_slave') # Replace with device file path
    
    # Read initial temperature from sensor
    init_temp = sensor.temperature
    
    # Wait 10 seconds and read second temperature from sensor
    sleep(10)
    second_temp = sensor.temperature
    
    # Ask user for the ambient cooking temperature and desired target temperature
    amb_temp = int(input("Provide the ambient temperature for the food item: "))
    targ_temp = int(input("Provide your target temperature for the food item: "))
    
    # Calculate constants using initial temp, second temp, ambient temp, and time passed between intial and second temp (10 seconds)
    C = init_cooling(init_temp, amb_temp)
    k = find_k(C, second_temp, amb_temp, 10)
    
    # Calculate time left to reach desired target temperature
    final_duration = round(find_total_duration(C, k, targ_temp, amb_temp), 2)
    time_left = round(final_duration - 10, 2)
    
    print()
    print(f"Initial temperature: {init_temp}°C")
    print(f"Second temperature: {second_temp}°C")
    print(f"Ambient temperature: {amb_temp}°C")
    print(f"Target temperature: {targ_temp}°C")
    print()
    print(f"In total, it will take {final_duration} minutes to cook your food to the desired temperature")
    print(f"You have about {time_left} minutes left until your food is cooked")
