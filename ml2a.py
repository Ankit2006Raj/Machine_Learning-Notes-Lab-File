import pandas as pd
from sklearn import datasets

# 1. Creating a dataset using pandas
data = {
    'Name': ['Ankit', 'Bittu', 'Chandan', 'Ramu'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df_create = pd.DataFrame(data)
print("Dataset Created using pandas:\n", df_create)

# 2. Loading a CSV dataset using pandas (Assuming 'data.csv' exists)
try:
    df_csv = pd.read_csv('data.csv')
    print("\nDataset Loaded from CSV:\n", df_csv.head())
except FileNotFoundError:
    print("\nCSV file not found. Please check the file path.")

# 3. Loading a dataset using sklearn (Iris dataset)
iris = datasets.load_iris()
df_sklearn = pd.DataFrame(iris.data, columns=iris.feature_names)
df_sklearn['target'] = iris.target
print("\nIris Dataset Loaded from sklearn:\n", df_sklearn.head())
