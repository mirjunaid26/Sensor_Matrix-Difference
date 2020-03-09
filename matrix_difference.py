"""
Author: Shakeel Ahmad Sheikh
PhD Student MultiSpeech Team LORIA-INRIA
University of Lorraine, France
Web: https://shakeel608.github.io/
"""

import csv
import os
import numpy as np
import pandas as pd

#Nodes = Total Sensors
#Readings: 745 1 extra need to pop it at the end:
def create_matrix_ReadingsVsNodes(files):
    tempr = np.zeros((745, 55))
    #print("files:",files)
    for i, file in enumerate(files):
        #print(i,file)
        data = pd.read_csv(files[i])
        data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

        data = data['td']
        data = data.replace('mq', 0)
        data_len = len(data)
    #print(data)
        tempr[:data_len,i] = data
    return tempr





#Matrix Difference
def reading_difference(tempr):
    print(tempr.shape)
    
    difference = np.zeros((744, tempr.shape[1], tempr.shape[1]))  #Difference Time Series Matrix 54 X 54 X 744 (=24*31)
    for i, item in enumerate(tempr):  #Read data hourly based from all nodes and save the difference in a 3D tensor of shape Difference 
        #print(i)                               
        for j,val in enumerate(item):            
            #print("in second loop",len(item))
            for k, val in enumerate(item):
                difference[i,j,k] = item[j] - item[k]  #Difference / Change the difference function as per your need here

    return difference





def main():

    """Array To save the readings : Size: 745(24hrs * 31 days + last row as zero,
    you can pop that and then you need to set the size accordingly) X 55(Number of Nodes)
    """
    dir = "/home/shsheikh/Music/time_series/Sensor_Matrix-Difference/RADOMEH/"
    temperature =  np.zeros((745,55))
    files = [os.path.join(dir,file) for file in os.listdir(dir) if file.endswith(".csv")]

    temperature = create_matrix_ReadingsVsNodes(files)
    temperature = np.delete(temperature,-1,0) #Delete Nan Row last
    #Save the differences
    difference_matrix = np.zeros((temperature.shape[1], temperature.shape[1], 744))    
    difference_matrix = reading_difference(temperature)
    print(difference_matrix.shape)
    print(difference_matrix[:10,:10])

if __name__ == "__main__":
    main()

