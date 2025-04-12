import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv("C:\\Users\\mailt\\Desktop\\Number of Schools by Management and Year of Establishment _Report type - State-wise_22 (2).csv")


# Check structure
print(df.head())
print(df.info())
print(df.isnull().sum())


#1. Analyze how school establishments have changed over the years
yearly_data = df.groupby('Year_of_Establishment').size().reset_index(name='School_Count')
plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly_data, x='Year_of_Establishment', y='School_Count', marker='o')
plt.title('Growth in School Establishments Over the Years')
plt.xlabel('Year of Establishment')
plt.ylabel('Number of Schools')
plt.grid(True)
plt.show()


#2. Track and visualize the total number of schools increasing over time.
yearly_data = df.groupby('Establishment Year')['Total School'].sum().reset_index()
yearly_data['Cumulative Count'] = yearly_data['Total School'].cumsum()
plt.figure(figsize=(10, 6))
plt.plot(yearly_data['Establishment Year'], yearly_data['Cumulative Count'], marker='o', color='blue', label='Cumulative Growth')
plt.xlabel('Year')
plt.ylabel('Total Number of Schools (Cumulative)')
plt.title('Cumulative Growth of Schools Over Time')
plt.legend()
plt.grid()
plt.show()


#3. Check if specific years show a spike due to government initiatives or educational.
yearly_data = df.groupby('Establishment Year')['Total School'].sum().reset_index()
yearly_data['Yearly Growth (%)'] = yearly_data['Total School'].pct_change() * 100
threshold = 20
spike_years = yearly_data[yearly_data['Yearly Growth (%)'] > threshold]
print("Spike Years:", spike_years)
plt.figure(figsize=(10, 6))
plt.bar(yearly_data['Establishment Year'], yearly_data['Yearly Growth (%)'], color='skyblue')
plt.axhline(y=threshold, color='red', linestyle='--', label='Spike Threshold')
plt.xlabel('Year')
plt.ylabel('Yearly Growth (%)')
plt.title('Yearly Growth Percentage in School Establishments')
plt.legend()
plt.show()

#4. Regional Distribution of Schools by Management Type.
heatmap_data = df.groupby('Location')[['State Govt', 'Central Govt', 'Private', 'Govt Aided']].sum()
heatmap_data = heatmap_data.fillna(0)
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='Blues', annot=False, linewidths=.5)
plt.title('Comparison of Schools by Management Type Across Regions')
plt.xlabel('Management Type')
plt.ylabel('Region')
plt.show()

#5. Analyze how different management types (State Govt, Central Govt, Private, Govt Aided) have grown over the years (from 2000).
filtered_df = df[df['Establishment Year'] >= 2000]
grouped_data = filtered_df.groupby('Establishment Year')[['State Govt', 'Central Govt', 'Private', 'Govt Aided']].sum()
plt.figure(figsize=(12, 8))
grouped_data.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Management Type Growth Trends Over the Years', fontsize=16)
plt.xlabel('Year of Establishment', fontsize=12)
plt.ylabel('Number of Schools Established', fontsize=12)
plt.legend(title="Management Type", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()





