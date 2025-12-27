import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Sample dataset
data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, np.nan, 35, 40, 28],  # Missing value in Age
    'Salary': [50000, 60000, 70000, 80000, 55000]
}
df = pd.DataFrame(data)

# Display Original Data
print("Original Dataset:\n", df)

### 1. Reshaping the Data
reshaped_data = df[['Age', 'Salary']].values.reshape(-1, 2)
print("\nReshaped Data:\n", reshaped_data)

### 2. Filtering the Data (e.g., selecting employees with Salary > 55000)
filtered_df = df[df['Salary'] > 55000]

print("\nFiltered Data (Salary > 55000):\n", filtered_df)

### 3. Merging Two DataFrames
additional_data = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
})
merged_df = pd.merge(df, additional_data, on='ID')
print("\nMerged DataFrame:\n", merged_df)

### 4. Handling Missing Values
df_filled = df.copy()
df_filled['Age'].fillna(df_filled['Age'].mean(), inplace=True)  # Filling missing Age with mean
print("\nDataset after Handling Missing Values:\n", df_filled)

### 5. Feature Normalization (Min-Max Scaling)
scaler = MinMaxScaler()
df_filled[['Age', 'Salary']] = scaler.fit_transform(df_filled[['Age', 'Salary']])
print("\nDataset after Min-Max Normalization:\n", df_filled)
