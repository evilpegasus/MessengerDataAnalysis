from tkinter import Tk
from tkinter.filedialog import askopenfile

import numpy as np
import matplotlib.pyplot as plt
import datetime
import json

def readfile():
    Tk().withdraw()
    file = askopenfile()
    data = json.load(file)
    return data

raw_data = readfile()
#print(json.dumps(raw_data, indent = 2, sort_keys=True))
timestamps = []
for message in raw_data['messages']:
    timestamps.append(message['timestamp_ms'])
#print(timestamps)

#print(raw_data['messages'][0]['timestamp_ms'])

#Plot the timestamps with histogram
#histogram = plt.hist(timestamps, bins=50, color='darkblue')
#plt.show()

#Plot with datetime
dates = []
for time in timestamps:
    dates.append(datetime.datetime.fromtimestamp(float(time)/1000.0))
print(dates)