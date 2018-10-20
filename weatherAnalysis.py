"""
# ==============================================================
# Weather Analysis Script
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
os.chdir("/home/chiattomaglio/Dropbox/PythonProjects/WeatherAnalysis")
df = pd.read_csv('history_export_Basel.csv', sep = ';', skiprows = 10)
df_parsed = pd.read_csv('history_export_Basel.csv', sep = ';', skiprows = 10, parse_dates=[['Year', 'Month', 'Day']])
df_parsed['Year_Month_Day'] = pd.to_datetime(df_parsed['Year_Month_Day'], format ='%Y-%m%d')
plt.plot(df_parsed['Year_Month_Day'], df_parsed['Temperature daily mean [2 m above gnd]'], '.')
plt.xlabel("Year")
plt.ylabel("Temperature (C)")
plt.savefig('fig_dateTemp.pdf')

"""
If we want to use the initial data frame (df) and select only specific months (i.e. October), then we need to subset out the months that we are not interested in. This is done easily.
"""
df_Oct = df.loc[df['Month'] == 10] # this selects only the month of October for every year.
plt.scatter(df_Oct['Day'], df_Oct['Temperature daily mean [2 m above gnd]'], c = df_Oct['Year'], cmap = 'viridis')
plt.colorbar()
plt.xlabel("Day in October")
plt.ylabel("Temperature (C)")
plt.show()
