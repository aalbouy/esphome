from esphome.components import binary_sensor, my_remote_base

DEPENDENCIES = ["remote_receiver"]

CONFIG_SCHEMA = my_remote_base.validate_binary_sensor


async def to_code(config):
    var = await my_remote_base.build_binary_sensor(config)
    await binary_sensor.register_binary_sensor(var, config)
