import numpy as np

def replace_less_than_value(arr, value):
    arr[arr > value] = value
    return arr

input_array = np.array([[0.42, 0.48, 0.32],
                        [0.74, 0.58, 0.38],
                        [0.51, 0.34, 0.15]])

print("Original array:")
print(input_array)
print("Replace all elements of the original array with 0.5 for values which are greater than 0.5")
output_array = replace_less_than_value(input_array, 0.5)
print(output_array)