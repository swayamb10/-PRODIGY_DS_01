# import python libraries

import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('population.csv')
df.head()

df.tail()

df.shape

df.info()

df.drop(['Unnamed: 67'],axis=1, inplace = True)

pd.isnull(df).sum()

df.head()

#Selecting specific country for data visualisation
selected_country = 'United States'
country_data = df[df['Country Name'] == selected_country]
country_data

# Extract population data from 1960 to 2022
years = range(1960, 2023)
population_values = country_data.iloc[:, 4:].values.flatten()
population_values

# Plotting the bar chart for population over the years
plt.figure(figsize=(12, 6))
plt.bar(years, population_values, color='purple')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title(f'Population Trend in {selected_country}')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Plotting the histogram of population values
plt.figure(figsize=(8, 5))
plt.hist(population_values, bins=20, color='lightgreen', edgecolor='black')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.title(f'Population Histogram for {selected_country}')
plt.grid(axis='y')
plt.show()

# Extract population data from 1960 to 2022 for all countries
years = range(1960, 2023)
total_population = df.iloc[:, 4:].sum(axis=0)
total_population

#Creating bar chart
# Plotting the bar chart for global population over the years
plt.figure(figsize=(12, 6))
plt.bar(years, total_population, color='skyblue')
plt.xlabel('Year')
plt.ylabel('Global Population')
plt.title('Global Population Trend (1960-2022)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

