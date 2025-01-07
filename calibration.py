import numpy as np

# Lux data points and corresponding output values
lux_output_values = np.array([255, 176, 135, 0])  # Output values for lux
lux_values = np.array([5, 120, 650, 10000])  # Corresponding lux values

# pH data points and corresponding output values
ph_output_values = np.array([0, 128, 255])  # Output values for pH
ph_values = np.array([0, 7, 14])  # Corresponding pH values

# Salinity (PPT) data points and corresponding output values (dummy values)
salinity_output_values = np.array([0,10, 20, 45,58,125])  # Example output values for salinity
salinity_values = np.array([0, 10, 20,30,40,60])  # Corresponding salinity values in PPT (parts per thousand)

# Fit a polynomial of degree 3 for lux values
lux_degree = 3
lux_coefficients = np.polyfit(lux_output_values, lux_values, lux_degree)
lux_polynomial = np.poly1d(lux_coefficients)

# Fit a linear regression (polynomial of degree 1) for pH values
ph_degree = 1
ph_coefficients = np.polyfit(ph_output_values, ph_values, ph_degree)
ph_polynomial = np.poly1d(ph_coefficients)

# Fit a polynomial of degree 3 for salinity values (to predict salinity)
salinity_degree = 3
salinity_coefficients = np.polyfit(salinity_output_values, salinity_values, salinity_degree)
salinity_polynomial = np.poly1d(salinity_coefficients)

# Function to predict lux based on output value
def predict_lux(value):
    return lux_polynomial(value)

# Function to predict pH based on output value
def predict_ph(value):
    return ph_polynomial(value)

# Function to predict salinity (PPT) based on output value using the polynomial
def predict_salinity(value):
    return salinity_polynomial(value)

# Example usage
output_value = 100
print(f"Predicted Lux for output {output_value}: {predict_lux(output_value)}")
print(f"Predicted pH for output {output_value}: {predict_ph(output_value)}")
print(f"Predicted Salinity for output {output_value}: {predict_salinity(output_value)}")
