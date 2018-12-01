import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


# compute error between given line model and observed data
def error(line, data):
    # line: tuple/list/arr (c0, c1) where c0 is slope and c1 is y-intercept
    # data: 2d arr where each row is a point (x, y)
    # returns sum of squared y-axis differences
    err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1])) ** 2)
    return err

def fit_line(data, error_func):
    l = np.float32([0, np.mean(data[:, 1])])
    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0] * x_ends + l[1], 'm--', linewidth=2.0, label='Initial Guess')

    result = spo.minimize(error_func, l, args=(data,), method='SLSQP', options={'disp': True})
    return result.x


orig_line = np.float32([4, 2])
print('Original line: c0 = {}, c1 = {}'.format(orig_line[0], orig_line[1]))
x = np.linspace(0, 10, 21)
y = orig_line[0] * x + orig_line[1]
plt.plot(x, y, 'b--', linewidth=2.0, label='Original Line')

# generate noisy data points
noise_sigma = 3.0
noise = np.random.normal(0, noise_sigma, y.shape)
data = np.asarray([x, y + noise]).T
plt.plot(data[:, 0], data[:, 1], 'go', label='Data Points')

# try to fit a line to this data
l_fit = fit_line(data, error)
print('Fitted line: c0 = {}, c1 = {}'.format(l_fit[0], l_fit[1]))
plt.plot(data[:, 0], l_fit[0] * data[:, 0] + l_fit[1], 'r--', linewidth=2.0, label='Fitted Line')

plt.show()
