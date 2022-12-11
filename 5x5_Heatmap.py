import matplotlib.animation as animation
import matplotlib.pyplot as plt
import seaborn as sns
import serial
import numpy as np

arduino = serial.Serial("COM12",9600)

#heatmap array 5x5, initial value = 0
heatmap_array= [[0 for col in range(5)]for row in range(5)]

fig = plt.figure()
plt.ion()

x = [0,1,2,3,4]
y = [4,3,2,1,0]

rdata = []

def init () :
    plt.title("Sensor_HeatMap",fontsize=10, color="black")
    plt.ylabel("Intensity")
    plt.xticks(x, labels=["COL1","COL2","COL3","COL4","COL5"])
    plt.yticks(y, labels=["ROW5","ROW4","ROW3","ROW2","ROW1"])

def animate(i) :
    while True :
        data = arduino.readline().decode().split("\t")
        
        if len(data) == 6 :
            del data[5]
            for j in range(len(data)) :
                rdata.append(float(data[j]))

        if len(rdata) == 25 :
            heatmap_array = np.asarray(rdata).reshape(5,5)
            ax = plt.imshow(heatmap_array, aspect='equal', cmap='hsv',interpolation='bilinear', vmin=0,vmax=5)
            rdata.clear()
            return ax

if __name__ == "__main__":
    ani = animation.FuncAnimation(fig,animate,init_func=init,interval=10)
    plt.show()