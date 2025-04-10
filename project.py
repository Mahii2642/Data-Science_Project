import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\Khushi\\OneDrive\\Desktop\\python project\\Dataset_py.csv")

print("Dataset Overview: ")
df

df.info()
df.head()
df.tail()
df.columns
df.shape
df.isnull().sum()

#A. Identify Growth Trends – Analyze how school establishments have changed over the years and predict future trends.

yearly_data = df.groupby('Establishment Year').sum().reset_index()
yearly_data

plt.figure(figsize=(10,5))
sns.lineplot(data=yearly_data, x='Establishment Year', y='Total School', marker='o')
plt.title('Total Schools Established Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Schools')
plt.grid(True)
plt.tight_layout()
plt.show()
