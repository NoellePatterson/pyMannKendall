import pymannkendall as mk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# do some testing to make sure it works
x = pd.read_csv('Examples/shampoo.csv',parse_dates=['Month'],index_col='Month')
trend,h,p,z,tau,s,var_s,slope,intercept = mk.original_test(x,0.05)
plt.plot(x)
import pdb; pdb.set_trace()
plot_x = np.linspace(0, max(x.values)[0],60)
y = slope * plot_x + intercept
plt.plot(y)
