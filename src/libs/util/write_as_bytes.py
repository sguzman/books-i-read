def exec(path: str, data: bytes) -> None:
    fs = open(path, 'wb')
    fs.write(data)
    fs.close()
