import os


# Variáveis para o ambiente de teste
def pytest_configure():
    os.environ.setdefault(
        "crypto_key_fernet", "q7UxUO3F0mvDhxFW1N2tZ9R9oJzYkbU2sZ8v0oXK5xE="
    )
    os.environ.setdefault(
        "crypto_key_aes256",
        "buKRQdINqMHI+DQQ6TgRl4BVFUgDQtffKl7lbQDE0ho=",
    )
    os.environ.setdefault(
        "crypto_key_chacha20",
        "ewKDn8wwrANK+I3g3zXiOtWGLyNiOSaVOUwfY5viDzY=",
    )
