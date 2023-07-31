import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv('Salary_Data.csv').values # uploading the CSV data

size = data[:,0]
data_len = len(size)

print("***********************************************************************************************************************************")

def loss_function(m, b, points):
    total_error = 0.
    # for i in points:
    for i in range(data_len):
        x = points[i][4]
        y = points[i][5]
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(data_len)

def gradient_descent(m_now: float, b_now: float, points, L):
    m_gradient = 0
    b_gradient = 0
    # print(f"m_now: {m_now}, b_now: {b_now}, L: {L}, m_gradient: {m_gradient}, b_gradient: {b_gradient}")
    n = float(len(points))

    for i in range(data_len):
        x = points[i][4]
        y = points[i][5]

        if math.isnan(x) or math.isnan(y):
            break
        else:
            m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
            b_gradient += -(2/n) * (y - (m_now * x + b_now))
            print(f"m_gradient: {m_gradient}, b_gradient: {b_gradient}")
    
    m = m_now - L * m_gradient
    b = b_now - L * b_gradient
    return [m, b]

m = 0
b = 0
L = 0.001
epochs = 1000

for i in range(epochs):
    m, b = gradient_descent(m, b, data, L)
    print(f"Iteration {i+1}: m = {m}, b = {b}")


plt.scatter(data[:,4], data[:,5], color='#EF6C35')
plt.plot(list(range(0, 50)), [m * x + b for x in range(0, 50)], color='#00ABAB')

plt.show()

# m = 9575.54229447314, b = 25190.857533656308
