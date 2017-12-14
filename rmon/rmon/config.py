"""rmon.config
rmon config file
"""

import os 

class DevConfig:
	"""dev env config
	"""

	DEBUG=True
	SQLALCHEMY_TRACK_MODIFICATIONS=False
	SQLALCHEMY_DATABASE_URI='sqlite://'
	TEMPLATES_AUTO_RELOAD=True


class ProductConfig(DevConfig):
	"""product env config
	"""

	DEBUG=False

	#sqlite database file path
	path=os.path.join(os.getcwd(),'rmon.db').replace('\\','/')
	SQLALCHEMY_DATABASE_URI='sqlite:///%s' % path