#!/bin/bash

sleep 15

while :
do

	data_logger=$(pgrep -a python | grep -c /opt/rmcs-gateway/data_logger/logger_modbus.py)
	if [ $data_logger -eq 0 ]
	then

		printf "rerun data logger script...\n"
		sudo /opt/rmcs-gateway/.venv/bin/python /opt/rmcs-gateway/data_logger/logger_modbus.py &

	fi

	sleep 5

done
