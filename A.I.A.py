import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sb

df = pd.read_csv(r'CSV\Stars Original.csv')

X = np.array(df.drop('class', axis = 1))

kmeans = KMeans(n_clusters=2, random_state=21)

kmeans.fit(X)

df['kclass'] = kmeans.labels_

sb.scatterplot(x="class", y="MeanIP", hue="class", data=df)
