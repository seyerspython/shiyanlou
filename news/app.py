#!/usr/bin/env python3
import os,json
from flask import Flask,render_template,redirect,url_for

app=Flask(__name__)

@app.route('/')
def index():
	article_list=[]
	path='/home/shiyanlou/files'
	file_list=os.listdir(path)
	for file in file_list:
		file=os.path.join(path,file)
		article_list.append(read_file(file))
	return render_template('index.html',article_list=article_list)

@app.route('/files/<filename>')
def file(filename):
	filename=os.path.join('/home/shiyanlou/files',filename+'.json')
	if os.path.exists(filename):		
		article=read_file(filename)
		return render_template('file.html',article=article)
	else:
		return render_template('404.html')

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

def read_file(file_path):
	with open(file_path,'r') as f:
		file_content=json.loads(f.read())
	return file_content