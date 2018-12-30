.PHONY : init clean clean-test-dependencies package test test-dependencies secrets

GIT_HASH := $(shell git rev-parse --short HEAD)
GIT_BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
IMAGE_NAME := "mpmsimo/nsb"
PROJECT_ID := "noobshack-164103"

package:
	docker build --build-arg GIT_HASH=$(GIT_HASH) -t $(IMAGE_NAME):$(GIT_HASH) .

bash: package 
	docker run -it --rm \
		-v $(PWD)/credentials.json:/usr/bin/nsb/config/credentials.json \
		$(IMAGE_NAME):$(GIT_HASH) \
        bash

run: package
	docker run --rm -it\
		-v $(PWD)/credentials.json:/usr/bin/nsb/config/credentials.json \
		$(IMAGE_NAME):$(GIT_HASH)

tag: package
	docker tag $(IMAGE_NAME):$(GIT_HASH) $(IMAGE_NAME):$(GIT_BRANCH)

push: tag
	docker push $(IMAGE_NAME):$(GIT_HASH)
	docker push $(IMAGE_NAME):$(GIT_BRANCH)

local: clean init package
