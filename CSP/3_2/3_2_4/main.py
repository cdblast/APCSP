import matplotlib as plt
import pandas as pd

# Load in the data with read_csv()
# TODO #1: change the file name to your data file name
df = pd.read_csv("honey.csv", header=0)   # identify the header row


# Clean the data. Add the following code to your program to remove commas in the Value column. Then convert the data to_numeric values.
df['Value'] = df['Value'].str.replace(',', '') #Variations of replace: Unlike temperature data earlier in the lesson, the Value column contains string data so the replace method requires a preceding str.
df['Value'] = pd.to_numeric(df['Value'], errors='coerce') #converts to numeric values, or if failed returned (D) or NaN

#Drop rows with NaN values
df = df.dropna(subset=['Value'])

unique_states = df['State'].unique()
all_honey = []
all_states = []
'''
# without grouping
for state in unique_states:
  honey_data = df[df['State'] == state]['Value']
  print (state, honey_data.sum())
  all_honey.append(honey_data.sum())
  all_states.append(state)

# with grouping
for state in unique_states:
  #This algorithm groups data by state, and then lists the data by year.
  honey_data = df[df['State'] == state].groupby('Year')['Value'] #year and honey value
  print (state, honey_data.sum())
  all_honey.append(honey_data.sum())
  all_states.append(state)
'''

