# 🔐 SecureCipher API

Uma API FastAPI para criptografia e descriptografia de textos usando os algoritmos **Fernet**, **AES-256** e **ChaCha20-Poly1305** (criptografia simétrica segura).

## 📋 Sobre o Projeto

Trabalho final do módulo Introdução à Engenharia de Software aplicada a ML  do IBMEC.

### 1️⃣ Participantes
  - Daniel Werneck
  - Guilherme Matos
  - David Passos

### 2️⃣ Descrição do projeto

SecureCipher é uma API RESTful que permite:
- ✅ **Criptografar e Descriptografar textos** com segurança usando Fernet, AES-256 e ChaCha20-Poly1305
- ✅ **Validação automática** de entrada com Pydantic
- ✅ **Documentação interativa** via Swagger/OpenAPI

## 🏗️ Estrutura do Projeto

```
Projeto Final/
├── frontend/
│   ├── index.html               # Frontend da aplicação   
├── src/
│   ├── api/
│   │   └── main.py              # Endpoints da API
│   ├── models/
│   │   └── schemas.py           # Modelos Pydantic (validação)
│   ├── config.py                # Configurações da aplicação
│   └── crypto/
│       └── factory.py           # Factory das cifras
├── tests/
│   └── test.py                  # Testes automatizados
|   └── conftest.py              # Configurações para os testes automatizados
├── .env                         # Variáveis de ambiente
├── requirements.txt             # Dependências do projeto
└── README.md
```

## 🚀 Como Usar

### 1️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2️⃣ Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
CRYPTO_KEY_FERNET=sua_chave_fernet_aqui
CRYPTO_KEY_AES256=sua_chave_aes_aqui
CRYPTO_KEY_CHACHA20=sua_chave_chacha20_aqui
```

> **Dica:** Gere uma chave Fernet com:
> ```python
> from cryptography.fernet import Fernet
> print(Fernet.generate_key().decode())
> ```

> **Dica:** Gere uma chave AES-256 ou ChaCha20-Poly1305 com:
> ```python
> from Crypto.Random import get_random_bytes
> print(get_random_bytes(32).hex())
> ```

### 3️⃣ Executar a API

```bash
uvicorn src.api.main:app --reload
```

A API estará disponível em `http://localhost:8000`

### 4️⃣ Acessar Documentação

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 5️⃣ Rodar Testes

```bash
pytest tests/test.py -v
```

## 📡 Endpoints

### 🔐 POST `/encrypt`

Criptografa um texto, podendo ser utilizado as criptografias "fernet", "aes" e "chacha".

**Request:**
```json
{
  "text": "Texto que será criptografado",
  "crypto_type": "fernet", 
  "length": 34
}
```

**Response (200):**
```json
{
  "token": "gAAAAABlYwK9oU1k3H...",
  "crypto_type": "fernet",
  "version": "1.0.0"
}
```

### 🔓 POST `/decrypt`

Descriptografa um token criptografado com "fernet", "aes" e "chacha".

**Request:**
```json
{
  "crypto_type": "fernet", 
  "token": "gAAAAABlYwK9oU1k3H...",
  "length": 140
}
```

**Response (200):**
```json
{
  "text": "Texto que será criptografado",
  "crypto_type": "fernet",
  "version": "1.0.0"
}
```

### 💚 GET `/`

Health check da API.

**Response (200):**
```json
{
  "version": "1.0.0",
  "message": "Bem-vindo à SecureCipher API!"
}
```

## 🔧 Customização

### Adicionar Novos Endpoints

Edite `src/api/main.py` e crie funções decoradas com `@app.post()`, `@app.get()`, etc.

### Criar Novos Schemas

Edite `src/models/schemas.py` e estenda a classe `BaseModel` do Pydantic.

## 📦 Dependências Principais

- **FastAPI**: Framework web moderno
- **Uvicorn**: Servidor ASGI
- **Pydantic**: Validação de dados
- **cryptography**: Algoritmos criptográficos
- **pytest**: Framework de testes

## 📝 Exemplo de Uso

```bash
# Criptografar
curl -X POST http://localhost:8000/encrypt \
  -H "Content-Type: application/json" \
  -d '{"text": "Olá Mundo!", "crypto_type": "fernet", "length": 11}'

# Descriptografar
curl -X POST http://localhost:8000/decrypt \
  -H "Content-Type: application/json" \
  -d '{"token": "gAAAAABlYwK9...",  "crypto_type": "fernet", "length": 140}'
```

## ⚠️ Segurança

- 🔐 As chaves devem ser armazenadas com segurança em variáveis de ambiente
- 🚫 Nunca commite o arquivo `.env` no repositório
- ✅ Use HTTPS em produção

## 📄 Licença

Projeto desenvolvido para fins educacionais na IBMEC.

---

**Desenvolvido com ❤️ | FastAPI + Pydantic + Fernet**

