TARGET = /docs
IMAGE = sphinx
DOCKER_COMMAND = docker run --rm -it -v "$$PWD"$(TARGET):/docs $(IMAGE)
PROJECT = math
AUTHOR = 'Taku Ikegami'
LANGUAGE = ja
VERSION = 1.0.0


images:
	docker build --no-cache=true -t $(IMAGE) .

html:
	$(DOCKER_COMMAND) make html

preview: html
	docker run --rm -it -p 7000:8000 -v "$$PWD"$(TARGET):/docs $(IMAGE) sphinx-autobuild --host=0.0.0.0 --port=8000 source/ build/html

quickstart:
	$(DOCKER_COMMAND) sphinx-quickstart \
	-q -p $(PROJECT) -a $(AUTHOR) -l $(LANGUAGE) -v $(VERSION) --sep
