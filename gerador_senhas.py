import random

tamanho_senha = int(input("Digite o tamanho da senha que você deseja gerar: "))

caracteres = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

senha = "".join(random.sample(caracteres, tamanho_senha))

print(senha)