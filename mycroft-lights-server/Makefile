.PHONY: build


build-for-pi:
	env GOOS=linux GOARCH=arm GOARM=5 go build

build-for-local:
	go build

upload: build-for-pi
	scp ./mycroft-lights-server pi@10.0.22.219: