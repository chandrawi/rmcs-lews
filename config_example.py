DATABASE = {
    "url_auth" : "postgres://postgres:password@127.0.0.1:5432/test_rmcs_auth",
    "url_resource" : "postgres://postgres:password@127.0.0.1:5432/test_rmcs_resource",
    "url_external": "postgres://postgres:password@127.0.0.1:5432/defaultdb"
}

SERVER_LOCAL = {
    "address_auth": "127.0.0.1:9001",
    "address_resource": "127.0.0.1:9002",
    "root_password": "r0ot_P4s5w0rd",
    "admin_name": "administrator",
    "admin_password": "Adm1n_P4s5w0rd",
    "user_name": "gundala",
    "user_password": "Us3r_P4s5w0rd"
}

SERVER_MAIN = {
    "address_auth": "api.gundala.co.id:9001",
    "address_resource": "api.gundala.co.id:9002",
    "admin_name": "administrator",
    "admin_password": "Adm1n_P4s5w0rd",
}

API = {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "lews",
    "category": "resource",
    "password": "Ap1_P4s5w0rd"
}

GATEWAY_MODBUS = {
    "id": "00000000-0000-0000-0000-000000000000",
    "period_time": 60,
    "serial_port": "/dev/ttyS0"
}

GATEWAYS = [
    "00000000-0000-0000-0000-000000000000",
]

TIMING = {
    "transfer_sleep": 1,
    "analysis_sleep": 1
}

STATUS = {
    "logger_modbus_end": "ANALYSIS_1",
    "transfer_local_raw": "DELETE",
    "transfer_local_end": "TRANSFER_SERVER",
    "transfer_server_end": "DELETE",
    "transfer_external_db_begin": "EXTERNAL_OUTPUT",
    "transfer_external_db_end": "DELETE"
}

SOIL_INCLINOMETER_GROUP_ID = "00000000-0000-0000-0000-000000000000"
