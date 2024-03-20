#!/bin/bash

sleep 15

while :
do

	transfer_data=$(pgrep -a python | grep -c /opt/rmcs-gateway/transfer/transfer_data.py)
	if [ $transfer_data -eq 0 ]
	then

		printf "rerun transfer data script...\n"
		sudo /opt/rmcs-gateway/.venv/bin/python /opt/rmcs-gateway/transfer/transfer_data.py &

	fi

	sleep 5

done
