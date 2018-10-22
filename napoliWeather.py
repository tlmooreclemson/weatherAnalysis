"""
# =======================================================================
# Project created on:  21 Oct. 2018
# Last updated on:     22 Oct. 2018
# Created by:          Thomas Moore
# =======================================================================
# Object of this script is to analyze the meteorological data for Napoli.
# This data was downloaded from https://rp5.ru
# =======================================================================
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('napoliWeather_2005_2018.csv', sep = ';') # import the data set
df['Date_Time'] = pd.to_datetime(df['Date_Time'], format = '%d.%m.%Y %H:%M')
# Split all of the time variables
df['year'] = pd.to_datetime(df['Date_Time']).dt.year
df['month'] = pd.to_datetime(df['Date_Time']).dt.month
df['day'] = pd.to_datetime(df['Date_Time']).dt.day
df['hour'] = pd.to_datetime(df['Date_Time']).dt.hour
# ========================================================================
# To drop all times of day in the morning (we want 11 to 23 h)
df = df.drop(df[df.hour < 11].index)
# ========================================================================
# To find the averages over each day.
# cols = df.columns.difference(['Date_Time'])
# df[cols] = df[cols].astype(str).apply(pd.to_numeric, errors = 'coerce')
# df = df.resample('d', on = 'Date_Time').mean().dropna(how = 'all')
# ==========
# Another way to separate the dates could be done like below. Not sure the best way.
df['Dates'] = pd.to_datetime(df['Date_Time']).dt.date # creates a 'date only' column
df_avgTemp = df[['Dates', 'Temp_C']]
df_avgTemp = df_avgTemp.groupby('Dates')
df_avgTemp = df_avgTemp.mean()
df_avgTemp.to_csv('avgTemp.csv', sep = ';')
df_avgTemp = pd.read_csv('avgTemp.csv', sep = ';')
df_avgTemp['Dates'] = pd.to_datetime(df_avgTemp['Dates'], format = '%Y-%m-%d')
df_avgTemp['year'] = pd.to_datetime(df_avgTemp['Dates']).dt.year
df_avgTemp['month'] = pd.to_datetime(df_avgTemp['Dates']).dt.month
df_avgTemp['day'] = pd.to_datetime(df_avgTemp['Dates']).dt.day
df2 = df_avgTemp
# ========================================================================
# Now, we play with this data frame
# !!August Data!!
df_Aug = df2.loc[df2['month'] == 8] # this selects all data from only the month of August
groupDays_Aug = df_Aug.groupby('day')
meanTemp_Aug = groupDays_Aug.mean()
plt.figure()
plt.scatter(df_Aug['day'], df_Aug['Temp_C'], c = df_Aug['year'], cmap = 'plasma')
plt.colorbar()
plt.plot(meanTemp_Aug['Temp_C'], 's', c = 'k')
plt.xlabel('Day of August')
plt.ylabel('Temperature (°C)')
plt.ylim((0, 40))
plt.savefig('fig_AugTemp_mean.pdf', dpi = 300, bbox_inches='tight')
# ==========
df_Sep = df2.loc[df2['month'] == 9]
groupDays_Sep = df_Sep.groupby('day')
meanTemp_Sep = groupDays_Sep.mean()
plt.figure()
plt.scatter(df_Sep['day'], df_Sep['Temp_C'], c = df_Sep['year'], cmap = 'plasma')
plt.colorbar()
plt.plot(meanTemp_Sep['Temp_C'], 's', c = 'k')
plt.xlabel('Day of September')
plt.ylabel('Temperature (°C)')
plt.ylim((0, 40))
plt.savefig('fig_SepTemp_mean.pdf', dpi = 300, bbox_inches='tight')
# ==========
df_Oct = df2.loc[df2['month'] == 10]
groupDays_Oct = df_Oct.groupby('day')
meanTemp_Oct = groupDays_Oct.mean()
plt.figure()
plt.scatter(df_Oct['day'], df_Oct['Temp_C'], c = df_Oct['year'], cmap = 'plasma')
plt.colorbar()
plt.plot(meanTemp_Oct['Temp_C'], 's', c = 'k')
plt.xlabel('Day of October')
plt.ylabel('Temperature (°C)')
plt.ylim((0, 40))
plt.savefig('fig_OctTemp_mean.pdf', dpi = 300, bbox_inches='tight')
# ==========
df_Nov = df2.loc[df2['month'] == 11]
groupDays_Nov = df_Nov.groupby('day')
meanTemp_Nov = groupDays_Nov.mean()
plt.figure()
plt.scatter(df_Nov['day'], df_Nov['Temp_C'], c = df_Nov['year'], cmap = 'plasma')
plt.colorbar()
plt.plot(meanTemp_Nov['Temp_C'], 's', c = 'k')
plt.xlabel('Day of November')
plt.ylabel('Temperature (°C)')
plt.ylim((0, 40))
plt.savefig('fig_NovTemp_mean.pdf', dpi = 300, bbox_inches='tight')
# ==============================================================================
# To plot heat maps, we need the Seaborn package.
# ==============================================================================
import seaborn as sns
# ==========
Aug_heatmap = df_Aug.pivot('year','day','Temp_C')
Sep_heatmap = df_Sep.pivot('year','day','Temp_C')
Oct_heatmap = df_Oct.pivot('year','day','Temp_C')
Nov_heatmap = df_Nov.pivot('year','day','Temp_C')
# ==========
plt.figure()
sns.heatmap(Aug_heatmap, cmap = 'viridis', vmin = 0, vmax = 40)
plt.xlabel('Day of August')
plt.gca().invert_yaxis()
plt.ylabel('Year')
plt.savefig('fig_Aug_heatmap.pdf', dpi = 300, bbox_inches='tight')
# ==========
plt.figure()
sns.heatmap(Sep_heatmap, cmap = 'viridis', vmin = 0, vmax = 40)
plt.xlabel('Day of September')
plt.gca().invert_yaxis()
plt.ylabel('Year')
plt.savefig('fig_Sep_heatmap.pdf', dpi = 300, bbox_inches='tight')
# ==========
plt.figure()
sns.heatmap(Oct_heatmap, cmap = 'viridis', vmin = 0, vmax = 40)
plt.xlabel('Day of October')
plt.gca().invert_yaxis()
plt.ylabel('Year')
plt.savefig('fig_Oct_heatmap.pdf', dpi = 300, bbox_inches='tight')
# ==========
plt.figure()
sns.heatmap(Nov_heatmap, cmap = 'viridis', vmin = 0, vmax = 40)
plt.xlabel('Day of November')
plt.gca().invert_yaxis()
plt.ylabel('Year')
plt.savefig('fig_Nov_heatmap.pdf', dpi = 300, bbox_inches='tight')
