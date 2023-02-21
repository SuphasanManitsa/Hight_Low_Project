import numpy as np
A = np.random.choice(a = [1,2,3,4,5,6],size = 4,replace = True)
B = np.random.choice(a = [1,2,3,4,5,6],size = 4,replace = True)
sum = np.array([12,5,17,9])
# print(sum)
g = 1
a = np.where(np.logical_and(sum < 11,g == 0),1,0)
b = np.where(np.logical_and(sum > 11,g == 1),1,0)
vAB = a + b
# print(a)
# print(b)
# print(np.sum(vAB))

k = np.linspace(1,10,10)
def f(a,x):
    return x * (-1)
l = f(k)
print(1,l)