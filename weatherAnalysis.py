"""
# ==============================================================
# Project created on: 19 Oct. 2018
# Last updated on:    20 Oct. 2018
# Created by:         Thomas Moore
# ==============================================================
# The objective of this script is to practice opening .csv files,
# parsing the data within, and making new and interesting plots.
# ==============================================================
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# this is to set the working directory... maybe not necessary.
# os.chdir("/home/chiattomaglio/Dropbox/PythonProjects/WeatherAnalysis")
# import the data frame
df = pd.read_csv('history_export_Basel2.csv', sep = ';')
# import a different data frame where the year-month-day are merged into a single column.
df_parsed = pd.read_csv('history_export_Basel2.csv', sep = ';', parse_dates=[['Year', 'Month', 'Day']])
# Set the year month day column as a datetime class
df_parsed['Year_Month_Day'] = pd.to_datetime(df_parsed['Year_Month_Day'], format ='%Y-%m%d')
# plot the data using matplotlib
plt.figure()
plt.plot(df_parsed['Year_Month_Day'], df_parsed['Temp_C'], '.')
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.savefig('fig_dateTemp.pdf', dpi = 300)
"""
If we want to use the initial data frame (df) and select only specific months (i.e. October), then we need to subset out the months that we are not interested in. This is done easily.
"""
df_Oct = df.loc[df['Month'] == 10] # this selects only the month of October for every year.
plt.figure()
plt.scatter(df_Oct['Day'], df_Oct['Temp_C'], c = df_Oct['Year'], cmap = 'viridis')
plt.colorbar()
plt.xlabel("Day in October")
plt.ylabel("Temperature (°C)")
plt.savefig('fig_OctTemp.pdf', dpi = 300)
"""
I want to find now the mean temperature in October.
"""
group_Days = df_Oct.groupby('Day')
mean_Temps = group_Days.mean()
plt.figure()
plt.scatter(df_Oct['Day'], df_Oct['Temp_C'], c = df_Oct['Year'], cmap = 'viridis', alpha = 0.75)
plt.colorbar()
plt.plot(mean_Temps['Temp_C'], 's', c = 'r')
plt.xlabel("Day in October")
plt.ylabel("Temperature (°C)")
plt.savefig('fig_OctTemp_mean.pdf', dpi = 300)
"""
Another way to look at the October data would be to plot the year vs. the day. Now I will try to plot a 2D heat map.
"""
#import seaborn as sns
#df_heatmap = df_Oct.pivot(df_Oct['Day'], df_Oct['Year'], df_Oct['Temp_C'])
#ax = sns.heatmap(df_heatmap)
#plt.savefig('fig_Oct_heatmap.pdf', dpi = 300)
