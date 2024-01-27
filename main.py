import base64

q = input("Do you want to encode or decode something?\n[Encode] or [Decode]: ")

if q == 'Encode':
    data = input("what would you like to encode?: ")
    data_bytes = data.encode('ascii')
    base64_bytes = base64.b64encode(data_bytes)
    base64_string = base64_bytes.decode('ascii')
    print(f"Encoded complete: {base64_string}")

elif q == 'Decode':
    b64data = input("What would you like to decode?: ")
    base64_bytes = b64data.encode('ascii')
    data_bytes = base64.b64decode(b64data)
    data = data_bytes.decode('ascii')
    print(f"Decode coomplete: {data}")
else:
    print("Can't run, Try again")

