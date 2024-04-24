#!/bin/bash

sleep 15

while :
do

	transfer_local=$(pgrep -a python | grep -c /opt/rmcs-lews/transfer/transfer_local.py)
	if [ $transfer_local -eq 0 ]
	then

		printf "rerun transfer local script...\n"
		/opt/rmcs-lews/.venv/bin/python /opt/rmcs-lews/transfer/transfer_local.py &

	fi

	transfer_ext_db=$(pgrep -a python | grep -c /opt/rmcs-lews/transfer/transfer_external_db.py)
	if [ $transfer_ext_db -eq 0 ]
	then

		printf "rerun transfer external database script...\n"
		/opt/rmcs-lews/.venv/bin/python /opt/rmcs-lews/transfer/transfer_external_db.py &

	fi

	sleep 5

done
