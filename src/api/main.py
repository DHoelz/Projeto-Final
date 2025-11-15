import os, sys
from fastapi import FastAPI, HTTPException
from cryptography.fernet import Fernet
import logging
from dotenv import load_dotenv

# Carrega o .env ANTES de qualquer outra coisa
load_dotenv()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from config import settings
from models.schemas import TextInput, TextOutput, TokenInput, TokenOutput

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description, 
    version=settings.app_version
)

# Carrega a chave criptográfica do .env
def load_crypto_key():
    key = os.getenv("CRYPTO_KEY")
    if not key:
        raise ValueError("CRYPTO_KEY não encontrada no arquivo .env")
    return key.encode()

KEY = load_crypto_key()
cipher = Fernet(KEY)

@app.get("/")
def health_check():
    """Endpoint de health check"""
    return {"status": True, "message": "API funcionando"}

@app.post("/encrypt")
def encrypt_text(data: TextInput) -> TextOutput:
    """Endpoint responsável por criptografar o texto informado."""
    try:
        encrypted = cipher.encrypt(data.text.encode())
        return TextOutput(
            token=encrypted.decode(),
            crypto_type=settings.app_crypto_type,
            version=settings.app_version
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao criptografar o texto: {str(e)}"
        )

@app.post("/decrypt")
def decrypt_text(data: TokenInput) -> TokenOutput:
    """Endpoint para descriptografia do token informado para texto claro"""
    try:
        decrypted = cipher.decrypt(data.token.encode())
        return TokenOutput(
            text=decrypted.decode(),
            crypto_type=settings.app_crypto_type,
            version=settings.app_version
        )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Token inválido ou não pode ser descriptografado."
        )