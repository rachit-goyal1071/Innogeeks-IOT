from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_excel("Components for Robo.xlsx")
x=data['Components']
y=data['Quantity']
plt.bar(x,y)
plt.title("bar plot")
plt.xlabel("day")
plt.ylabel("No")
plt.show()