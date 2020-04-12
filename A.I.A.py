import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn

data = np.genfromtxt(r"C:\Users\Cliente\Desktop\A.I.A\CSV\brazil_covid19.csv", delimiter=",")

plt.plot(data)
plt.show()

