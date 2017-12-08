import sys
import json
import pandas as pd 
import os

def analysis(file,user_id):
	times=0
	minutes=0
	if os.path.isfile(file):
		study_data=pd.read_json(file)
		times=study_data[study_data['user_id']==user_id]['minutes'].count()
		minutes=study_data[study_data['user_id']==user_id]['minutes'].sum()
	else:
		return times,minutes

	return times,minutes

def main():

	file='user_study.json'
	user_id=int('144042')
	list=analysis(file,user_id)
	print(list)

if __name__=='__main__':
	main()