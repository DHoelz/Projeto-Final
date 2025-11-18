import logging
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


# CONFIGURAÇÕES GERAIS =================================================
class Settings(BaseSettings):
    app_name: str = "SecureCipher API"
    app_version: str = "1.0.0"
    app_description: str = (
        "API que criptografa e decriptografa textos usando Fernet, AES-256 ou"
        "ChaCha20."
    )
    crypto_key_fernet: str
    crypto_key_aes256: str
    crypto_key_chacha20: str
    debug: bool = False

    # carrega do .env e permite variáveis extras (não ignorar)
    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()  # type: ignore[call-arg]


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
