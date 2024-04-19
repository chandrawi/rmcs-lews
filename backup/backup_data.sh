#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ENV_FILE="${SCRIPT_DIR}/.env"
set -o allexport
source $ENV_FILE
set +o allexport

EPOCH=$(date +%s)
END_SEC=$((EPOCH - (EPOCH % BACKUP_PERIOD)))
BEGIN_SEC=$((END_SEC - BACKUP_PERIOD))
END=$(date +'%Y-%m-%d %H:%M:%S %z' -d "@$END_SEC")
BEGIN=$(date +'%Y-%m-%d %H:%M:%S %z' -d "@$BEGIN_SEC")
echo $BEGIN
echo $END

COLUMNS="\"device_id\",\"model_id\",\"timestamp\",\"data\""
if [ $BACKUP_TABLE = "data_buffer" ]; then
    COLUMNS="\"device_id\",\"model_id\",\"timestamp\",\"data\",\"status\""
fi

psql $DB_URL -c "\copy (SELECT $COLUMNS FROM \"$BACKUP_TABLE\" WHERE \"timestamp\" >= '$BEGIN' AND \"timestamp\" < '$END') to '$BEGIN_SEC.csv' with (format csv, header true);"
