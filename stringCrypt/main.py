import os
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message


if __name__ == "__main__":
    # 키 생성
    key = generate_key()
    print("생성된 키:", key) # 해당 키로 암호화/복호화를 진행한다.

    # 암호화할 문자열
    message = "Hello, world!"

    # 문자열 암호화
    encrypted_message = encrypt_message(message, key)
    print("암호화된 문자열:", encrypted_message)

    # 암호화된 문자열 복호화
    decrypted_message = decrypt_message(encrypted_message, key)
    print("복호화된 문자열:", decrypted_message)




