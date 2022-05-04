# In statistics, imputation is the process of replacing missing data with substituted values

import numpy as np
import pandas as pd
df = pd.read_csv('FILENAME.csv')

# Number of cells in a DataFrame
total_number_cells = np.product(df.shape)

# Number of cells missing a value
total_missing_cells = df.isnull().sum()

# Percentage of DataFrame missing a value
total_percentage_missing = (total_missing_cells / total_number_cells) * 100

# Number of missing values in a specific column
data['COLUMN'].isnull().sum()

# Replace missing values in a specific column with its mean value
data['COLUMN'].fillna(data['COLUMN'].mean(), inplace=True)

# Replace missing values in a specific column with its median value
data['COLUMN'].fillna(data['COLUMN'].median(), inplace=True)

# Replace missing values in a specific column with its mode value
data['COLUMN'].fillna(data['COLUMN'].mode(), inplace=True)

# Replace missing values in a specific column with a specific value
data['COLUMN'].fillna('STRING')