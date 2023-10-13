import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

g=np.array([100., 200., 140.])
theta=140

def simple_pred_vec(g, theta):
    values = g >= theta  
    return values

print(simple_pred_vec(g, theta))