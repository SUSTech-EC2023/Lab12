import numpy as np

def quadratic(x):
    return np.sum(x**2)

def rastrigin(x):
    A = 10
    return A + np.sum(x**2) - A * np.cos(2 * np.pi * x)

# TODO: Implement your own evolutionary algorithm to optimize the provided objective function, and explore the connection between the no free lunch theory and fitness landscape characteristics.
