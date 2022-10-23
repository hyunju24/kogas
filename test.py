# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd
from pandas.tseries.offsets import DateOffset
from statsmodels.tsa.statespace.sarimax import SARIMAX

data = pd.read_csv('월별공급량및비중all.csv')
data["ID"] = pd.date_range("1996-01-01", "2020-12-01", freq="MS")

civil = data["도시가스(톤)_민수용"]
civil.index = data["ID"]
civil = civil.to_frame()
civil.columns=['gas']
civil.index = pd.DatetimeIndex(civil.index.values, freq=civil.index.inferred_freq)

model = SARIMAX(civil['gas'], order=(1,1,3), seasonal_order=(0,1,1,12))
results = model.fit()

pred_date = [civil.index[-1] + DateOffset(months=x) for x in range(0, 169)]
pred_date = pd.DataFrame(index=pred_date[1:], columns=civil.columns)
civil = pd.concat([civil, pred_date])
civil['forecast'] = results.predict(start=300, end=469, dynamic=True)

print(civil)
civil.to_csv("civil_pred.csv", mode='w')