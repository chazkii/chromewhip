.PHONY: release
release:
	git checkout master
	git pull
	py.test
	bumpversion release
	python setup.py sdist bdist_wheel upload
	bumpversion --no-tag patch
	git push origin master --tags

