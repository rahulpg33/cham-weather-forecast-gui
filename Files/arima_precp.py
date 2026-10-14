import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
import pandas as pd
import numpy as np

df=pd.read_csv(os.path.join(BASE_DIR, "Precp data.csv"),index_col='Date',parse_dates=True)
df=df.dropna()
print('Precipitation_Data',df.shape)
df.head()

from statsmodels.tsa.stattools import adfuller

def adf_test(dataset):
  dftest = adfuller(dataset, autolag = 'AIC')
  print("1. ADF : ",dftest[0])
  print("2. Probability : ", dftest[1])
  print("3. Lag : ", dftest[2])
  print("4.Observation for ADF Regression and Critical values calculation :", dftest[3])
  print("5. Critical Values :")
  for key, val in dftest[4].items():
      print("\t",key, ": ", val)

adf_test(df['Precipitation'])

from pmdarima import auto_arima
import warnings
warnings.filterwarnings("ignore")

stepwise_fit = auto_arima(df['Precipitation'], 
                          suppress_warnings=True)           

stepwise_fit.summary()

print(df.shape)
train=df.iloc[:-30]
test=df.iloc[-30:]
print(train.shape,test.shape)
print(test.iloc[0],test.iloc[-1])

from statsmodels.tsa.arima.model import ARIMA
model=ARIMA(train['Precipitation'],order=(1,0,1))
model=model.fit()
model.summary()



start=len(train)
end=len(train)+len(test)-1
pred=model.predict(start=start,end=end).rename('ARIMA predictions')
pred
test['Precipitation']
test['Precipitation'].mean()

from sklearn.metrics import mean_squared_error
from math import sqrt
rmse=sqrt(mean_squared_error(pred,test['Precipitation']))
print(rmse)

model2=ARIMA(df['Precipitation'],order=(1,0,1))
model2=model2.fit()
df.tail()

def Precipit(date):
    index_future_dates=pd.date_range(start='2021-12-30',end='2022-01-29')
    index_future_dates=index_future_dates.astype(str)
    precp_pred=model2.predict(start=len(df),end=len(df)+30).rename('ARIMA Predictions')
    precp_pred.index=index_future_dates

    index_future_dates = index_future_dates.tolist()

    for i in range(0,30):
            if index_future_dates[i] == date:
                return precp_pred.iloc[i]

