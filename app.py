import os,re,json
from flask import Flask

def create_app():
	"""创建并初始化Flask app
	returns:
		app(object)：Flask app实例
	"""
	app=Flask('rmon')
	#获取json配置文件名称
	file=os.environ.get('RMON_CONFIG')
	
	#TODO从json_file 中读取配置项并将每一项配置写入app.config中
	with open(file,'r') as f:
		data=re.sub('\s?#.*#?','',f.read())
		data=data.replace('\'','"')
	json_file=json.loads(data)
	if json_file:
		for js in json_file:
			app.config[js.upper()]=json_file[js]

	return app



