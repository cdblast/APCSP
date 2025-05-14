# Import pandas and matplotlib libraries
import pandas as pd
import matplotlib.pyplot as plt


# Read the data from the CSV file
df = pd.read_csv("honey.csv", header=0)


# Clean the 'Value' Column by removing commas and converting to numeric form
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')


# Drop rows with missing 'Value' data
df = df.dropna(subset = ['Value'])


# Print the cleaned 'Value column'
print(df['Value'])


# Get unique states from the 'State column
unique_states = df['State'].unique()


# Initialize lists to store results
all_honey = []
all_states = []
all_honey_without_grouping = []


# Calculate honey production sums by year for each state
for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']
  honey_sums = honey_data.sum()
  all_honey.append(honey_sums)
  all_honey_without_grouping.append(honey_sums.sum())
  all_states.append(state)
  #print(state + ": " + )


sorted_states = sorted(zip(all_honey_without_grouping, all_states), reverse=True)
third = len(sorted_states) // 3

all_prod = [state for _, state in sorted_states]


# Process data without grouping
# plt.figure(figsize = (12,8))
plt.bar(df['State'], df['Value'], align='center')
for i, state in enumerate(all_prod):
  honey = all_honey[all_states.index(state)]
  years = honey.index
  plt.plot(years, honey, label=state)
plt.xlabel('Year')
plt.ylabel('Honey Production')
plt.title('Honey Production')
#plt.legend()
plt.show()

'''
# Split states into large, mid-level, and small producers
large_prod = [state for _, state in sorted_states[:third]]
mid_prod = [state for _, state in sorted_states[third:2*third]]
small_prod = [state for _, state in sorted_states[2*third:]]

# Process data without grouping
plt.figure(figsize = (12,8))
for i, state in enumerate(large_prod):
  honey = all_honey[all_states.index(state)]
  years = honey.index
  plt.plot(years, honey, label=state)
plt.xlabel('Year')
plt.ylabel('Honey Production')
plt.title('Honey Production by Large Producers')
plt.legend()
plt.show()

plt.figure(figsize = (12,8))
for i, state in enumerate(mid_prod):
  honey = all_honey[all_states.index(state)]
  years = honey.index
  plt.plot(years, honey, label=state)
plt.xlabel('Year')
plt.ylabel('Honey Production')
plt.legend()
plt.title('Honey Production by Mid Producers')
plt.show()
 
plt.figure(figsize = (12,8))
for i, state in enumerate(small_prod):
  honey = all_honey[all_states.index(state)]
  years = honey.index
  plt.plot(years, honey, label=state)
plt.xlabel('Year')
plt.ylabel('Honey Production')
plt.legend()
plt.title('Honey Production by Small Producers')  
plt.show()'''