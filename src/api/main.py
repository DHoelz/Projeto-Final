from src.config import logger, settings
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.models.schemas import TextInput, TextOutput, TokenInput, TokenOutput
from src.crypto.factory import get_cipher
import base64

# INSTÂNCIA DA API =====================================================
app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
)

logger.info("API iniciada com sucesso")

# MIDDLEWARES ==========================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ENDPOINTS ============================================================
@app.get("/")
def root():
    """
    Endpoint raiz da API
    """
    logger.info("Endpoint raiz acessado")
    return {"message": "Bem-vindo à SecureCipher API!", "version": settings.app_version}


@app.get("/health")
def health_check():
    """
    Endpoint de health check
    """
    logger.info("Health check realizado")
    return {"status": "healthy", "version": settings.app_version}


@app.post("/encrypt")
def encrypt_text(data: TextInput) -> TextOutput:
    """
    Endpoint responsável por criptografar o texto informado.
    """
    logger.info(
        "Solicitação de criptografia recebida",
        extra={
            "crypto_type": data.crypto_type,
            "text": data.text,
            "length": data.length,
        },
    )

    try:
        cipher = get_cipher(data.crypto_type)
        encrypted = cipher.encrypt(data.text.encode())

        # Codificar em base64 para retornar como string no JSON
        token_b64 = base64.b64encode(encrypted).decode()

        return TextOutput(
            token=token_b64,
            crypto_type=data.crypto_type,
            version=settings.app_version,
        )
    except Exception as e:
        logger.warning(f"Erro ao criptografar o texto: {str(e)}")
        raise HTTPException(
            status_code=400, detail=f"Erro ao criptografar o texto: {str(e)}"
        )


@app.post("/decrypt")
def decrypt_text(data: TokenInput) -> TokenOutput:
    """
    Endpoint para descriptografia do token informado para texto claro
    """
    logger.info(
        "Solicitação de descriptografia recebida",
        extra={
            "token": data.token,
            "length": data.length,
            "crypto_type": data.crypto_type,
        },
    )
    try:
        # Decodificar de base64 antes de descriptografar
        encrypted_bytes = base64.b64decode(data.token)

        cipher = get_cipher(data.crypto_type)
        decrypted = cipher.decrypt(encrypted_bytes)

        return TokenOutput(
            text=decrypted.decode(),
            crypto_type=data.crypto_type,
            version=settings.app_version,
        )
    except Exception as e:
        logger.warning(f"Erro ao descriptografar o token: {str(e)}")
        raise HTTPException(
            status_code=400, detail="Token inválido ou não pode ser descriptografado."
        )
