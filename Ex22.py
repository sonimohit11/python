# Write a code snippet to check the data types of each column in a DataFrame.
import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "Salary": [50000.0, 45000.5, 52000.0]
})

# Check data types
print("Data types of each column:")
print(df.dtypes)

# Write a code snippet that demonstrates how to fill missing values with the mean of a column.
import pandas as pd
import numpy as np

# Example DataFrame with missing values
df = pd.DataFrame({
    "Age": [30, np.nan, 25, 35, np.nan]
})

print("Before filling missing values:")
print(df)

# Fill NaN with mean of the column
df["Age"].fillna(df["Age"].mean(), inplace=True)

print("\nAfter filling missing values with mean:")
print(df)