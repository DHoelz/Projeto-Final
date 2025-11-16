from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_root():
    """Testa o endpoint ROOT da aplicação"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Bem-vindo à SecureCipher API!"


def test_health_check():
    """Testa o endpoint de health check"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_encryption():
    """Testa se a criptografia está funcionando corretamente"""
    test_message = "Mensagem para teste do endpoint"
    payload = {
        "crypto_type": "fernet",
        "length": len(test_message),
        "text": test_message,
    }

    response = client.post("/encrypt", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()
    assert response.json()["crypto_type"] == "Fernet"
    assert response.json()["version"] is not None


def test_encryption_and_decryption():
    """Testa criptografia e descriptografia completa"""
    test_message = "Mensagem para teste do endpoint"

    # 1. Criptografa
    encrypt_payload = {
        "crypto_type": "fernet",
        "length": len(test_message),
        "text": test_message,
    }

    encrypt_response = client.post("/encrypt", json=encrypt_payload)
    assert encrypt_response.status_code == 200
    encrypted_token = encrypt_response.json()["token"]

    # 2. Descriptografa o token gerado
    decrypt_payload = {"token": encrypted_token, "length": len(encrypted_token)}

    decrypt_response = client.post("/decrypt", json=decrypt_payload)
    assert decrypt_response.status_code == 200
    assert decrypt_response.json()["text"] == test_message
