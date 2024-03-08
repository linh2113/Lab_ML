import numpy as np

input_array = np.array([1, 2, 3, 4])
num_repetitions = int(input("Enter the number of repetitions: "))
repeated_array = np.tile(input_array, num_repetitions)
print("Original array:",input_array)
print(f"Repeating {num_repetitions} times:",repeated_array)