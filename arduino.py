import serial
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
ser = serial.Serial("COM6",9600)

while True :
    cap_value = ser.readline().decode()[:-2].split("\t")
    del cap_value[5]

    for x in range(len(cap_value)) :
        cap_value[x] = float(cap_value[x])

    data = np.asarray(cap_value).reshape(1,5)
    sns.heatmap(data, vmin=-200, vmax=1000)
    plt.title('Heatmap of 1x5 Array_Cap', fontsize=20)
    plt.show()