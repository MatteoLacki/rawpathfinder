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
	ve_rawpathfinder/bin/python bin/query.py M210903_008_1_1_4704.d M210903_017_1_1_4713.d M210903_026_1_1_4722.d M210903_035_1_1_4731.d M210903_044_1_1_4740.d M210903_053_1_1_4749.d M210903_063_1_1_4759.d M210903_072_1_1_4768.d M210903_081_1_1_4777.d M210903_090_1_1_4786.d M210903_099_1_1_4795.d M210903_108_1_1_4804.d --host 192.168.178.20 --port 8958
