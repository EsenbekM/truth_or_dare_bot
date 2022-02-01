import base64

message = input()

encoded_data = base64.b64encode(f"{message}".encode())

print(f"Зашифрованное сообщение - {encoded_data}")

decoded_data = base64.decode(f"{encoded_data}".encode())

print(f"Расшифрованное сообщение - {decoded_data}")