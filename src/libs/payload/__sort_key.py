from . import __column_data as cold


def exec(value: cold.MyData) -> str:
    return value[7]
