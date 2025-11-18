import os

# Variáveis para o ambiente de teste
def pytest_configure():
    os.environ.setdefault("crypto_key_fernet", "q7UxUO3F0mvDhxFW1N2tZ9R9oJzYkbU2sZ8v0oXK5xE=")
    os.environ.setdefault("crypto_key_aes256", "4f9c1b8ad4e5c632c31df07bebc2fa31ed923c211c4fd49e18d117a8cc962a4f")     
    os.environ.setdefault("crypto_key_chacha20", "a3d5c8e42fb91bf8327bd49c80d0d63a8c0aef2fba6b571e2ac275f77cc8e942")  