PROJECT_NAME = rawpathfinder
install:
	virtualenv ve_rawpathfinder
	ve_rawpathfinder/bin/pip install IPython
	ve_rawpathfinder/bin/pip install -e .
upload_test_pypi:
	rm -rf dist || True
	python setup.py sdist
	twine -r testpypi dist/* 
upload_pypi:
	rm -rf dist || True
	python setup.py sdist
	twine upload dist/*
py:
	ve_rawpathfinder/bin/ipython
