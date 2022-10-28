import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

df = pd.read_csv('epa-sea-level.csv')
x = df['Year']
y = df ['CSIRO Adjusted Sea Level']
x2 = df[df['Year']>1999]['Year']
y2 = df[df['Year']>1999]['CSIRO Adjusted Sea Level']
years_extended = np.arange(1880,2050,1)
years_extended2 = np.arange(2000,2050,1)
lin = linregress(x,y)
lin2 = linregress(x2,y2)
fig, ax = plt.subplots()
fig = plt.scatter(x,y)
fig = plt.plot(years_extended, lin.slope*years_extended + lin.intercept, 'y', label = f'2050: {round(((lin.slope*2050) + lin.intercept),2)} inches')
fig = plt.plot(years_extended2, lin2.slope*years_extended2 + lin2.intercept, 'g', label = f'2050: {round(((lin2.slope*2050) + lin2.intercept),2)} inches')

plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend(loc='best')
plt.show()


def draw_plot():pass