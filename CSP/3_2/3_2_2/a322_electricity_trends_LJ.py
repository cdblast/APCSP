# a322_electricity_trends.py
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs 

import matplotlib.pyplot as plt
import pandas as pd

styles = ["ob--", "*r-", ".y-.", "og:", "om--", "*g--"]

# choose countries of interest
#my_countries = ['Canda','Bolivia','Colombia','Brazil','Cuba','United States']
my_countries = ['China', 'Japan','North Korea', 'Nepal', 'India', 'Russia']
#my_countries = ['Nigeria', 'Ethiopia', 'South Africa', 'Kenya', 'Yemen', 'Ghana']

counter = 0

# Load in the data with read_csv()
df = pd.read_csv("elec_access_data.csv", header=0)    # header=0 means there is a header in row 0

# get a list unique countries
unique_countries = df['Entity'].unique()

# Plot the data on a line graph
for c in unique_countries:
  if c in my_countries:
    
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == c]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == c]['Access']

    plt.plot(years, sum_elec, (styles[counter]), label=c)
    counter += 1

  
plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()