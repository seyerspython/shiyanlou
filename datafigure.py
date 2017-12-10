import sys
import json
import pandas as pd 
import os
import numpy as np 
import matplotlib.pyplot as plt

def analysis(file):
	times=0
	minutes=0
	if os.path.isfile(file):
		study_data=pd.read_json(file)
		df=study_data[['user_id','minutes']].groupby('user_id',as_index=False).sum()
	else:
		return times,minutes

	return df

def out_fig(df):
	fig=plt.figure()
	ax=fig.add_subplot(1,1,1)
	ax.set_title("StudyData")
	ax.set_xlabel("User ID")
	ax.set_ylabel("Study Time")
	ax.plot(df.user_id<1000,df.minutes,)
	fig.show()

def main():

	file='user_study.json'
	out_fig(analysis(file))
	
	

if __name__=='__main__':
	main()