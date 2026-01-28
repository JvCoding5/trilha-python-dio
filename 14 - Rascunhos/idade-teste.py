IDADE_LEGAL = 18

idade_atual = int(input("Digite a sua idade>    "))

if idade_atual >= IDADE_LEGAL:
    print("Você é maior de idade.")
elif idade_atual < IDADE_LEGAL:
    print("Você é menor de idade.")
else: 
    print("Idade inválida.")