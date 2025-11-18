import pytest
from fastapi.testclient import TestClient
from src.api.main import app


@pytest.fixture(scope="module")
def client() -> TestClient:
    """Client de teste da aplicação FastAPI."""
    return TestClient(app)


def test_root(client: TestClient):
    """Valida o endpoint raiz da aplicação."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json().get("message") == "Bem-vindo à SecureCipher API!"


def test_health_check(client: TestClient):
    """Valida o endpoint de health check."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json().get("status") == "healthy"


@pytest.mark.parametrize("crypto_type", ["fernet", "aes", "chacha"])
def test_encryption(client: TestClient, crypto_type: str):
    """Testa o endpoint /encrypt com diferentes algoritmos."""
    test_message = "Mensagem para teste do endpoint de criptografia."

    payload = {
        "crypto_type": crypto_type,
        "length": len(test_message),
        "text": test_message,
    }

    response = client.post("/encrypt", json=payload)
    assert response.status_code == 200, response.text

    data = response.json()

    assert "token" in data and isinstance(data["token"], str) and data["token"]
    assert data.get("crypto_type") == crypto_type
    assert data.get("version") is not None


@pytest.mark.parametrize("crypto_type", ["fernet", "aes", "chacha"])
def test_encryption_and_decryption(client: TestClient, crypto_type: str):
    """Testa criptografia e descriptografia completas."""

    test_message = "Mensagem de teste para ciclo completo."

    # 1) Encriptação
    encrypt_payload = {
        "crypto_type": crypto_type,
        "length": len(test_message),
        "text": test_message,
    }

    encrypt_response = client.post("/encrypt", json=encrypt_payload)
    assert encrypt_response.status_code == 200, encrypt_response.text

    encrypt_data = encrypt_response.json()

    assert "token" in encrypt_data and isinstance(encrypt_data["token"], str) and encrypt_data["token"]
    assert encrypt_data.get("crypto_type") == crypto_type
    assert encrypt_data.get("version") is not None
    
    # 2) Descriptografia
    token = encrypt_data["token"]
    decrypt_payload = {
        "crypto_type": crypto_type,
        "token": token,
        "length": len(token)
    }

    decrypt_response = client.post("/decrypt", json=decrypt_payload)
    assert decrypt_response.status_code == 200, decrypt_response.text

    decrypt_data = decrypt_response.json()

    assert "text" in decrypt_data and isinstance(decrypt_data["text"], str) and decrypt_data["text"]
    assert decrypt_data.get("crypto_type") == crypto_type
    assert decrypt_data.get("version") is not None

    assert decrypt_data["text"] == test_message