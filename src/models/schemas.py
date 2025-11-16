from pydantic import BaseModel, Field, ConfigDict


class TextInput(BaseModel):
    """
    Modelo de entrada para criptografar um texto.
    """

    text: str = Field(
        ...,
        description="Texto que será criptografado.",
    )
    crypto_type: str = Field(
        ...,
        description="Tipo de criptografia a ser utilizada (Tipos suportados: 'fernet', aes, chacha).",
    )
    length: int = Field(
        ..., description="Comprimento do texto informado. Para validação ou metadados."
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "text": "Mensagem de teste",
                "crypto_type": "fernet",
                "length": 17,
            }
        }
    )


class TextOutput(BaseModel):
    """
    Modelo de saída para dados criptografados.
    """

    token: str = Field(..., description="Texto criptografado.")
    crypto_type: str = Field(..., description="Tipo de criptografia aplicada.")
    version: str = Field(..., description="Versão da API.")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "token": "gAAAAABpGcWRKnm31PMWpelUzlsj-xPeScERH1ekEr3MjtQug6jxe1hd5QJcoQFSMecb2Eh_UPvEt2tKmtzPns3qsTRYFBvk_u_LJxtoVTw53BoeiS5wdNpwKZ0XhRr9U_zVH2kAeeoK",
                "crypto_type": "Fernet",
                "version": "1.0.0",
            }
        }
    )


class TokenInput(BaseModel):
    """
    Modelo de entrada para descriptografar um token.
    """

    token: str = Field(
        ..., description="Token criptografado que será descriptografado."
    )
    length: int = Field(
        ..., description="Comprimento do token. Opcionalmente usado para validação."
    )
    crypto_type: str = Field(
        ...,
        description="Tipo de criptografia utilizada (Tipos suportados: 'fernet', aes, chacha).",
    )
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "token": "gAAAAABpGcWRKnm31PMWpelUzlsj-xPeScERH1ekEr3MjtQug6jxe1hd5QJcoQFSMecb2Eh_UPvEt2tKmtzPns3qsTRYFBvk_u_LJxtoVTw53BoeiS5wdNpwKZ0XhRr9U_zVH2kAeeoK",
                "length": 140,
                "crypto_type": "fernet",
            }
        }
    )


class TokenOutput(BaseModel):
    """
    Modelo de saída para retornar o texto descriptografado.
    """

    text: str = Field(..., description="Texto descriptografado.")
    crypto_type: str = Field(..., description="Tipo de criptografia utilizada.")
    version: str = Field(..., description="Versão da API.")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "text": "Mensagem de teste",
                "crypto_type": "Fernet",
                "version": "1.0.0",
            }
        }
    )
