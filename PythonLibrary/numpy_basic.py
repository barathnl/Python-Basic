import numpy as np

# --- 1D Array (Vector) ---
array_1d = np.array([1, 2, 3])

print(f"\nNumpy array :\n {array_1d}")
print(array_1d.ndim)  # Number of axes/dimensions (1)
print(array_1d.shape) # Tuple representing elements along each axis (3,)
print(array_1d.size)  # Total number of elements in the array (3)
print(type(array_1d)) # <class 'numpy.ndarray'> - The core N-dimensional array object


# --- 2D Array (Matrix) ---
# Rows and Columns: Useful for tabular data
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])

print(f"\nNumpy array :\n {array_2d}")
print(array_2d.ndim)  # Output: 2
print(array_2d.shape) # Output: (2, 3) -> (Rows, Columns)
print(array_2d.size)  # Output: 6 (Total elements: 2 * 3)


# --- 3D Array (Tensor) ---
# Think of this as a stack of matrices (Blocks or Depth, Rows, Columns)
array_3d = np.array([[[1, 2, 3], [4, 5, 6]],
                     [[7, 8, 9], [10, 11, 12]],
                     [[13, 14, 15], [16, 17, 18]],
                     [[19, 20, 21], [22, 23, 24]]
                     ])

print(f"\nNumpy array :\n {array_3d}")
print(array_3d.ndim)  # Output: 3
print(array_3d.shape) # Output: (4, 2, 3) -> (Depth/Plates, Rows, Columns)
print(array_3d.size)  # Output: 24 (4 * 2 * 3)