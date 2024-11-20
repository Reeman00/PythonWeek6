# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets

# Load the Iris dataset from sklearn
iris = datasets.load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['species'] = iris.target

# Map species to their names for better readability
data['species'] = data['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Task 1: Load and Explore the Dataset
print("First few rows of the dataset:")
print(data.head())

print("\nDataset information:")
print(data.info())

print("\nChecking for missing values:")
print(data.isnull().sum())

# Since there are no missing values, no cleaning is needed for this dataset
# If you have missing values in your dataset, you can fill or drop them using:
# data = data.dropna()  # Drop missing values
# or
# data = data.fillna(value)  # Fill missing values with a specific value

# Task 2: Basic Data Analysis
print("\nBasic statistics of numerical columns:")
print(data.describe())

# Perform groupings and compute the mean for each species
grouped_data = data.groupby('species').mean()
print("\nMean of numerical columns for each species:")
print(grouped_data)

# Identify patterns or interesting findings
print("\nObservations:")
print("- Setosa generally has the smallest petal and sepal measurements.")
print("- Virginica has the largest petal length and width on average.")

# Task 3: Data Visualization

# 1. Line Chart: Average petal length across species
plt.figure(figsize=(8, 5))
plt.plot(grouped_data.index, grouped_data['petal length (cm)'], marker='o')
plt.title('Average Petal Length Across Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.grid(visible=True, linestyle='--', alpha=0.5)
plt.show()

# 2. Bar Chart: Average sepal width across species
plt.figure(figsize=(8, 5))
sns.barplot(x=grouped_data.index, y=grouped_data['sepal width (cm)'])
plt.title('Average Sepal Width Across Species')
plt.xlabel('Species')
plt.ylabel('Sepal Width (cm)')
plt.show()

# 3. Histogram: Distribution of petal length
plt.figure(figsize=(8, 5))
sns.histplot(data['petal length (cm)'], bins=20, kde=True)
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot: Sepal length vs. petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(x=data['sepal length (cm)'], y=data['petal length (cm)'], hue=data['species'])
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
