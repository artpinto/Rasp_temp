#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 19:59:03 2021

@author: arturpinto
"""
import Adafruit_DHT as dht
import time 
from datetime import datetime
import numpy as np

out = []

time0 = time.time()
start = datetime.now()
start_str = start.strftime("%d_%m_%Y_%H_%M_%S")

print(start_str)

while True:
    
    now = datetime.now()
    
    print('\t' + str(now)+ '\n')
    
    umid_sum = 0
    temp_sum = 0
    
    for i in range(5):
        
        umid, temp = dht.read_retry(dht.DHT11, 4)
        umid_sum = umid_sum + umid
        temp_sum = temp_sum + temp
        
        umid_avg = umid_sum/5.0
        temp_avg = temp_sum/5.0
        
        out.append([time.time()-time0, temp_avg, umid_avg])
        
        np.savetxt("Temperature_"+start_str+".csv", out)
        
        print('\t {0:.1f} oC \n \t {1:.1f} % \n'.format(temp_avg, umid_avg))
        
        time.sleep(60*10)
    
    