import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv(r"Data\Ice Cream Ratings.csv")
df1 = df1.set_index('Date')
#df1_graph = df1.plot(kind='bar') #shows the typical bar chart
df1_graph = df1.plot(kind='line', subplots=True) #subplots eparates the t
plt.show() #shows the graph
print(df1)

