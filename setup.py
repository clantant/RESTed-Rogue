try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
setup(name='Restgame',
	version='0.2',
	author="Eric Timmerman",
	author_email = "eet1992@gmail.com",
	description = ("REST based web game"),
	url="https://github.com/clantant/RESTed-Rogue",
	install_requires=['Flask'],
	test_suite="restgame/test",
	packages=['restgame']
	)
