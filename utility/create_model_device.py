import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from typing import Union, List
from dataclasses import dataclass
import uuid
from uuid import UUID
import uuid
from rmcs_api_client.auth import Auth
from rmcs_api_client.resource import Resource, DataType
import config


@dataclass
class ModelConfig:
    name: str
    value: Union[int, float, str, None]
    category: str

@dataclass
class Model:
    category: str
    name: str
    description: str
    types: List[DataType]
    configs: List[List[ModelConfig]]

@dataclass
class Type:
    name: str
    description: str
    models: List[str]

@dataclass
class DeviceConfig:
    name: str
    value: Union[int, float, str]
    category: str

@dataclass
class Device:
    serial_number: str
    name: str
    description: str
    type: str
    configs: List[DeviceConfig]

@dataclass
class Group:
    category: str
    name: str
    description: str
    members: List[str]


MODELS = {
    "accelerometer": Model(
        "RAW", 
        "3-axis 16-bit accelerometer", 
        "3 16-bit integer accelerometer output value", 
        [DataType.U16, DataType.U16, DataType.U16],
        []
    ),
    "soil_inclinometer": Model(
        "DATA",
        "XZ-axis soil inclinometer",
        "XZ-axis inclination and displacement, Y-axis parallel with gravity",
        [DataType.F64, DataType.F64, DataType.F64, DataType.F64, DataType.F64, DataType.F64, DataType.F64],
        [
            [
                ModelConfig("scale", "acceleration-X", "SCALE"),
                ModelConfig("unit", "gravity", "UNIT"),
                ModelConfig("symbol", "g", "SYMBOL")
            ],
            [
                ModelConfig("scale", "acceleration-Y", "SCALE"),
                ModelConfig("unit", "gravity", "UNIT"),
                ModelConfig("symbol", "g", "SYMBOL")
            ],
            [
                ModelConfig("scale", "acceleration-Z", "SCALE"),
                ModelConfig("unit", "gravity", "UNIT"),
                ModelConfig("symbol", "g", "SYMBOL")
            ],
            [
                ModelConfig("scale", "inclination-X", "SCALE"),
                ModelConfig("unit", "degree", "UNIT"),
                ModelConfig("symbol", "°", "SYMBOL")
            ],
            [
                ModelConfig("scale", "inclination-Y", "SCALE"),
                ModelConfig("unit", "degree", "UNIT"),
                ModelConfig("symbol", "°", "SYMBOL")
            ],
            [
                ModelConfig("scale", "displacement-X", "SCALE"),
                ModelConfig("unit", "millimeter", "UNIT"),
                ModelConfig("symbol", "mm", "SYMBOL")
            ],
            [
                ModelConfig("scale", "displacement-Y", "SCALE"),
                ModelConfig("unit", "millimeter", "UNIT"),
                ModelConfig("symbol", "mm", "SYMBOL")
            ]
        ]
    ),
    "piezometer_raw": Model(
        "RAW", 
        "piezometer raw data", 
        "16-bit integer pressure and depth value", 
        [DataType.U16, DataType.U16, DataType.U16, DataType.U16],
        []
    ),
    "piezometer_data": Model(
        "DATA",
        "piezometer data",
        "pressure and depth value",
        [DataType.F64, DataType.F64],
        [
            [
                ModelConfig("scale", "pressure", "SCALE"),
                ModelConfig("unit", "pascal", "UNIT"),
                ModelConfig("symbol", "pa", "SYMBOL")
            ],
            [
                ModelConfig("scale", "depth", "SCALE"),
                ModelConfig("unit", "millimeter", "UNIT"),
                ModelConfig("symbol", "mm", "SYMBOL")
            ]
        ]
    ),
    "rain_gauge_raw": Model(
        "RAW", 
        "rain gauge raw data", 
        "16-bit integer rain fall value", 
        [DataType.U16, DataType.U16, DataType.U16, DataType.U16],
        []
    ),
    "rain_gauge_data": Model(
        "DATA",
        "rain gauge data",
        "rain gauge yesterday, daily, last hour, and hourly data",
        [DataType.F64, DataType.F64, DataType.F64, DataType.F64],
        [
            [
                ModelConfig("scale", "rain yesterday", "SCALE"),
                ModelConfig("unit", "millimeter", "UNIT"),
                ModelConfig("symbol", "mm", "SYMBOL")
            ],
            [
                ModelConfig("scale", "rain daily", "SCALE"),
                ModelConfig("unit", "millimeter", "UNIT"),
                ModelConfig("symbol", "mm", "SYMBOL")
            ],
            [
                ModelConfig("scale", "rain last hour", "SCALE"),
                ModelConfig("unit", "millimeter", "UNIT"),
                ModelConfig("symbol", "mm", "SYMBOL")
            ],
            [
                ModelConfig("scale", "rain hourly", "SCALE"),
                ModelConfig("unit", "millimeter", "UNIT"),
                ModelConfig("symbol", "mm", "SYMBOL")
            ]
        ]
    ),
    "environment_raw": Model(
        "RAW", 
        "environment sensor raw data", 
        "16-bit integer temperature, humidity, and pressure value", 
        [DataType.U16, DataType.U16, DataType.U16],
        []
    ),
    "environment_data": Model(
        "DATA",
        "environment sensor data",
        "air temperature, relative humidity, and pressure data",
        [DataType.F64, DataType.F64, DataType.F64],
        [
            [
                ModelConfig("scale", "temperature", "SCALE"),
                ModelConfig("unit", "celcius", "UNIT"),
                ModelConfig("symbol", "°C", "SYMBOL")
            ],
            [
                ModelConfig("scale", "humidity", "SCALE"),
                ModelConfig("unit", "percent", "UNIT"),
                ModelConfig("symbol", "%", "SYMBOL")
            ],
            [
                ModelConfig("scale", "pressure", "SCALE"),
                ModelConfig("unit", "kilo pascal", "UNIT"),
                ModelConfig("symbol", "kPa", "SYMBOL")
            ]
        ]
    )
}

TYPES = {
    "gateway": Type(
        "gateway blank",
        "gateway with no model",
        []
    ),
    "soil_inclinometer": Type(
        "soil inclinometer",
        "3-axis accelerometer and soil inclinometer",
        ["accelerometer", "soil_inclinometer"]
    ),
    "piezometer": Type(
        "piezometer",
        "piezometer with fluid pressure and depth output",
        ["piezometer_raw", "piezometer_data"]
    ),
    "rain_gauge": Type(
        "rain gauge",
        "tipping bucket rain gauge with daily and hourly rain fall output",
        ["rain_gauge_raw", "rain_gauge_data"]
    ),
    "environment": Type(
        "environment sensor",
        "environment sensor with air temperature, relative humidity, and  output",
        ["environment_raw", "environment_data"]
    )
}

GATEWAY = Device(
    "GATE01",
    "Gateway_1",
    "",
    "gateway",
    []
)

DEVICES = [
    Device(
        "TESTACC01",
        "Accelerometer_1",
        "soil inclinometer 1 testing",
        "soil_inclinometer",
        [
            DeviceConfig("slave_id", 0x01, "COMMUNICATION"),
            DeviceConfig("offset-X", 0, "OFFSET"),
            DeviceConfig("offset-Y", 0, "OFFSET"),
            DeviceConfig("offset-Z", 0, "OFFSET"),
            DeviceConfig("space", 1000, "ANALYSIS"),
            DeviceConfig("position", 1, "ANALYSIS")
        ]
    ),
    Device(
        "TESTACC02",
        "Accelerometer_2",
        "soil inclinometer 2 testing",
        "soil_inclinometer",
        [
            DeviceConfig("slave_id", 0x02, "COMMUNICATION"),
            DeviceConfig("offset-X", 0, "OFFSET"),
            DeviceConfig("offset-Y", 0, "OFFSET"),
            DeviceConfig("offset-Z", 0, "OFFSET"),
            DeviceConfig("space", 1000, "ANALYSIS"),
            DeviceConfig("position", 2, "ANALYSIS")
        ]
    ),
    Device(
        "TESTACC03",
        "Accelerometer_3",
        "soil inclinometer 3 testing",
        "soil_inclinometer",
        [
            DeviceConfig("slave_id", 0x03, "COMMUNICATION"),
            DeviceConfig("offset-X", 0, "OFFSET"),
            DeviceConfig("offset-Y", 0, "OFFSET"),
            DeviceConfig("offset-Z", 0, "OFFSET"),
            DeviceConfig("space", 1000, "ANALYSIS"),
            DeviceConfig("position", 3, "ANALYSIS")
        ]
    ),
    Device(
        "TESTACC04",
        "Accelerometer_4",
        "soil inclinometer 4 testing",
        "soil_inclinometer",
        [
            DeviceConfig("slave_id", 0x04, "COMMUNICATION"),
            DeviceConfig("offset-X", 0, "OFFSET"),
            DeviceConfig("offset-Y", 0, "OFFSET"),
            DeviceConfig("offset-Z", 0, "OFFSET"),
            DeviceConfig("space", 1000, "ANALYSIS"),
            DeviceConfig("position", 4, "ANALYSIS")
        ]
    ),
    Device(
        "TESTACC05",
        "Accelerometer_5",
        "soil inclinometer 5 testing",
        "soil_inclinometer",
        [
            DeviceConfig("slave_id", 0x05, "COMMUNICATION"),
            DeviceConfig("offset-X", 0, "OFFSET"),
            DeviceConfig("offset-Y", 0, "OFFSET"),
            DeviceConfig("offset-Z", 0, "OFFSET"),
            DeviceConfig("space", 1000, "ANALYSIS"),
            DeviceConfig("position", 5, "ANALYSIS")
        ]
    ),
    Device(
        "TESTPIE01",
        "Piezometer_1",
        "piezometer testing",
        "piezometer",
        [
            DeviceConfig("slave_id", 0x80, "COMMUNICATION"),
            DeviceConfig("offset-pressure", 0, "OFFSET"),
            DeviceConfig("offset-depth", 0, "OFFSET")
        ]
    ),
    Device(
        "TESTRAG01",
        "Rain_Gauge_1",
        "rain gauge testing",
        "rain_gauge",
        [
            DeviceConfig("slave_id", 0x90, "COMMUNICATION")
        ]
    ),
    Device(
        "TESTENV01",
        "Environment_Sensor_1",
        "environment sensor testing",
        "environment",
        [
            DeviceConfig("slave_id", 0xA0, "COMMUNICATION")
        ]
    )
]

GROUPS = [
    Group(
        "ANALYSIS",
        "soil inclinometer",
        "soil inclinometer testing",
        [
            "TESTACC01",
            "TESTACC02",
            "TESTACC03",
            "TESTACC04",
            "TESTACC05"
        ]
    )
]


# admin login
address_auth = config.SERVER_LOCAL['address_auth']
address_resource = config.SERVER_LOCAL['address_resource']
auth = Auth(address_auth)
login = auth.user_login(config.SERVER_LOCAL['admin_name'], config.SERVER_LOCAL['admin_password'])
resource = Resource(address_resource, login.access_tokens[0].access_token)

# create data model and add data types and configs
model_map = {}
for key, model in MODELS.items():
    model_id = resource.create_model(uuid.uuid4(), model.category, model.name, model.description)
    resource.add_model_type(model_id, model.types)
    for index, configs in enumerate(model.configs):
        for conf in configs:
            resource.create_model_config(model_id, index, conf.name, conf.value, conf.category)
    model_map[key] = model_id

# create type
type_map = {}
for key, type_ in TYPES.items():
    type_id = resource.create_type(uuid.uuid4(), type_.name, type_.description)
    for model_key in type_.models:
        model_id = model_map[model_key]
        resource.add_type_model(type_id, model_id)
    type_map[key] = type_id

# create gateway
gateway_map = {}
# gateway_id = UUID(config.GATEWAY_MODBUS['id'])
gateway_id = uuid.uuid4()
type_id = type_map[GATEWAY.type]
resource.create_gateway(gateway_id, type_id, GATEWAY.serial_number, GATEWAY.name, GATEWAY.description)
for conf in GATEWAY.configs:
    resource.create_gateway_config(gateway_id, conf.name, conf.value, conf.category)
gateway_map[GATEWAY.serial_number] = gateway_id

# create devices
device_map = {}
for device in DEVICES:
    device_id = uuid.uuid4()
    type_id = type_map[device.type]
    resource.create_device(device_id, gateway_id, type_id, device.serial_number, device.name, device.description)
    for conf in device.configs:
        resource.create_device_config(device_id, conf.name, conf.value, conf.category)
    device_map[device.serial_number] = device_id

# create groups
group_map = {}
for group in GROUPS:
    group_id = uuid.uuid4()
    resource.create_group_device(group_id, group.name, group.category, group.description)
    for member in group.members:
        if member in device_map:
            resource.add_group_device_member(group_id, device_map[member])
    group_map[group.name] = group_id

print("LOGIN:")
print("user_id       = {}".format(login.user_id))
print("auth_token    = {}".format(login.auth_token))
for token in login.access_tokens:
    print("api_id        = {}".format(token.api_id))
    print("access_token  = {}".format(token.access_token))
    print("refresh_token = {}".format(token.refresh_token))
print("MODELS:")
for name in model_map:
    print("{}: {}".format(model_map[name], name))
print("TYPES:")
for name in type_map:
    print("{}: {}".format(type_map[name], name))
print("GATEWAY:")
for name in gateway_map:
    print("{}: {}".format(gateway_map[name], name))
print("DEVICES:")
for name in device_map:
    print("{}: {}".format(device_map[name], name))
print("GROUP:")
for name in group_map:
    print("{}: {}".format(group_map[name], name))
