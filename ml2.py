import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# (a) Create a Series using pandas and display  
data = pd.Series([10, 20, 30, 40, 50])
print("Pandas Series:\n", data)

# (b) Access the index and values of our Series  
print("\nIndexes:", data.index)
print("Values:", data.values)

# (c) Compare an array using NumPy with a series using pandas  
numpy_array = np.array([10, 20, 30, 40, 50])
pandas_series = pd.Series(numpy_array)
print("\nNumPy Array:", numpy_array)
print("Pandas Series:\n", pandas_series)
print("Are they equal?", np.array_equal(numpy_array, pandas_series.values))

# (d) Define Series objects with individual indices  
custom_series = pd.Series([100, 200, 300, 400], index=['a', 'b', 'c', 'd'])
print("\nSeries with Custom Indices:\n", custom_series)

# (e) Access single value of a series  
print("\nValue at index 'b':", custom_series['b'])
print("Value at position 2:", custom_series.iloc[2])

# (f) Load datasets in a DataFrame variable using pandas  
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
print("\nDataset Loaded in DataFrame:\n", df.head())

# (g) Usage of different methods in Matplotlib  
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Sine Wave", color='b')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Example of Matplotlib Usage")
plt.legend()
plt.grid(True)
plt.show()
