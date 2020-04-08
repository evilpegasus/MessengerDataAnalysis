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

print(json.dumps(readfile(), indent = 2, sort_keys=True))