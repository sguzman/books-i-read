def exec(path: str) -> bytes:
    fs = open(path, 'rb')
    bn: bytes = fs.read()
    fs.close()

    return bn
