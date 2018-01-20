run:
	@sudo python ./app.py

test:
	@python ./relayShow.py

help:
	@echo "---------------------------------------------------------"
	@echo "Python Relay API help"
	@echo ""
	@echo "make run will start the flask server on port 35"
	@echo "for controlling mechanical relays using GPIO pins."
	@echo ""
	@echo "sudo is required to run on port 35, so you'll need"
	@echo "to enter your password, or change the port."
	@echo ""
	@echo "make test will launch a test of the relays where the"
	@echo "16 relays should flip on and back off in succession."
	@echo "---------------------------------------------------------"
