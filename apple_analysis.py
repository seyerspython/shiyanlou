# -*- coding:utf8 -*-

import pandas as pd 

def quarter_volume():
	data=pd.read_csv('apple.csv',header=0,parse_dates=['Date'],index_col=[0])
	data_3m=data.resample('Q-DEC').sum()

	second_volume=data_3m.sort_values(by='Volume')['Volume'][-2]

	return second_volume

print(quarter_volume)