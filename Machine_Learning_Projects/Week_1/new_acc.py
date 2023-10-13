import numpy as np
import pandas as pd
import numpy as np
a = np.array([1,2,3,4]).reshape(1, -1) # "a" is a row vector
b = np.array([1,3,6]).reshape(-1, 1) # "b" is a column vector
print(a)
print(b)
c = (a == b)
d = (a * b)
e = (a + b)
f = (a > b)
print(f'c.shape is {c.shape}. d.shape is {d.shape}. e.shape is {e.shape}. f.shape is {f.shape}.')
print('----------')
print('c is ')
print(c)
print('----------')
print('d is ')
print(d)
print('----------')
print('e is ')
print(e)
print('----------')
print('f is ')
print(f)
print('----------')

# def simple_acc(df, theta):
#     g = df['Glucose'].values
#     g_reshape = g.reshape(1,-1)
#     pred = g_reshape >= theta
#     o = df['Outcome'].values
#     o_reshape = o.reshape(1,-1)
#     comparisons = pred == o_reshape
#     truth_values = np.count_nonzero(comparisons)
#     acc = truth_values / comparisons.size
#     return np.array(acc, dtype=float())


# test_array = ([True, True, False])
# print(np.count_nonzero(test_array))
#Accuracy = number of times predicted label matches correct label / total number of prediction