#!/bin/bash

sleep 15

while :
do

	transfer_data=$(pgrep -a python | grep -c /home/orangepi/rmcs-gateway/transfer/transfer_data.py)
	if [ $transfer_data -eq 0 ]
	then

		printf "rerun transfer data script...\n"
		sudo /home/orangepi/rmcs-gateway/.venv/bin/python /home/orangepi/rmcs-gateway/transfer/transfer_data.py &

	fi

	sleep 5

done
