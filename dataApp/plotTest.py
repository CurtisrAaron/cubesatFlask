#testing matplotlib
import matplotlib as  mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
import numpy as np
import datetime


class main():
    def __init__(self):
        f = open("/var/www/dataApp/dataApp/decData.csv")
        reader = csv.DictReader(f)

        print(reader)

        time = []
        tsolar = []
        px = []
        mx = []
        py = []
        my = []

        for row in reader:
            time.append(row['time'])
            tsolar.append(float(row['Total Solar']))
            px.append(float(row['+x']))
            mx.append(float(row['-x']))
            py.append(float(row['+y']))
            my.append(float(row['-y']))

        print(time)
        print(tsolar)

        fig, ax1 = plt.subplots()
        ax1.set_xlabel('time (s)')
        ax1.set_ylabel('current')
        ax1.plot(time, px, 'r--', marker = 'o', label='+x')
        ax1.plot(time, py, '', marker = 'x', label='+y')
        ax1.plot(time, mx, '', marker = '+', label='-x')
        ax1.plot(time, my,'', marker = '8', label='-y')
        ax1.plot(time, tsolar,'b--',label='total solar')
        ax1.set_ylim(-100,500)

        ax1.legend()

        plt.savefig("/var/www/dataApp/dataApp/static/data.png")
