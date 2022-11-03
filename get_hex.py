def get_hex(file):
    with open(file, "rb") as f:
        hex = f.read(6)
        return hex.hex().upper()
