import serial
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
ser = serial.Serial("COM12",9600)
raw_data = []
k=0

plt.ion()
xs = []

cs1_1 = []
cs1_2 = []
cs1_3 = []
cs1_4 = []
cs1_5 = []

cs2_1 = []
cs2_2 = []
cs2_3 = []
cs2_4 = []
cs2_5 = []

cs3_1 = []
cs3_2 = []
cs3_3 = []
cs3_4 = []
cs3_5 = []

cs4_1 = []
cs4_2 = []
cs4_3 = []
cs4_4 = []
cs4_5 = []

cs5_1 = []
cs5_2 = []
cs5_3 = []
cs5_4 = []
cs5_5 = []

fig = plt.figure()
plt.title("Sensor_Graph",fontsize=10, color="black")
plt.ylabel("Capacitance(pF)")
plt.ylim([0,12])

while True :

    data = ser.readline().decode().split("\t")
    
    k+=1

    if len(data) == 6 :
        del data[5]
        for i in range(len(data)) :
            raw_data.append(float(data[i]))

    if len(raw_data) == 25 :
        rdata = np.asarray(raw_data).reshape(5,5)
        raw_data.clear()

        cs1_1.append(rdata[0][0])
        cs1_2.append(rdata[0][1])
        cs1_3.append(rdata[0][2])
        cs1_4.append(rdata[0][3])
        cs1_5.append(rdata[0][4])

        cs2_1.append(rdata[1][0])
        cs2_2.append(rdata[1][1])
        cs2_3.append(rdata[1][2])
        cs2_4.append(rdata[1][3])
        cs2_5.append(rdata[1][4])

        cs3_1.append(rdata[2][0])
        cs3_2.append(rdata[2][1])
        cs3_3.append(rdata[2][2])
        cs3_4.append(rdata[2][3])
        cs3_5.append(rdata[2][4])

        cs4_1.append(rdata[3][0])
        cs4_2.append(rdata[3][1])
        cs4_3.append(rdata[3][2])
        cs4_4.append(rdata[3][3])
        cs4_5.append(rdata[3][4])

        cs5_1.append(rdata[4][0])
        cs5_2.append(rdata[4][1])
        cs5_3.append(rdata[4][2])
        cs5_4.append(rdata[4][3])
        cs5_5.append(rdata[4][4])

        xs.append(k)

        plt.plot(xs, cs1_1, color="firebrick")
        plt.plot(xs, cs1_2, color="red") 
        plt.plot(xs, cs1_3, color="tomato") 
        plt.plot(xs, cs1_4, color="darksalmon") 
        plt.plot(xs, cs1_5, color="mistyrose")

        plt.plot(xs, cs2_1, color="sienna")
        plt.plot(xs, cs2_2, color="chocolate") 
        plt.plot(xs, cs2_3, color="darkorange") 
        plt.plot(xs, cs2_4, color="burlywood") 
        plt.plot(xs, cs2_5, color="antiquewhite")

        plt.plot(xs, cs3_1, color="darkgreen")
        plt.plot(xs, cs3_2, color="forestgreen") 
        plt.plot(xs, cs3_3, color="lime") 
        plt.plot(xs, cs3_4, color="springgreen") 
        plt.plot(xs, cs3_5, color="mintcream")

        plt.plot(xs, cs4_1, color="darkgreen")
        plt.plot(xs, cs4_2, color="forestgreen") 
        plt.plot(xs, cs4_3, color="lime") 
        plt.plot(xs, cs4_4, color="springgreen") 
        plt.plot(xs, cs4_5, color="mintcream")

        plt.plot(xs, cs5_1, color="midnightblue")
        plt.plot(xs, cs5_2, color="blue") 
        plt.plot(xs, cs5_3, color="royalblue") 
        plt.plot(xs, cs5_4, color="cornflowerblue") 
        plt.plot(xs, cs5_5, color="lavender")

        plt.pause(0.0000001)
        plt.show()