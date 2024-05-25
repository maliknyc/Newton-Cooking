import numpy as np


def init_cooling(init_temp, amb_temp):
    C = init_temp + amb_temp
    return C

def find_k(C, second_temp, amb_temp, duration):
    k = -(np.log((second_temp + amb_temp) / C)) / duration
    return k

def find_duration(C, k, targ_temp, amb_temp):
    duration = -(np.log((targ_temp + amb_temp) / C)) / k
    return duration

if __name__ == "__main__":
    
    init_temp = float(input("Provide an initial temperature for the food item: "))
    amb_temp = float(input("Provide the ambient temperature for the food item: "))
    
    second_temp = float(input("Provide a later temperature for the food item: "))
    duration = float(input("Provide how many minutes has passed between the temperature readings: "))
    
    targ_temp = float(input("Provide your target temperature for the food item: "))
    
    C = init_cooling(init_temp, amb_temp)
    k = find_k(C, second_temp, amb_temp, duration)
    
    final_duration = round(find_duration(C, k, targ_temp, amb_temp), 2)
    time_left = round(final_duration - duration, 2)
    
    print()
    print("In total, it will take", final_duration, "minutes to cook your food to the desired temperature")
    print("You have about", time_left, "minutes left until your food is cooked")
    