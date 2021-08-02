import numpy as np
import random
import matplotlib.pyplot as pl
import math

a_original = 5
b_original = 3

N = 50
X = []
Y = []
print "Make noise in data"
for i in range(N):
    noise_x = random.uniform(0, 1)
    noise_y = random.uniform(0, 1) * 50
    x = i + noise_x
    X.append(x)
    Y.append(a_original + b_original * x + noise_y)

print "Start linear regression calculations"
avg_X = np.average(X)
avg_Y = np.average(Y)
avg_XY = 0.0
for i in range(N):
    avg_XY += X[i] * Y[i]
avg_XY /= N

avg_X2 = 0.0
for i in range(N):
    avg_X2 += X[i] ** 2
avg_X2 /= N

b = (avg_XY - avg_X * avg_Y) / (avg_X2 - avg_X ** 2)
a = avg_Y - b * avg_X
print "A and B coefficient are respectively"
print (a, b)
Y_predict = []
for x in X:
    Y_predict.append(a + b * x)
pl.plot(X, Y_predict)
pl.plot(X, Y, 'ro')
pl.show()

print "Calculate Piers coefficient"

print np.cov(X, Y)[1][0] / math.sqrt(np.var(X, ddof=1) * np.var(Y, ddof=1))
corr = np.corrcoef(X, Y)[1][0]

R = corr ** 2
print "Determination coefficient"
print R

Var_data = np.var(Y)
Var_rests = 0
for i in range(N):
    Var_rests += (Y[i] - Y_predict[i]) ** 2
Var_rests /= N

Var_regression = 0
for i in range(N):
    Var_regression += (Y_predict[i] - avg_Y) ** 2
Var_regression /= N
print "Data variance"
print Var_data
print "Rests variance"
print Var_rests
print "Regression variance"
print Var_regression

print "Var_data == Var_rests + Var_regression"
print Var_data, " == ", Var_rests + Var_regression

print "Calculate determination coefficient"
print (Var_data - Var_rests) / Var_data
