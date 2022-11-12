class bicicleta:
    def __init__(self, cor, modelo, ano, valor): #init é um construtor
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
#Self é uma referencia explicita do objeto bicicleta, a instancia do objeto que quero passar. 
# Cor, modelo, ano e valor são as caracteristicas do minha bicicleta.

#Métodos são funções que estão dentro de uma classe. 
# Usaremos para adicionar o comportamento da bicicleta.
    def buzinar(self):
        print("Plim Plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummm...")

    #exibir a instacia para ver os valores do objeto
    #util para fazer representações das classes
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


#Para instancia vou usar uma variavel
#b1 = bicicleta("amarelo", "caloi", 2022, 600)
#print(b1.cor, b1.modelo, b1.ano, b1.valor)
#b1.buzinar()
#b1.parar()
#b1.correr()

b2 = bicicleta("Verde", "monark", 2000, 200)
print(b2)



