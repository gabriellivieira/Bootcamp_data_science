# Python para Cientistas de Dados

## Tipos de dados

Os tipos definem as características e comportamentos de um valor (objeto) para o interpretador. Os tipos subdividem o que pode ser feito com aquele dado especifico e espaço que ira ocupar na memória.

- Números Inteiros : Números pela classe **int**. Ex: 1, 10, 50, -1, -100.
- Números de ponto flutuante: Números racionais representados pela classe **float**. Ex: 1,5,-10,54 … 999278.002
- Booleano: representa verdadeiro e falso na classe **bool**. Em Python booleano é uma sub classe de int, onde qualquer número diferente de 0 representa verdadeiro e o 0 é falso.
- Strings: Usados para representar valores alfanuméricos, na classe **str**.

![Sem título](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/4a42f8ed-ea2e-4d69-9527-a820f0150963)


## Variáveis e constantes

Variáveis são usadas quando o valor de um objeto pode sofrer alterações durante a execução o programa, enquanto as constantes são valores fixos e não altera durante a execução do programa.

Diferentes de outras linguagens que possuem uma palavra reservada para determinar se uma variável é ou não constante, no Python não existe e para determinar se uma variável é constante basta escrever ela em MAIÚSCULO, de acordo com convenção.

### Boas Práticas

- O padrão de nome deve ser em snake case: em nomes onde existe espaço deve ser usado um _ . EX: Total de compras > Total_de_compras
- Escolher nomes sugestivos;
- Nome de constantes todo em maiúsculo.

## Funções de entrada e saída

### Função imput

Função builtin (padrão/nativa) input é usada quando queremos ler dados de entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido na saída padrão(tela) ao usuário.

### Função print

Função builtin print é usada quando queremos apresentar dados na saída padrão. Ela recebe argumentos obrigatórios do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados em set e terminados por end.

## Operadores

[Operadores Aritméticos e Operadores Lógicos em Python](https://pythonacademy.com.br/blog/operadores-aritmeticos-e-logicos-em-python)

### Operadores artméticos

Eles executam operações matemáticas, como adição (+), subtração ( - ), multiplicação ( * ), divisão ( / ) e divisão inteira ( // ).

**Módulo** é um operador que mostra o resto da operação. 

E a **exponenciação** se usa ** .

Para as operações o Python segue a ordem matemática para os calculos. 

![a-ordem-das-operacoes-em-expressoes-matematicas](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/aa0bdbf1-10f3-4416-a196-511d21fe9cd6)


### Operadores de comparação

Utilizados para comparar dois valores, se ele é igual ( == ), maior ( > ), maior ou igual ( > =), menor ( < ), menor ou igual ( < = ) ou diferente ( != ).

### Operadores de atribuição

São utilizados para definir um valor inicial ou redefinir o valor de uma variável ( = ). Também é possível adicionar e somar um valor usando ( += ) e assim por diante com as demais operações aritméticas.

### Operadores lógicos

São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Assim, quando um operador de comparação é usado o resultado será um booleano.

| and | Retorna True se ambas as afirmações forem verdadeiras |
| --- | --- |
| or | Retorna True se uma das afirmações for verdadeira |
| not | Retorna Falso se o resultado for verdadeiro |

### Operadores de identidade

São utilizados para comparar se os mesmos objeto testados ocupam o mesmo espaço/região de memória.

![Sem título2](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/04932d6f-0ce9-49b7-ab0e-0b3603df07b8)


### Operadores de associação

Usado para verificar se um objeto esta presente na sequência/variável.

![download](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/db89f498-9db1-41ae-a803-d01cced4c13f)


## Estruturas condicionais e de repetição

### Indentação e blocos

Identar código é uma forma de manter o código fonte mais legível e manutenível, mas em Python ela exerce a função de determinar onde um bloco de comando inicia com ( : ) mas onde termina é determinado pela indentação, diferente de outras  linguagens onde existe caracteres que fazem essa delimitação.

Em Java por exemplo, é usado as chaves para identificar o fim de cada bloco.
Mesmo sem a indentação o código em Java irá funcionar.

~~~
void sacar (double valor) { // inicio do bloco do método
    if (this.saldo >= valor) { // inicio do bloco do if
        this.saldo -= valor;
    } // fim do bloco do if
} // fim do bloco do método
~~~


Mas em Python, existe uma convensão de boas práticas onde é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.
Diferente de Java o Python precisa da indentação para funcionar. 

~~~
def sacar(self, valor: float) -> None:
    if self.saldo >= valor:
        self.saldo -= valor
    # fim bloco if
# fim do bloco do método
~~~

### Estruturas condicionais

Permite um desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas, que são: if, if-else e elif, if aninhado e if ternário.

- **if** : Usado para um único desvio onde ele irá testar a expressão lógica e em caso de retorno verdadeiro as ações no bloco de código if serão executadas.
- **if-else** :  Usada quando existe dois desvios, onde se a expressão lógica testada no if for verdadeira o bloco de código será executada, caso contrário o bloco de código do else será executada.
- **elif** : Usado quando existe mais de dois desvios, não existe um número máximo de utilização do elif, porém evite criar grandes estruturas condicionais para não aumentar a complexidade do código.
- **if aninhado** : Para criar essa estrutura basta usar if/elif/else dentro de um bloco de código de estruturas if/elif/else.
- **if ternário** : Permite escrever a condição em uma única linha. Ele é composto por três parte, sendo: retorno caso a expressão retorno verdadeiro; a expressão lógica; retorno caso a expressão não seja atendida. Para condições simples.

 

### Estrutura de repetição

São utilizadas para repetir um trecho do código um determinado número de vezes, que pode ser previamente conhecido ou determinado atrávez de uma expressão lógica.

Estrutura de repetição exemplo (não esta na sintase usada pelo Python).

![download (1)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/97099841-efff-42e8-a7e8-0881677f623c)


Para fazer essa repetição pode ser usado o comando **for** em momento onde sabemos o número exato de vezes que o bloco de código deve ser executado, ou quando queremos percorrer um objeto interável.

![download (2)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/fddf7215-6b22-48c4-bc00-fca2d60b6cab)


Também é possível utilizar a função **built-in range**, usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo), isso significa que em um range de 0 à 10 o 10 não será incluso. 

Se usarmos range (i, j) será produzido: i, i+1, i+2, i+3, …, j-1. Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step (opcional).

![download (3)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/6c408f9d-cbac-49d9-afd3-42b47c14821d)


Também é possível utilizar o comando **while** para repetir um bloco de código varias vezes. Ideal para quando não existe um número exato de vezes em que o código deve ser executado, onde o código será executado até acontecer determinada ação.

![download (4)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/75edee89-2236-4459-90e3-2c0d982966bf)


Dentro das estruturas de repetição existe a palavra reservada **break** que determina o fim da repetição de um laço infinito ao ser informado um valor especifico. 

Como variação, também podemos usar a palavra reservada **continue** que nos permite pular/desviar de uma situação específica do laço.

## Metodos uteis

### Classe string

Esta classe é famosa em Python por ser rica em métodos e possui uma interface fácil de trabalho.

- Método upper - Converte os caracteres da variável em maiúsculo.
- Método lower - Converte os caracteres da variável em minusculo.
- Método tittle - Converte os caracteres da variável em título deixando somente a primeira letra maiúscula.

    ~~~

        nome = "gabrielli"

        print(nome.upper())
        print(nome.lower())
        print(nome.title())

    ~~~
    
- Método strip - Corta os espaços em branco na esqueda e direita da variárel.
- Método lstrip - Corta os espaços em branco na esqueda da variárel.
- Método rstrip -  Corta os espaços em branco na direita da variárel.
    
   ~~~
    print(texto.strip() + ".")
    print(texto.lstrip() + ".")
    print(texto.rstrip() + ".")

   ~~~
    
- Método center - Centraliza a variável centro do número de caracteres determinados, podendo informar um caracter para ocupar os espaços em branco.
- Método join - Adiciona um caracter entre as letras, faz uma junção(join).
    
    ~~~

    print(menu.center(14))
    print(menu.center(14, "#"))
    print("####" + menu + "####")
    print("-" .join(menu))

    ~~~
    
    ### Interpolação de variáveis
    
    É o processo de juntar uma string com variáveis, no qual as variáveis serão adicionadas em espaços reservados dentro da string. 
    
    Existem 3 formas de interpolar váriaveis em strings:
    
    - **Usando %** - Utiliza o sinal de %, pouco utilizado por diminuir a capacidade de manutenção do código.
        
       ![Sem título](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/ae7b704a-8d4d-4a03-9908-36d8944e5740)

        
    - **Método format** - Se utiliza {} para concatenar variaveis a uma string. Muito parecido com o %, mas com uma capacidade um pouco maior de customização e elegibilidade.
        
        ![Sem título2](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/005b666c-1c1f-4869-8bd4-f91c9c135d8c)

        Ao invés de passar a posição da variável, também é possível nomear com o nome da variável. 
        ![Sem título3](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/3a0be07d-3bc8-451a-b4d8-05cb6e5170c8)

        
    - **Usando f strings** - A forma mais utilizadas onde em {} se informa somente o nome da variável sem a necessidade de comandos adicionais. O f também é utilizado para determinar o número de casas em números dentro da string.
        
    ![Sem título4](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/1ec4d2a1-6f72-46cb-9470-5a8ff7ca2436)


    ![Sem título5](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/ce49fa78-5dbb-43a1-af46-025e5fa02a73)

        
    
    ### Fatiamento de string
    
    É uma técnica utilizada para retornar sbstrings (partes da string original), informando inicio (start), fim (stop) e passo (step): **[start: stop: step]**.
    
    ![Sem título6](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/c6ca4fb4-ea43-4a60-94b7-41ff19b40a20)
    
    ### Strings de múltiplas linhas
    
    São definidas informando 3 simples/duplas ou duas durante a atribuição. Elas podem ocupar várias linhas do código e todos os espaços em branco são incluídos na string final. Uso interessante quando será criado um menu um texto maior ao usuário.
    
    ~~~
    name = "Gabrielli"

    mensagem = f"""
        Olá, meu nome é {name},
    Eu estou aprendendo Python.
        Essa mensagem tem diferentes recuos.
    """

    print(mensagem)

    ~~~

    ## Listas
    
    É um sequencial que armazena qualquer tipo de objeto. Podemos criar listas utilizando o construtor “list”, a função range ou colando valores separados por virgula dentro de colchetes. 

    ![download (5)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/7812d535-4811-4e5b-9390-08aefa76c293)
    
    Para acessar os valores da lista é o **acesso direto**, por ser uma sequencia a lista pode ser acessada utilizando os índices que é contado apartir de zero. 
    
    Sequências suportam indexação negativa, começando em **-1** , ideal para começar a contar o índece de trás para crente ou descrecente.
    
    Por ser um objeto, a lista pode armazenar outras listas, chamada assim de **lista aninhada**.  
    
    ![download (6)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/96b1d6d7-4d09-4bf0-ba0b-e3de0a7ff26d)
    
    O **fatiamento** usado nas strings também pode ser usado nas listas. 
    
   ![download (7)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/ca89bb10-ddf9-4136-91ba-633f77132eef)

    
    Para percorrer os valores da lista usamos o comando **for**, podendo ser usado o índice da lista usando o comando **enumerate**.
    
    ![download (8)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/864daa1d-d312-448c-aa76-b536d595bfa8)

    
     Para criar uma lista com base em valores de uma lista já existe (filtro) ou gerar uma nova lista aplicando modificações nos elementos de ums lista existente podemos usar a sintaxe mais curta de **compreensão de lista**.
    
     Filtro sem a compreensão
    
    ![download (9)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/532efe46-a831-4ef6-9065-ea09f13e9c88)

    
    Filtro com a compreensão(comprehension).
    
    ![download (10)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/ff059126-a709-4b13-8390-1f7947c64ac8)

    
    Modificando o valor sem a compreensão.
    
    ![download (11)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/673d4900-550c-463c-8d2d-2889580131b6)

    
    Modificando com a compreensão.
    
    ![download (12)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/c0854665-e25b-4794-8d82-672c7bb0e6b0)

    
    ### Métodos da lista
    
    A lista possui varias classes prontas para serem usadas.
    
    - **[].append** : Para adicionar um novo elemento na lista.
    - **[].clear** : Para limpar a lista.
    - **[].copy** : Pela lista ser um objeto mutavel/alteralvel, se usa o uso do copy para copiar a lista assim qualquer modficação na lista copiada não irá repletir na lista original.
    - **[].count** : Usado para contar quantas vezes um determinado objeto aparece na lista.
    - **[].extend** : Usado quando se ter adicionar novos elementos na lista juntando duas listas.
    - **[].index** : Usado para encontrar qual a primeira ocorrência de um objeto, em qual local no índex o objeto esta.
    - **[].pop** : Tira o ultimo elemnto da lista, podendo identificar o index do objeto que vai ser removido.
    - **[].remove** : Remove um objeto identidicando o objeto propriamente dito, removendo o primeiro que encontrar na lista.
    - **[].reverse** : Pegar uma lista e fazer o espelhamento.
    - **[].sort** : Ordenar uma lista, podendo ser usado outros comandos em conjunto como o reverser para ordenar de trás para frente, ou usando uma função anonima como lambda  (key=lambda) para ordenar por tamanho da string.
    - **len** : Identificar o tamanho da lista.
    - **sorted** : função usada também para ordenar interaveis, parecido com o [].sort.
        

    ## Tupla
    
    Tuplas diferentes das listas são imutaveis, ou seja, os valores não são alteraveis até o fim da execução do programa como como acontece com as listas sendo esta a unica diferença entre uma tupla e uma lista. Para criar uma tupla podemos usar a classe tuple, ou colocando valores separados por vírgula  de parenteses.
    
   ![download](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/750db8a7-1f56-41ea-9096-4750d8d7c479)

    
    Para acessar diretamente os valores da tupla ou usar indices negativos utilizamos os mesmos comandos que a lista. Pois os comandos em objetos em sequencias são os mesmos, sendo uma tupla ou lista. 
    
    Pela tupla ser um elemento imutavel, todos os métodos relacionados a alteração que existe na lista não irá existir nas tuplas, sendo assim tempos como métodos: **[].count ; [].index ; len** .
    
    ## Conjuntos
    
    **Set** é uma coleção que não possui objetos repetidos. usamos o set para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.
    
    Conjuntos em Python não suportam indexação e nem fatiamento, assim quando é preciso acessar os valores o set terá que ser convertido em uma lista. Sendo assim, a forma mais comum de percorrer os dados de um conjunto é utilizando o camando **for** (sintase é a mesma usada para a lista e tupla)
    
    ### **Métodos do set.**
    
    - **{}.union** : Usado para unir dois conjuntos.
    - **{}.intersection** :  Usado para ter a interceção entre os conjuntos A e B.
    - **{}.difference** : Usado para pegar o que é diferente entre os conjuntos A e B.
    - **{}.symmetric_difference** : Pega todos os elementos que não fazem parte da interceção.
    - **{}.issubset** : quando um conjunto A possui todos os elementos do conjunto B.
    - **{}.isdisjoint** : quando todos os elemtnos de um conjunto A não estão em B.
    - **{}.add** : Para adicionar um elemento no conjunto, onde elemntos repetidos são ignorados.
    - **{}.copy** : Mesma função do usado nas listas.
    - **{}.discard** : Para discartar um elemento do conjunto.
    - **{}.pop** : Mesma função usado nas listas, mas tirando os elementos da frente.
    - **{}.remove** : parecido com o discart com a diferença que ao tentar remover um elemento que não existe na lista ele irpa apresentar um erro.
    - **len** : Verifica o tamanho do conjunto.
    - **in** : Verificar se um elemento esta nos conjuntos.
    
    > PDF aula de conjuntos DIO, com exemplos.
    > 
    > 
    > [[Dio] Conjuntos.pdf](https://www.notion.so/Python-para-Cientistas-de-Dados-5482660b2b5d441c882829949e8cfbf8#1d7db7873d9640999c4d44a05d3c6f4b)
    > 
    
    ## Dicionários
    
    É um conjunto não-ordenado de pares chave:valor (sempre juntos), onde as chaves são unicas em um determinado valor, recomendado ser um valor imutavel como uma tupla ou string e o valor pode ser qualquer objeto. 
    
    Para declarar um dicionário, usamos as {} como delimitadores contendo uma lista de pares chave:valor separad por uma vírgula. 
    
    Segue formas de criar um dicionario. 
    
    A terceira forma também é a forma de acessar o dicionário. 
    
   ![download (1)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/21b8331a-e4de-4d12-adcb-8bcda8153224)
    
    Exemplo mostrando a criação de 4 dicionários, cada um com seus valores e abaixo o acesso a um desses docionário e o valor.
    
    ![download (2)](https://github.com/gabriellivieira/Bootcamp_data_science/assets/112736236/058333a0-17f3-480e-8f6e-b70af8e04d6b)

    
    ### Métodos
    
    - **{}.clear** : Para limpar os valores do dicionário.
    - **{}.copy** : Mesma funções das descrições nos outros comandos.
    - **{}.fromkeys** : Cria chaves para mim quando quero criar as chaves sem atribuir valor ou quando se quer criar chaves com valores padrões.
    - **{}.get** : Outra forma de adicionar valor nos dicionários. Interessante quando você quer buscar uma chave mas não tem certeza se a chave existe.
    - **{}.items** : Retorno uma lista de tuplas.
    - **{}.keys** : Retorna somente as chaves do dicionário.
    - **{}.pop** : Remove o valor de um docionário
    - **{}.popitem** : Parecido com o {}.pop com diferença que não inforamos a chave e ele exclui os itens em sequencias.
    - **{}.setdefaut** : Se o atributo não estiver no docionário ele adicionado com o atributo que informei, caso o atributo existe ele não altera.
    - **{}.update** : Permite atualizar um dicionário com outro dicionário.
    - **{}.values** : Retorna todos os valores do docionário.
    - **in** : Usado para saber se um valor é uma chave no docionário.
    - **del** : Outra forma de tirar um valor, onde se passa o objeto que se quer remover.
    
    > PDF aula de Métodos do dicionário DIO, com exemplos.
    > 
    > 
    > [[Dio] Dicionários.pdf](https://www.notion.so/Python-para-Cientistas-de-Dados-5482660b2b5d441c882829949e8cfbf8#806e9c84f96d49928171c22c83b8bd36)
    > 
    
    ## Funções do Python
    
     É um bloco de código identificado por um nome(identificador da função) e pode receber uma lista de parâmetros que podem ou não ter valores padrões (possui um conjunto de entradas e saídas). Usar funções torna o código mais legível e possibilita o reaproveitamento de código, programando dessa forma de uma maneira estruturada. 
    
    Para mostrar ao interpretador Python que estamos criando uma função usamos a palavra reservada “**def**” .
    
    Para retornar valores, usando a palavra reservada **return** . Em Python uma função pode retornar mais de um valor no qual o retorno padrão é “**None**” quando não existe valores a serem retornados. 
    
    Em Python, as funções também podem ser chamados usando **argumentos nomeadas** da forma chave=valor.
    
    **Args e Kwargs** : Podemos combinar os parâmetros obrigatórios com args e kwargs, definidos como *args e **kwards (podem ser usado qualquer palavra) onde o método recebe os valores como tupla e dicionário respectivamente. 
    
    ### Parametros especiais
    
    Por padrçao argumentos podem ser passados uma uma função Python tanto por posição como por nome, para melhorar legibilidade e desempenho o ideal é restringir a maneira como argumentos possam ser passados, se serão por posição, por posição e nome ou por apenas nome.
    
    ### Objetos de primeira classe
    
    Em Python tudo é objeto, dessa forma funções também são objetos, as tornando objetos de primeira classe. Com isso podemos **atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados** (listas, tuplas, dicionários,etc) e usar como valor de retorno para uma função (closures).