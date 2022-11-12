
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)

#quando usar um argumento por referencia como o lista é importante fazer uma copia para 
# não alterar a referncia externa, uma vez que a lista é mutavel

salario = 2000

def salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")


    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)