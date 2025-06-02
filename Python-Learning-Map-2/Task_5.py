# Exercise 1

import numpy as np

# Create arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Basic operations
print("Sum:", arr1 + arr2)
print("Product:", arr1 * arr2)
print("Reshaped (3x1):", arr1.reshape(3, 1))

# Matrix operations
matrix = np.array([[1, 2], [3, 4]])
print("Matrix determinant:", np.linalg.det(matrix))

#exercise 2
import pandas as pd
data = {
    'Name': ['Kamal', 'Amal', 'Nimal'],
    'Age': [25, 30, 35],
    'City': ['Ja-Ela', 'Galle', 'Gampaha']
}
df = pd.DataFrame(data)

# Basic operations
print("DataFrame:")
print(df)
print("\nDescriptive statistics:")
print(df.describe())
print("\nFiltered data (Age > 25):")
print(df[df['Age'] > 25])