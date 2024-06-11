import os
from pathlib import Path

TOKEN_FILE = "token.txt"

def get_token():
    token_path = Path(TOKEN_FILE)
    if token_path.is_file():
        with token_path.open("r") as file:
            return file.readline().strip()
    else:
        with token_path.open("w") as file:
            token = input("Insert your token: ").strip()
            file.write(token)
            return token
