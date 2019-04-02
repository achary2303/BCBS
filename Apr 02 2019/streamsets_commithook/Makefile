IMAGE_NAME = streamsets_commithook

.PHONY: build
build: docker-clean
	#s2i create registry.access.redhat.com/rhscl/python-36-rhel7 streamsets_commithook   <---- command used to start, but not correct
	docker build -t $(IMAGE_NAME) .
	s2i build app/streamsets_commithook registry.access.redhat.com/rhscl/python-36-rhel7 $(IMAGE_NAME) -s file://s2i/bin

.PHONY: docker-clean
docker-clean:
	-docker rm $(IMAGE_NAME) --force
	-docker rmi $(IMAGE_NAME) --force

