#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:10:13 2020

@author: arturpinto
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates
from datetime import timedelta, datetime

filename = 'Temperature_16_05_2021_16_49_39.csv'

plot_date_start = ''

data = np.genfromtxt(filename)

start_day = int(filename.split('_')[1])
start_month = int(filename.split('_')[2])
start_hour = int(filename.split('_')[4])
start_min = int(filename.split('_')[5])

#date_str = datetime(2021, start_month, start_day, start_hour-4, start_min)
date_str = datetime(2021, start_month, start_day, start_hour, start_min)

print(date_str)

date_list = []

for i in range(len(data)):
    
    date_list.append(date_str + timedelta(seconds=int(data[i,0])))
    
    
dates_mlib = dates.date2num(date_list)

formatter = dates.DateFormatter('%d/%m \n %H:%M')

fig, ax = plt.subplots(figsize=(20,8))

plt.plot_date(dates_mlib, data[:,2], '.-')
#ax.xaxis.set_major_locator(loc)
#ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_minor_locator(dates.HourLocator())


locator = dates.AutoDateLocator(minticks=50, maxticks=15)
formatter = dates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

#ax.set_xlim(dates_mlib[150], dates_mlib[200])

plt.grid(which='both')

plt.show()
