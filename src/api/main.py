from src.config import logger, cipher, settings
from fastapi import FastAPI, HTTPException
from src.models.schemas import TextInput, TextOutput, TokenInput, TokenOutput

# INSTÂNCIA DA API =====================================================
app = FastAPI(
    title=settings.app_name,
    description=settings.app_description, 
    version=settings.app_version
)


# ENDPOINTS ============================================================
@app.get("/")
def root():
    """
    Endpoint raiz da API
    """
    logger.info("Endpoint raiz acessado")
    return {
        "message": "Bem-vindo à SecureCipher API!",
        "version": settings.app_version
    }

@app.get("/health")
def health_check():
    """
    Endpoint de health check
    """
    logger.info("Health check realizado")
    return {
        "status": "healthy", 
        "version": settings.app_version}


# PAREI DE REVISAR AQUI XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
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