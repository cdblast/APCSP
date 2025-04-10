# a321_temps_analysis.py
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph and a bar chart
import matplotlib.pyplot as plt
import pandas as pd
import math as math

#THESE ARE THE COMMENTS FROM THE CO2_DATA CSV
# The average CO2 is expressed as parts per million (ppm),,,,
# which is the number of molecules of CO2 in every one million,,,,
# molecules of dried air (water vapor removed).  ,,,,
# Missing months are denoted by -99.99.,,,,
# -1 means no data on the number of days,,,,
#THE COLUMNS Year,Month,decimal_year,Average,#Days

# Load in the data with read_csv()
# TODO #1: change the file name to your data file name
co2_data = pd.read_csv("co2_data.csv", header=0)   # identify the header row
#reads the csv as-is
print(co2_data)
co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
print(co2_data)
co2_data.dropna(subset=['Average'], inplace=True)
print(co2_data)
#now the missing spots are replaced by averages

# TODO #2: Use matplotlib to make a line graph
plt.plot(co2_data['decimal_year'], co2_data['Average'], color='gray')
plt.ylabel('Co2 levels in PPM')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.show()

'''
#FROM A321

# TODO #3: Plot LOWESS in a line graph
plt.plot(co2_data['decimal_year'], co2_data['Month'], color='blue')
plt.show()

# TODO #4: Use matplotlib to make a bar chart
plt.bar(co2_data['Year'], co2_data['Anomaly'], align='center', color='green')
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.show()

# TODO #5: Calculate min, max, and avg anomaly and the corresponding min/max years
min_anomaly = co2_data['Anomaly'][0]
max_anomaly = co2_data['Anomaly'][0]
min_year = co2_data['Year'][0]
max_year = co2_data['Year'][0]
sum_anomaly = 0
avg_anomaly = 0
# find the min, max and calculate the sum
for i in range(len(co2_data['Anomaly'])):
  if (co2_data['Anomaly'][i] < min_anomaly):
    min_anomaly = co2_data['Anomaly'][i]
    min_year = co2_data['Year'][i]
    # new code inside the same for loop
  if (co2_data['Anomaly'][i] > max_anomaly):
    max_anomaly = co2_data['Anomaly'][i]
    max_year = co2_data['Year'][i]
  sum_anomaly += co2_data['Anomaly'][i]
# calculate average
avg_anomaly = sum_anomaly/len(co2_data['Anomaly'])
# print the statistical values
print("The maximum anomaly is:", max_anomaly, "which occured in", max_year)
print("The minimum anomaly is:", min_anomaly, "which occured in", min_year)
print("The average anomaly is:", avg_anomaly)
'''