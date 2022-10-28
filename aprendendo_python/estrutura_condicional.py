saldo = 2000

opcao = int(input("Informe uma opção: [1] Sacar \n [2] Extrato: "))

if opcao == 1:
    saque = float(input("Informe a quantia de saque: "))

    if saldo >= saque:
        print("Realizando saque!")

    else:
        print("Saldo insuficiente.")


elif opcao == 2:
    print("Extrato igual: ", saldo)

else:
    sys.exit("Opção inválida")

#Idade para tirar a CNH

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Faça sua CNH aqui!")
elif idade == IDADE_ESPECIAL:
    print("Você pode fazer as aulas teóricas.")
else:
    print("Você precisa ter 18 anos.")


#estrutura condicional if aninhado

saldo = 1000
cheque_especial = 450

opcao = int(input("Informe uma opção: [1] conta_normal \n [2] conta_universitaria: "))


if opcao == 1:
    saque = float(input("Informe o valor do saque: "))

    if saldo >= saque:
        print("Saque realizado com sucesso.")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial.")
    else:
        print("Não foi possível realizar o saque.")

elif opcao == 2:
    saque = float(input("Informe o valor do saque: "))

    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente!")

else:
    print("Conta não localiza.")


#Estrutura condicional if ternário

saldo = 1000
saque = 1500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")