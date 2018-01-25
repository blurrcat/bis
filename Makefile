.PHONY: clean clean-test clean-pyc
clean: clean-test clean-pyc
ENV:=dev


clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage*
	rm -fr htmlcov
	rm -f junit.xml

install: clean
	pip install -r requirements/${ENV}.txt

lint:
	flake8

lint-changes:
	flake8 $$(git status -s | grep -E '\.py$$' | cut -c 4-)

test .coverage:
	pytest --cov-report=term:skip-covered --cov-fail-under=100 --cov=.

cov: .coverage
	@coverage report --skip-covered

htmlcov: .coverage
	@coverage html --skip-covered
	@echo "open htmlcov/index.html"

htmlcov-debug: clean
	# when coverage is less then 100%, run this to see which
	# parts are not covered
	@$(MAKE) htmlcov -i 
	@open htmlcov/index.html
