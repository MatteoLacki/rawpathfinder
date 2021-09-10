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
run:	
	ve_rawpathfinder/bin/python bin/run.py --debug

test_query:
	ve_rawpathfinder/bin/python bin/query.py M210903* M210903_099_1_1_4795.d M210903_108_1_1_4804.d --host 192.168.1.209 --port 8958
