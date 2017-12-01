#!/usr/bin/env python3
import os,json
from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/shiyanlou'
db=SQLAlchemy(app)

class File(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(80))
	created_time=db.Column(db.DateTime)
	category_id=db.Column(db.Integer,db.ForeignKey('category.id'))
	category=db.relationship('Category')
	content=db.Column(db.Text)

	def __init__(self,title,created_time,category_id,content):
		self.title=title
		self.created_time=created_time
		self.category_id=category_id
		self.content=content

	def __repr__(self):
		return '<File %r>' % self.title

class Category(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(80))

	def __init__(self,name):
		self.name=name

	def __repr__(self):
		return '<Category %r>' % self.name
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