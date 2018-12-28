GIT_HASH=$(shell git rev-parse --short HEAD)
IMAGE_NAME="mpmsimo/nsb"

docker build --build-arg GIT_HASH=$GIT_HASH -t $IMAGE_NAME:$GIT_HASH .

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

