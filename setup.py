import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_pc', #this should be unique
	include_package_data=True,
	version = '0.0.3',
	long_description = long_description,
	packages = setuptools.find_packages(),
	python_requires = '>=3.5'
	)
