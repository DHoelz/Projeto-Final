import os
import base64
from cryptography.fernet import Fernet


def gerar_chave_base64(num_bytes: int) -> str:
    """
    Gera uma chave aleatória com num_bytes bytes
    e retorna em formato Base64 (string).
    """
    key = os.urandom(num_bytes)
    return base64.b64encode(key).decode()


def main():
    # Fernet já gera a chave diretamente em Base64
    fernet_key = Fernet.generate_key().decode()

    # AES-256: 32 bytes (256 bits), codificados em Base64
    aes256_key = gerar_chave_base64(32)

    # ChaCha20: 32 bytes, codificados em Base64
    chacha20_key = gerar_chave_base64(32)

    print('# Adicione isso ao seu arquivo .env\n')
    print(f'CRYPTO_KEY_FERNET="{fernet_key}"')
    print(f'CRYPTO_KEY_AES256="{aes256_key}"')
    print(f'CRYPTO_KEY_CHACHA20="{chacha20_key}"')

if __name__ == "__main__":
    main()