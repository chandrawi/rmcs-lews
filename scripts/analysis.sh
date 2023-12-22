#!/bin/bash

sleep 15

while :
do

	analysis_sin=$(pgrep -a python | grep -c /home/orangepi/rmcs-gateway/analysis/analysis_soil_inclinometer.py)
	if [ $analysis_sin -eq 0 ]
	then

		printf "rerun soil inclinometer analysis script...\n"
		sudo /home/orangepi/rmcs-gateway/.venv/bin/python /home/orangepi/rmcs-gateway/analysis/analysis_soil_inclinometer.py &

	fi

	analysis_pie=$(pgrep -a python | grep -c /home/orangepi/rmcs-gateway/analysis/analysis_piezometer.py)
	if [ $analysis_pie -eq 0 ]
	then

		printf "rerun piezometer analysis script...\n"
		sudo /home/orangepi/rmcs-gateway/.venv/bin/python /home/orangepi/rmcs-gateway/analysis/analysis_piezometer.py &

	fi

	sleep 5

done
