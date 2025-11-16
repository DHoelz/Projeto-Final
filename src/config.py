import logging
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from cryptography.fernet import Fernet

# CONFIGURAÇÕES GERAIS =================================================
class Settings(BaseSettings):
    app_name: str = "SecureCipher API"
    app_version: str = "1.0.0"
    app_description: str = "API que criptografa e decriptografa textos usando Fernet e chave via " \
    "variável de ambiente"
    app_crypto_type: str = "Fernet"
    crypto_key: str
    debug: bool = False
    
    model_config = SettingsConfigDict(env_file=".env") 

settings = Settings()


# VERIFICAÇÃO DA CHAVE CRIPTOGRÁFICA + INSTÂNCIA DO FERNET =============
try: 
    cipher = Fernet(settings.crypto_key.encode())
except Exception:
    raise RuntimeError(
        "Erro ao carregar a CRYPTO_KEY do .env. "
        "Verifique se a chave está correta e no formato base64 do Fernet."
    )


# CONFIGURAÇÕES DE LOGGING =============================================
LOG_DIR = Path(__file__).resolve().parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def setup_logging():
    """
    Configura sistema de logging da aplicação
    """
    # Evita logs duplicados devido ao --reload do Uvicorn
    root_logger = logging.getLogger()
    root_logger.handlers.clear()  

    logging.basicConfig(
        level=LOG_LEVEL,
        format=LOG_FORMAT,
        handlers=[
            logging.FileHandler(LOG_DIR / "app.log", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger("securecipher")


# LOGGER GLOBAL ========================================================
logger = setup_logging()
logger.info("Logging configurado com sucesso")