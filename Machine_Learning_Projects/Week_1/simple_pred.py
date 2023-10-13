import numpy as np
import pandas as pd
def simple_pred(df, theta):
    p = df['Glucose'].values
    p_new = p.reshape(1, -1)
    pred = p_new >= theta
    return pred