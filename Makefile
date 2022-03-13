compile:
	python3 setup.py bdist_wheel

upload:
	python3 -m twine upload dist/*
