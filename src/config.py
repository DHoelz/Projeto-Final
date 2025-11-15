from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Configurações da aplicação"""
    app_name: str = "SecureCipher API"
    app_version: str = "1.0.0"
    app_description: str = "API que criptografa e decriptografa textos usando Fernet e chave via variável de ambiente"
    app_crypto_type: str = "Fernet"
    debug: bool = False
    
    class Config:
        env_file = ".env"
        extra = "ignore" 

settings = Settings()