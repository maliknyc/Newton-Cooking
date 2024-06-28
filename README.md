# Food Cooling Calculator

## Overview
This Python script helps users calculate the duration required to cool food to a desired temperature using initial and ambient temperatures. The script uses an exponential decay model to estimate the cooling duration and provides the user with the estimated time left to reach the target temperature.

## Prerequisites
Before running the script, ensure you have the following library installed:
- numpy

## Usage
Install the library with:
pip install numpy

Make sure you have the initial and ambient temperature values ready. You will also need a later temperature reading and the duration between the initial and later temperature readings.

Execute the script and follow the prompts:
python User-input tool.py

### Input Details:
1. **Initial Temperature:** Provide the initial temperature of the food item.
2. **Ambient Temperature:** Provide the ambient temperature.
3. **Later Temperature:** Provide a later temperature of the food item.
4. **Duration:** Enter the duration in minutes between the initial and later temperature readings.
5. **Target Temperature:** Provide your target temperature for the food item.

### Output:
The script will display:
- The total time required to cool the food to the desired temperature.
- The estimated time left until the food reaches the target temperature.

