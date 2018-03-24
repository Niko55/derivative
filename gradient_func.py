import numpy as np
import matplotlib.pyplot as plt


x_old = 0.0
x_new = 6.0
eps = 0.01
precision = 0.00001

def f_der(x):
    return 4*x**3 - 9*x**2

while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new = x_old - eps*f_der(x_old)
    
print("The local minima occurs at ", x_new)
plt.plot()
    