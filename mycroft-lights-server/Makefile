.PHONY: build

all: build-for-pi upload

build-for-pi:
	env GOOS=linux GOARCH=arm GOARM=5 go build

build-for-local:
	go build

upload:
	scp ./mycroft-lights-server* ./mycroft-autostart.service pi@10.0.22.219:
	ssh pi@10.0.22.219 sudo mv /home/pi/mycroft-lights-server /usr/local/bin/mycroft-lights-server
	ssh pi@10.0.22.219 sudo mv /home/pi/mycroft-lights-server.service /lib/systemd/system/
	ssh pi@10.0.22.219 sudo mv /home/pi/mycroft-autostart.service /lib/systemd/system/
	
	ssh pi@10.0.22.219 sudo systemctl daemon-reload
	ssh pi@10.0.22.219 sudo systemctl restart mycroft-lights-server.service
	ssh pi@10.0.22.219 sudo systemctl restart mycroft-autostart.service
	ssh pi@10.0.22.219 sudo systemctl enable mycroft-lights-server.service
	ssh pi@10.0.22.219 sudo systemctl enable mycroft-autostart.service
	