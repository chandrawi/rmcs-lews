#!/bin/bash

sleep 15

while :
do

	data_logger=$(pgrep -a python | grep -c /home/orangepi/rmcs-gateway/data_logger/logger_modbus.py)
	if [ $data_logger -eq 0 ]
	then

		printf "rerun data logger script...\n"
		sudo /home/orangepi/rmcs-gateway/.venv/bin/python /home/orangepi/rmcs-gateway/data_logger/logger_modbus.py &

	fi

	sleep 5

done
