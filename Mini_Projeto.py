import random

# Gerador de senhas aleatórias

# Solicitação de parâmetros para a senha
quantidade = int(
    input(f"{5 * "="} GERADOR DE SENHAS {5 * "="}\nInforme a quantidade de caracteres que a senha deve conter:\n"))
numeros = input("\nA senha deve conter números? (s/n)\n")
letras_maiusculas = input("\nA senha deve conter letras maiúsculas? (s/n):\n")
letras_minusculas = input("\nA senha deve conter letras minúsculas? (s/n):\n")
char_especial = input("\nA senha deve conter caracteres especiais? (s/n)\n")

# Inicialização da variável
possibilidades = ""

# Looping para a execução da criação da senha
while True:
    if numeros == "s" or numeros == "S":
        possibilidades += "0123456789"

    if letras_maiusculas == "s" or letras_maiusculas == "S":
        possibilidades += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letras_minusculas == "s" or letras_minusculas == "S":
        possibilidades += "abcdefghijklmnopqrstuvwxyz"

    if char_especial == "s" or char_especial == "S":
        possibilidades += "!@#$%&*+_."

    # Geração da senha aleatória dentro dos parâmetros
    senha = random.choices(possibilidades, k=quantidade)
    senha = "".join(senha)

    print(f"\nA sugestão de senha é:\n{senha}\n")
    escolha = int(input("\nDeseja outra sugestão de senha dentro dos mesmos parâmetros?\n[ 1 ] Não\n[ 2 ] Sim\n"))

    if escolha == 1:
        print("Fico feliz que gostou da senha! Até mais.")
        break





