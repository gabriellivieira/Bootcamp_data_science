nome = "gabrielli"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo  "

print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

menu = "Gabrielli"

#Utilizando o center a manutenção e elegibilidadedo código aumenta

print(menu.center(14))
print(menu.center(14, "#"))
print("####" + menu + "####")
print("-" .join(menu))

#usando for ao invez de join (recomentado usar o join para essa operação)

for letra in menu:
    print(letra, end="-")
print()

#Interpolação de variáveis

nome = "Gabrielli"
idade = "24"
saldo = 45.6521

#dicionário
dados = {"nome": "Gabrielli", "idade": 24}

print("Nome: {} Idade: {}" .format(nome, idade))
print("Nome: {1} Idade: {0}" .format(idade, nome))
print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {idade}" .format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Saldo: {saldo:8.2f}")
print(f"Nome: {nome} Saldo: {saldo:.2f}")

#Fatiamento de string

nome = "Gabrielli Vieira Santos"

print(nome[0])
print(nome[:10])
print(nome[10:])
print(nome[10:21])
print(nome[10:21:2])
print(nome[:])
print(nome[::-1])
print(nome[-1])


#String de múltipla linhas

name = "Gabrielli"

mensagem = f"""
    Olá, meu nome é {name},
Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos.
"""

print(mensagem)

mensagem = f'''
    Olá, meu nome é {name},
Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos.
'''

print(mensagem)

print(
    """
    ##### MENU ######

    1 - Depositar
    2 - Sacar
    0 - Sair

    #################
    """
)