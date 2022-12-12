import matplotlib.animation as animation
import matplotlib.pyplot as plt
import seaborn as sns
import serial
import numpy as np

arduino = serial.Serial("COM19",9600)

heatmap_array= [[0 for col in range(5)]for row in range(5)]

x = [0,1,2,3,4]
y = [4,3,2,1,0]

x_labels = ["COL1","COL2","COL3","COL4","COL5"]
y_labels = ["ROW5","ROW4","ROW3","ROW2","ROW1"]

def make_heatmap_array(array) :
    heatmap_array[0][0] = float(array[0])
    heatmap_array[0][1] = float(array[1])
    heatmap_array[0][2] = float(array[2])
    heatmap_array[0][3] = float(array[3])
    heatmap_array[0][4] = float(array[4])

    heatmap_array[1][0] = float(array[5])
    heatmap_array[1][1] = float(array[6])
    heatmap_array[1][2] = float(array[7])
    heatmap_array[1][3] = float(array[8])
    heatmap_array[1][4] = float(array[9])

    heatmap_array[2][0] = float(array[10])
    heatmap_array[2][1] = float(array[11])
    heatmap_array[2][2] = float(array[12])
    heatmap_array[2][3] = float(array[13])
    heatmap_array[2][4] = float(array[14])

    heatmap_array[3][0] = float(array[15])
    heatmap_array[3][1] = float(array[16])
    heatmap_array[3][2] = float(array[17])
    heatmap_array[3][3] = float(array[18])
    heatmap_array[3][4] = float(array[19])
    
    heatmap_array[4][0] = float(array[20])
    heatmap_array[4][1] = float(array[21])
    heatmap_array[4][2] = float(array[22])
    heatmap_array[4][3] = float(array[23])
    heatmap_array[4][4] = float(array[24])

def animate_heat_map() :
    fig = plt.figure()

    data_from_uno = arduino.readline()
    data_from_uno = data_from_uno[:-2].decode()
    string_data_array = data_from_uno.split(" ")

    make_heatmap_array(string_data_array)

    float_data_array = heatmap_array
    ax = plt.imshow(float_data_array, aspect='equal' , interpolation='gaussian')

    def init() :
        plt.clf()

        ax = plt.imshow(float_data_array, aspect='equal', interpolation='gaussian')

    def animate(i) :
        plt.clf()

        plt.title("Sensor_HeatMap",fontsize=10, color="black")
        plt.ylabel("Intensity")
        plt.xticks(x, x_labels)
        plt.yticks(y, y_labels)
        
        data_from_uno = arduino.readline()
        data_from_uno = data_from_uno[:-2].decode()
        string_data_array = data_from_uno.split(" ")

        make_heatmap_array(string_data_array)

        float_data_array = heatmap_array
        ax = plt.imshow(float_data_array, aspect='equal', interpolation='gaussian')

        plt.clim(0,5)
        plt.colorbar()



    anim = animation.FuncAnimation(fig,animate,init_func=init, interval=10)

    plt.show()


if __name__ == "__main__":
    animate_heat_map()


