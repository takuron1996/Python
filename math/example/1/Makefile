SHELL = /bin/bash
PYTHON	= python3
PIP = pip3
FORMAT = yapf
PYLINT = pylint
INSTALL := yapf pylint
LINTRCF	= pylintrc.txt
LINTRST = pylintresult.txt
STYLE = pep8
RUN = example.py

run: format
	@$(PYTHON) -B $(RUN)

format: pip
	@$(FORMAT) -vv -i -r --style $(STYLE) . > /dev/null

lint: format
	@if [ ! -e $(LINTRCF) ]; then $(PYLINT) --generate-rcfile > $(LINTRCF) 2> /dev/null ; fi
	@$(PYLINT) --rcfile=$(LINTRCF) `find . -name "*.py" -print` > $(LINTRST) ; \
	less $(LINTRST)

pip:
	@for pacage in $(INSTALL); \
	do \
		if [ -z `$(PIP) list --format=freeze | grep $${pacage}=` ]; \
		then \
			sudo $(PIP) install $${pacage}; \
		fi \
	done