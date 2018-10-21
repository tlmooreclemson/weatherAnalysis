"""
# =======================================================================
# Project created on:  21 Oct. 2018
# Last updated on:     21 Oct. 2018
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
# ========================================================================
