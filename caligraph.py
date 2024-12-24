import numpy as np
import matplotlib.pyplot as plt

# Data points
output_values = np.array([255, 176, 135, 0])  # Output values
lux_values = np.array([5, 120, 650, 10000])  # Corresponding lux values

# Fit a polynomial of degree 3 (or any other degree that fits your data)
degree = 3
coefficients = np.polyfit(output_values, lux_values, degree)

# Create a polynomial function from the coefficients
polynomial = np.poly1d(coefficients)

# Generate a range of output values for plotting the fitted curve
output_range = np.linspace(0, 255, 100)
lux_predicted_range = polynomial(output_range)

# Plot the data and the fitted curve
plt.scatter(output_values, lux_values, color='red', label='Data Points')
plt.plot(output_range, lux_predicted_range, label=f'Fitted Polynomial: degree={degree}', color='blue', lw=2)

plt.xlabel('Output Value')
plt.ylabel('Lux')
plt.title('Polynomial Fit to Lux Data')
plt.grid(True)
plt.legend()
plt.show()
print(polynomial(255))
