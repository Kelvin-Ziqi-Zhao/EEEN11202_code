import numpy as np


def vector_and_matrix_multiplication():
    # Define vectors
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])

    # Perform vector-matrix multiplication
    r1 = np.dot(v1, v2)  # dot product
    r2 = np.cross(v1, v2)  # cross product

    # Define matrices
    m1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    # Perform matrix multiplication
    r3 = m1 @ m2  # matrix multiplication
    r4 = np.matmul(m1, m2)  # alternative method
    return


if __name__ == "__main__":
    vector_and_matrix_multiplication()
