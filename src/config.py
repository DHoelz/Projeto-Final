import logging
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


# CONFIGURAÇÕES GERAIS =================================================
class Settings(BaseSettings):
    app_name: str = "SecureCipher API"
    app_version: str = "1.0.0"
    app_description: str = (
        "API que criptografa e decriptografa textos usando Fernet e chave via "
        "variável de ambiente"
    )
    app_crypto_type: str = "Fernet"
    # tornar todas as variantes de chave opcionais para que o Settings aceite
    # CRYPTO_KEY_FERNET, CRYPTO_KEY_AES256, CRYPTO_KEY_CHACHA20
    crypto_key_fernet: str | None = None
    crypto_key_aes256: str | None = None
    crypto_key_chacha20: str | None = None
    debug: bool = False

    # carrega do .env e permite variáveis extras (não ignorar)
    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()


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
            logging.StreamHandler(),
        ],
    )

    return logging.getLogger("securecipher")


# LOGGER GLOBAL ========================================================
logger = setup_logging()
logger.info("Logging configurado com sucesso")
