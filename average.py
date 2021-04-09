import csv
import pandas as pd 
import plotly.figure_factory as ff

df=pd.read_csv('data1.csv')
fig=ff.create_distplot([df['Avg Rating'].tolist()],['average'],show_hist=True)
fig.show()