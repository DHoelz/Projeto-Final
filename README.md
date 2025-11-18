# 🔐 SecureCipher API

Uma API FastAPI para criptografia e descriptografia de textos usando o algoritmo **Fernet**, **AES-256** e **ChaCha20-Poly1305** (criptografia simétrica segura).

## 📋 Sobre o Projeto

Trabalho final do módulo Introdução à Engenharia de Software aplicada a ML do IBMEC.

### 1️⃣ Participantes

  - Daniel Werneck
  - Guilherme Matos
  - David Passos
  - Rafael Rocha

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
│       └── key_gen.py           # Gerador de chaves criptográficas
├── tests/
│   └── test.py                  # Testes automatizados
|   └── conftest.py              # Configurações para os testes automatizados
├── .env                         # Variáveis de ambiente
├── requirements.txt             # Dependências do projeto
└── 
```

## 🚀 Como Usar

### 1️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2️⃣ Gerar Chaves Criptograficas e Configurar Variáveis de Ambiente

Antes de executar a API, é obrigatório gerar as chaves de criptografia utilizadas pelos algoritmos Fernet, AES-256 e ChaCha20.

Para isso, crie um arquivo `.env` na raiz do projeto e execute o script de geração:

```bash
python src/crypto/key_gen.py
```

Esse script criará automaticamente três chaves seguras e exibirá no terminal o bloco completo para ser adicionado ao seu arquivo `.env`, no seguinte formato:

```env
CRYPTO_KEY_FERNET="sua_chave_fernet_aqui"
CRYPTO_KEY_AES256="sua_chave_aes256_aqui"
CRYPTO_KEY_CHACHA20="sua_chave_chacha20_aqui"
```

Basta copiar o conteúdo gerado e colar no seu `.env` antes de iniciar a API.

>**Importante:** Cada algoritmo utiliza sua própria chave e elas **não são intercambiáveis.**
>Nunca reutilize a mesma chave para algoritmos diferentes.

### 3️⃣ Executar a API

```bash
uvicorn src.api.main:app --reload
```

A API estará disponível em `http://localhost:8000`

### 4️⃣ Acessar o Frontend (opcional)

Com a API em execução, você pode utilizar a interface web localizada em `frontend/index.html`.

- Abra o arquivo diretamente no navegador (clicando duas vezes ou via *Open File*).
- Ou sirva a pasta `frontend/` com um servidor HTTP simples, por exemplo:

```bash
cd frontend
python -m http.server 5500
```

Em seguida, acesse no navegador:
  - Frontend: http://localhost:5500

### 5️⃣ Acessar Documentação

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 6️⃣ Rodar Testes

```bash
pytest tests/test.py -v
```

## 📡 Endpoints

### 🔐 POST `/encrypt`

Criptografa um texto, podendo ser utilizado as criptografias "fernet", "aes256" e "chacha20".

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

Descriptografa um token criptografado com "fernet", "aes256" e "chacha20".

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

Raiz (Root) da aplicação com mensagem de boas vindas.

**Response (200):**
```json
{
  "message":"Bem-vindo à SecureCipher API!",
  "version":"1.0.0"
}
```

### 💚 GET `/health`

Health check da API.

**Response (200):**
```json
{
  "status": "healthy",
  "version": "1.0.0"
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

**Desenvolvido com ❤️ | FastAPI + Pydantic + Criptografia Simétrica**