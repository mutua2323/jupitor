#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Load the CSV files
airports_df = pd.read_csv('airports.csv')
weather_df = pd.read_csv('weather.csv')

# Task 1: Find the northernmost and easternmost airports in the US
# Northernmost airport
northernmost_airport = airports_df.loc[airports_df['lat'].idxmax()]

# Easternmost airport (in the US, the easternmost airport will have the maximum longitude)
easternmost_airport = airports_df.loc[airports_df['lon'].idxmax()]

# Task 2: Determine the windiest New York area airport on February 12th, 2013
# Filtering New York area airports (assuming New York timezone is 'America/New_York')
ny_airports = airports_df[airports_df['tzone'] == 'America/New_York']

# Merging weather data with NY airports data
ny_weather = pd.merge(weather_df, ny_airports, left_on='origin', right_on='faa')

# Filtering for the specific date
weather_on_date = ny_weather[ny_weather['time_hour'].str.startswith('2013-02-12')]

# Finding the windiest airport on that date
windiest_airport = weather_on_date.loc[weather_on_date['wind_speed'].idxmax()]

# Output results
print("Northernmost Airport:", northernmost_airport)
print("Easternmost Airport:", easternmost_airport)
print("Windiest NY Area Airport on 2013-02-12:", windiest_airport[['origin', 'wind_speed', 'time_hour']])


# In[ ]:





# In[ ]:




