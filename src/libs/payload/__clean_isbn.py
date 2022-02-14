def exec(raw_isbn: str) -> str:
    return raw_isbn.strip('"=')
