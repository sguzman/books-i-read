from typing import Optional


def exec(path: str, data: Optional[str]) -> None:
    if data is None:
        payload: str = 'null'
        fs = open(path, 'w')
        fs.write(payload)
        fs.close()
    else:
        payload: str = str(data)
        fs = open(path, 'w')
        fs.write(payload)
        fs.close()
