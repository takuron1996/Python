TARGET = /docs
IMAGE = sphinx
DOCKER_COMMAND = docker run --rm -it -v "$$PWD"$(TARGET):/docs $(IMAGE)
PROJECT = math
AUTHOR = 'Taku Ikegami'
LANGUAGE = ja
VERSION = 1.0.0
USER = taku
GROUP = taku


images:
	docker build --no-cache=true -t $(IMAGE) .

html:
	$(DOCKER_COMMAND) make html
	sudo chown -R $(USER):$(GROUP) docs

preview: html
	docker run --rm -it -p 7000:8000 -v "$$PWD"$(TARGET):/docs $(IMAGE) sphinx-autobuild --host=0.0.0.0 --port=8000 source/ build/html;
	sudo chown -R $(USER):$(GROUP) docs

quickstart:
	$(DOCKER_COMMAND) sphinx-quickstart \
	-q -p $(PROJECT) -a $(AUTHOR) -l $(LANGUAGE) -v $(VERSION) --sep
	sudo chown -R $(USER):$(GROUP) docs
