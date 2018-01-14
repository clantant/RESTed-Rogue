try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
setup(name='Restgame',
	version='0.1',
	author="Eric Timmerman",
	author_email = "eet1992@gmail.com",
	description = ("REST based web game"),
	url="https://github.com/clantant/RESTed-Rogue",
	install_requires=['Flask'],
	packages=['restgame', 'test']
	)
