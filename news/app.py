#!/usr/bin/env python3
import os,json
from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/shiyanlou'
db=SQLAlchemy(app)
client=MongoClient('127.0.0.1',27017)
mgdb=client.shiyanlou

class File(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(80))
	created_time=db.Column(db.DateTime)
	category_id=db.Column(db.Integer,db.ForeignKey('category.id'))
	category=db.relationship('Category')
	content=db.Column(db.Text)

	def __init__(self,title,created_time,category,content):
		self.title=title
		self.created_time=created_time
		self.category=category
		self.content=content

	def __repr__(self):
		return '<File %r>' % self.title

	def add_tag(self,tag_name):
		if mgdb.tag.find({'name':tag_name}):
			return print('Add tag error,Tag already in')
		else:
			mgdb.tag.insert_one({'title_id':self.id,'name':tag_name})

	def remove_tag(self,tag_name):
		mgdb.tag.delete_one({'title_id':self.id,'name':tag_name})

	@property
	def tags(self):
		tag_list=mgdb.tag.find({'title_id':self.id})
		return tag_list


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
	
	file_list=db.session.query(File).all()
	
	return render_template('index.html',article_list=file_list)

@app.route('/files/<file_id>')
def file(file_id):
	filename=db.session.query(File).filter(File.id==file_id).first()

	if filename!=None:		
		article=filename
		category=db.session.query(Category).filter(Category.id==filename.category_id).first()

		return render_template('file.html',article=article,categorys=category.name)
	else:		
		return render_template('404.html')

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

def read_file(file_path):
	with open(file_path,'r') as f:
		file_content=json.loads(f.read())
	return file_content