import numpy as np
from scipy.optimize import curve_fit

# Data points
output_values = np.array([255, 176, 135, 0])  # Output values
lux_values = np.array([0, 120, 650, 10000])  # Corresponding lux values

# Define the exponential decay model for lux as the dependent variable
def exp_decay(x, a, b, c):
    return a * np.exp(b * x) + c

# Fit the curve to the data
params, _ = curve_fit(exp_decay, output_values, lux_values, p0=[10000, -0.001, 0])

# Extract the fitted parameters
a, b, c = params
#print(f"Fitted parameters: a = {a}, b = {b}, c = {c}")

# Function to predict lux from output value
def predict_lux(output_value):
    return exp_decay(output_value, *params)

# Example: Predict lux for an output value of 200
#output_test = 200
#lux_predicted = predict_lux(output_test)
#print(f"Predicted lux for output value {output_test}: {lux_predicted}")
