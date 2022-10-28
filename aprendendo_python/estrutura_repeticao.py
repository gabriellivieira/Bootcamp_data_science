#Estrutura de repetição FOR

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"
CONSOANTE = "BCDGJLMPQRS"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

for letra in texto:
    if letra.upper() in CONSOANTE:
        print(letra, end="")

print()


#Estrutura de repetição função built-in range
for numero in range(0,51,5):
    print(numero, end= " ")


#Estrutura de repetição while

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao -- 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Saindo...")

#Palavra reservada - break - para finalizar uma repetição

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero, end=" ")


for numero in range(100):
    
    if numero == 12:
        break

    print(numero, end=" ")

#Palavra reservada - continue - para pular uma situação especifica no laço

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero, end=" ")


for numero in range(100):
    
    if numero == 12:
        continue

    print(numero, end=" ")