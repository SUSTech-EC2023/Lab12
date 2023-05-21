# Lab12

This exercise is designed to allow you to explore the optimization of objective functions using your own implementation of an evolutionary algorithm. The aim is to gain an understanding of the connections between the "No Free Lunch" theory and the characteristics of fitness landscapes.

## Provided Code

Two functions have been provided, `quadratic` and `rastrigin`. These are objective functions that you will attempt to optimize.

```python
import numpy as np

def quadratic(x):
    return np.sum(x**2)

def rastrigin(x):
    A = 10
    return A + np.sum(x**2) - A * np.cos(2 * np.pi * x)
```

## Your Task
You are required to implement your own evolutionary algorithm to optimize the provided objective function.
### TODO: Implement your own evolutionary algorithm to optimize the provided objective function, and explore the connection between the no free lunch theory and fitness landscape characteristics.

As part of this, consider how your algorithm performs across different landscapes and why this might be the case. What does this tell you about the "No Free Lunch" theory?

This exercise is designed to enhance your understanding of the underlying principles of evolutionary computation and its applications in problem-solving and optimization. Have fun exploring!
