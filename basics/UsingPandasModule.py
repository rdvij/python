import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Basic DataFrame operations
print("\nSummary Statistics:")
print(df.describe())

print("\nDataFrame Info:")
print(df.info())

print("\nSelecting a column:")
print(df['Name'])

print("\nFiltering rows where Age > 30:")
print(df[df['Age'] > 30])