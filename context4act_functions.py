import pandas as pd
from itertools import cycle
import numpy as np
import datetime as dt
# from sklearn import linear_model
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None 
import seaborn as sns; sns.set()
import pickle

df_JULY = pd.read_pickle('/content/drive/My Drive/DFKI/Context4Act/df_JULY_big.pkl')

df_NOVEMBER = pd.read_pickle('/content/drive/My Drive/DFKI/Context4Act/df_NOVEMBER_big.pkl')

def replace_french(data_frame):

  data_frame.Sensor_measure.replace('Vaisselle', 'Dishes', regex=True, inplace=True)#Replace Vaisselle with dishes
  data_frame.Sensor_measure.replace('Loisir', 'Leisure', regex=True, inplace=True)#Replace Loisir with leisure
  data_frame.Sensor_measure.replace('Travail', 'Work', regex=True, inplace=True)#Replace Travail with work
  data_frame.Sensor_measure.replace('Sortir', 'Going_out', regex=True, inplace=True)#Replace Sortir with going out

  return data_frame
  

def first_last(dataframe):
    return dataframe['Sensor_measure'].apply(float).iloc[-1] - dataframe['Sensor_measure'].apply(float).iloc[0]  
  
  
def fridge_door_opening_times(dataframe):

  fridge_door_per_day_dataframe = ((dataframe.Sensor_measure == 'OPEN') & (dataframe['Sensor_id'] == 'C3')) \
                        .groupby(by=pd.to_datetime(dataframe['Timestamp']).dt.date).sum()

  fridge_door_per_day_dataframe = fridge_door_per_day_dataframe.to_frame(name='Door OPEN')

  return fridge_door_per_day_dataframe



