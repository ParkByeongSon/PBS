import serial
import csv
import numpy as np
import pandas as pd
ser = serial.Serial("COM12",9600)
raw_data = []
csv_data = []

header_name = ['ROW1_COL1','ROW1_COL2','ROW1_COL3','ROW1_COL4','ROW1_COL5',
'ROW2_COL1','ROW2_COL2','ROW2_COL3','ROW2_COL4','ROW2_COL5',
'ROW3_COL1','ROW3_COL2','ROW3_COL3','ROW3_COL4','ROW3_COL5',
'ROW4_COL1','ROW4_COL2','ROW4_COL3','ROW4_COL4','ROW4_COL5',
'ROW5_COL1','ROW5_COL2','ROW5_COL3','ROW5_COL4','ROW5_COL5']

k=0

while True :
    data = ser.readline().decode().split("\t")
    
    if len(data) == 6 :
        del data[5]
        for i in range(len(data)) :
            raw_data.append(float(data[i]))

    if len(raw_data) == 25 :
        df = pd.DataFrame(raw_data)
        df = df.transpose()
        k+=1
        raw_data.clear()

        if k == 0 :
            df.to_csv('capacitive_sensor_data.csv', index=False, mode='w', header=header_name)
        
        if k <= 50 :
            df.to_csv('capacitive_sensor_data.csv',index=False, mode='a', header=False)
        
        if k == 50 :
            break



