eBot-install:
	python ez_setup.py
	easy_install -U pyserial
	python setup.py install