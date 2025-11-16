import os
from os import getenv
from typing import Protocol
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305, AESGCM
from src.config import settings

class CipherProto(Protocol):
    def encrypt(self, data: bytes) -> bytes: ...
    def decrypt(self, token: bytes) -> bytes: ...

class FernetCipher:
    def __init__(self, key: bytes):
        self._f = Fernet(key)
    def encrypt(self, data: bytes) -> bytes:
        return self._f.encrypt(data)
    def decrypt(self, token: bytes) -> bytes:
        return self._f.decrypt(token)

class AESGCMCipher:
    def __init__(self, key: bytes):
        self._a = AESGCM(key)
    def encrypt(self, data: bytes) -> bytes:
        nonce = os.urandom(12)
        return nonce + self._a.encrypt(nonce, data, None)
    def decrypt(self, token: bytes) -> bytes:
        nonce, ct = token[:12], token[12:]
        return self._a.decrypt(nonce, ct, None)

class ChaChaCipher:
    def __init__(self, key: bytes):
        self._c = ChaCha20Poly1305(key)
    def encrypt(self, data: bytes) -> bytes:
        nonce = os.urandom(12)
        return nonce + self._c.encrypt(nonce, data, None)
    def decrypt(self, token: bytes) -> bytes:
        nonce, ct = token[:12], token[12:]
        return self._c.decrypt(nonce, ct, None)

def get_cipher(crypto_type: str):
    """
    Retorna uma implementação de cipher baseada no tipo solicitado.
    Busca a chave correta no .env conforme o algoritmo:
      - Fernet: CRYPTO_KEY_FERNET (base64)
      - AES-256: CRYPTO_KEY_AES256 (hexadecimal)
      - ChaCha20: CRYPTO_KEY_CHACHA20 (hexadecimal)
    """
    t = crypto_type.lower()

    if "fernet" in t:
        key_str = settings.crypto_key_fernet
        
        if not key_str:
            raise RuntimeError("CRYPTO_KEY_FERNET não encontrada no .env")

        # Fernet espera base64
        key_bytes = key_str.encode()
        return FernetCipher(key_bytes)

    if "aes" in t:
        key_str = settings.crypto_key_aes256
       
        if not key_str:
            raise RuntimeError("CRYPTO_KEY_AES256 não encontrada no .env")

        # AES-256 espera 32 bytes (chave em hex)
        key_bytes = bytes.fromhex(key_str)

        if len(key_bytes) != 32:
            raise ValueError(f"AES-256 precisa de 32 bytes, recebeu {len(key_bytes)}")
        
        return AESGCMCipher(key_bytes)

    if "chacha" in t:
        key_str = settings.crypto_key_chacha20
        if not key_str:
            raise RuntimeError("CRYPTO_KEY_CHACHA20 não encontrada no .env")

        # ChaCha20 espera 32 bytes (chave em hex)
        key_bytes = bytes.fromhex(key_str)

        if len(key_bytes) != 32:
            raise ValueError(f"ChaCha20 precisa de 32 bytes, recebeu {len(key_bytes)}")

        return ChaChaCipher(key_bytes)

    raise ValueError(f"Tipo de criptografia não suportado: {crypto_type}")