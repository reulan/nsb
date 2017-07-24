.PHONY : init clean clean-test-dependencies package test test-dependencies secrets

GIT_HASH := $(shell git rev-parse --short HEAD)
GIT_BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
IMAGE_NAME := "mpmsimo/nsb"

package:
	docker build --build-arg GIT_HASH=$(GIT_HASH) -t $(IMAGE_NAME):$(GIT_HASH) .

bash: package 
	docker run --rm \
		-v $(PWD)/credentials.json:/opt/nsb/config/credentials.json \
		$(IMAGE_NAME):$(GIT_HASH) \
        bash

run: package
	docker run --rm -it\
		-v $(PWD)/credentials.json:/opt/nsb/config/credentials.json \
		$(IMAGE_NAME):$(GIT_HASH)

# Don't worry about these due to DockerHub automated builds.
tag: 
	docker tag $(IMAGE_NAME):$(GIT_HASH) $(IMAGE_NAME):latest

push: tag
	docker push $(IMAGE_NAME):$(GIT_HASH)
	docker push $(IMAGE_NAME):latest
