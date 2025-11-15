# 🔐 SecureCipher API

Uma API FastAPI para criptografia e descriptografia de textos usando o algoritmo **Fernet** (criptografia simétrica segura).

## 📋 Sobre o Projeto

SecureCipher é uma API RESTful que permite:
- ✅ **Criptografar textos** com segurança usando Fernet
- ✅ **Descriptografar tokens** criptografados
- ✅ **Validação automática** de entrada com Pydantic
- ✅ **Documentação interativa** via Swagger/OpenAPI

## 🏗️ Estrutura do Projeto

```
Projeto Final/
├── src/
│   ├── api/
│   │   └── main.py              # Endpoints da API
│   ├── models/
│   │   └── schemas.py           # Modelos Pydantic (validação)
│   └── config.py                # Configurações da aplicação
├── tests/
│   └── test_*.py                # Testes automatizados
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
CRYPTO_KEY=sua_chave_fernet_aqui
```

> **Dica:** Gere uma chave Fernet com:
> ```python
> from cryptography.fernet import Fernet
> print(Fernet.generate_key().decode())
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
pytest tests/ -v
```

## 📡 Endpoints

### 🔐 POST `/encrypt`

Criptografa um texto.

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

Descriptografa um token.

**Request:**
```json
{
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
  "status": true,
  "message": "API funcionando"
}
```

## 🔧 Customização

### Alterar Tipo de Criptografia

Edite `src/config.py`:
```python
app_crypto_type: str = "Fernet"  # ou outro tipo
```

### Adicionar Novos Endpoints

Edite `src/api/main.py` e crie funções decoradas com `@app.post()`, `@app.get()`, etc.

### Criar Novos Schemas

Edite `src/models/schemas.py` e estenda a classe `BaseModel` do Pydantic.

## 📦 Dependências Principais

- **FastAPI**: Framework web moderno
- **Uvicorn**: Servidor ASGI
- **Pydantic**: Validação de dados
- **cryptography**: Algoritmos criptográficos (Fernet)
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
  -d '{"token": "gAAAAABlYwK9...", "length": 140}'
```

## ⚠️ Segurança

- 🔐 A chave Fernet deve ser armazenada com segurança em variáveis de ambiente
- 🚫 Nunca commite o arquivo `.env` no repositório
- ✅ Use HTTPS em produção

## 📄 Licença

Projeto desenvolvido para fins educacionais na IBMEC.

---

**Desenvolvido com ❤️ | FastAPI + Pydantic + Fernet**

