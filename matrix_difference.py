import csv
import os
import numpy as np
import pandas as pd
dir = "/home/shsheikh/Music/RADOMEH"

"""Array To save the readings : Size: 745(24hrs * 31 days + last row as zero,
you can pop that and then you need to set the size accordingly) X 55(Number of Nodes)
"""
temperature =  np.zeros((745,55))
files = [os.path.join(dir,file) for file in os.listdir(dir) if file.endswith(".csv")]

#Nodes = Total Sensors
#Readings: 745 1 extra need to pop it at the end:
def create_matrix_ReadingsVsNodes(files):
    global temperature
    #print("files:",files)
    for i, file in enumerate(files):
        print(i,file)
        data = pd.read_csv(files[i])
        data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

        data = data['td']
        data = data.replace('mq', 0)
        data_len = len(data)
    #print(data)
        temperature[:data_len,i] = data
    return temperature




#Save the differences
difference_matrix = np.zeros((temperature.shape[1], temperature.shape[1]))

#Matrix Difference
def reading_difference(temp):
    global difference_matrix
    for i, item in enumerate(temp):
        for j,val in enumerate(item):
            for k, val in enumerate(item):
                difference_matrix[j,k] = item[j] - item[k]  #Difference / Change the difference function as per your need here

    return difference_matrix





def main():
    temperature = create_matrix_ReadingsVsNodes(files)
    temperature = np.delete(temperature,-1,0) #Delete Nan Row last
    #Save the differences
    difference_matrix = np.zeros((temperature.shape[1], temperature.shape[1]))    
    difference_matrix = reading_difference(temperature)
    print(difference_matrix)

if __name__ == "__main__":
    main()

