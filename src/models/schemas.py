from pydantic import BaseModel, Field


class TextInput(BaseModel):
    """
    Modelo de entrada para criptografar um texto.
    """
    text: str = Field(..., min_length=10, description="Texto que será criptografado. Deve conter pelo menos 10 caracteres.")
    crypto_type: str = Field(..., description="Tipo de criptografia a ser utilizada (ex: 'fernet').")
    length: int = Field(..., description="Comprimento do texto informado. Para validação ou metadados.")

    class Config:
        json_schema_extra = {
            "example": {
                "text": "Texto de exemplo para criptografia",
                "crypto_type": "fernet",
                "length": 34
            }
        }


class TextOutput(BaseModel):
    """
    Modelo de saída para dados criptografados.
    """
    token: str = Field(..., description="Texto criptografado.")
    crypto_type: str = Field(..., description="Tipo de criptografia aplicada.")
    version: str = Field(..., description="Versão da API.")

    class Config:
        json_schema_extra = {
            "example": {
                "token": "gAAAAABlYwK9oU1k3H...",
                "crypto_type": "fernet",
                "version": "1.0.0"
            }
        }


class TokenInput(BaseModel):
    """
    Modelo de entrada para descriptografar um token.
    """
    token: str = Field(
        ...,
        description="Token criptografado que será descriptografado."
    )
    length: int = Field(..., description="Comprimento do token. Opcionalmente usado para validação.")

    class Config:
        json_schema_extra = {
            "example": {
                "token": "gAAAAABlYwK9oU1k3H...",
                "length": 140
            }
        }


class TokenOutput(BaseModel):
    """
    Modelo de saída para retornar o texto descriptografado.
    """
    text: str = Field(..., description="Texto descriptografado.")
    crypto_type: str = Field(..., description="Tipo de criptografia utilizada.")
    version: str = Field(..., description="Versão da API.")

    class Config:
        json_schema_extra = {
            "example": {
                "text": "Texto de exemplo já descriptografado",
                "crypto_type": "fernet",
                "version": "1.0.0"
            }
        }
