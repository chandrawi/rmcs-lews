#!/bin/bash

sleep 15

while :
do

	transfer_local=$(pgrep -a python | grep -c /opt/rmcs-gateway/transfer/transfer_local.py)
	if [ $transfer_local -eq 0 ]
	then

		printf "rerun transfer local script...\n"
		sudo /opt/rmcs-gateway/.venv/bin/python /opt/rmcs-gateway/transfer/transfer_local.py &

	fi

	transfer_first=$(pgrep -a python | grep -c /opt/rmcs-gateway/transfer/transfer_server_first.py)
	if [ $transfer_first -eq 0 ]
	then

		printf "rerun transfer server first script...\n"
		sudo /opt/rmcs-gateway/.venv/bin/python /opt/rmcs-gateway/transfer/transfer_server_first.py &

	fi

	transfer_last=$(pgrep -a python | grep -c /opt/rmcs-gateway/transfer/transfer_server_last.py)
	if [ $transfer_last -eq 0 ]
	then

		printf "rerun transfer server last script...\n"
		sudo /opt/rmcs-gateway/.venv/bin/python /opt/rmcs-gateway/transfer/transfer_server_last.py &

	fi

	sleep 5

done
