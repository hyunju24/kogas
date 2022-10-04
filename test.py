import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from datetime import datetime

data = pd.read_csv('월별공급량및비중.csv')
data["ID"] = pd.date_range("1996-01-01", "1998-12-01", freq="MS")

civil = data["도시가스(톤)_민수용"]
civil.index = data["ID"]
print(civil.head())
civil.plot(subplots=True)