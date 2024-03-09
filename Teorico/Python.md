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

![download (3).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8428976b-6b4d-4188-be4a-0fceb792fdff/download_%284%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T003941Z&X-Amz-Expires=86400&X-Amz-Signature=1076f65ad4ef697b24b94345f06a6d5ad95786031732599c6b5f523b79b0e74c&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%284%29.jpg%22&x-id=GetObject)

### Operadores de associação

Usado para verificar se um objeto esta presente na sequência.

![download (4).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8428976b-6b4d-4188-be4a-0fceb792fdff/download_%284%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T004104Z&X-Amz-Expires=86400&X-Amz-Signature=902657c15bbeab1e0fac87f97f7fbc6a5ef7defada97c6a6dc27438a23665e32&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%284%29.jpg%22&x-id=GetObject)

## Estruturas condicionais e de repetição

### Indentação e blocos

Identar código é uma forma de manter o código fonte mais legível e manutenível, mas em Python ela exerce a função de determinar onde um bloco de comando inicia com ( : ) mas onde termina é determinado pela identação, diferente de outras  linguagens onde existe caracteres que fazem essa delimitação.

Em Java por exemplo, é usado as chaves para identificar o fim de cada bloco.

![download (5).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/909f74d8-3fb9-4f13-8221-daf1250737fc/download_%285%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T004404Z&X-Amz-Expires=86400&X-Amz-Signature=1e561d9bf69fb79e70be818035aeeaf46797ff8ef6d5d9479ee155fa4d7df517&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%285%29.jpg%22&x-id=GetObject)

Mas em Python, existe uma convensão de boas práticas onde é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

![download (6).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/64b799ce-d946-4fd9-961d-e374af2549a0/download_%286%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T004147Z&X-Amz-Expires=86400&X-Amz-Signature=2a39f477fdb3d822ea50e3d994a436d8f754db1d8e51d2827dbc264a9124bd2c&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%286%29.jpg%22&x-id=GetObject)

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

![download (7).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/94c6de29-4135-4995-a0a7-b4433bea7b30/download_%287%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T004434Z&X-Amz-Expires=86400&X-Amz-Signature=b28220f54c5a906652a71b73883c55617719607777304b2131e852a7193c1828&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%287%29.jpg%22&x-id=GetObject)

Para fazer essa repetição pode ser usado o comando **for** em momento onde sabemos o número exato de vezes que o bloco de código deve ser executado, ou quando queremos percorrer um objeto interável.

Também é possível utilizar a função **built-in range**, usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo), isso significa que em um range de 0 à 10 o 10 não será incluso. 

Se usarmos range (i, j) será produzido: i, i+1, i+2, i+3, …, j-1. Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step (opcional).

![download (8).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1512b437-9d3e-4909-866f-108cc4b3d9f3/download_%288%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T004630Z&X-Amz-Expires=86400&X-Amz-Signature=be8d1b82c1bff5ab56ea83b2a5237c8d7bbce1ad2571fd0ab3526f9d441e908f&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%288%29.jpg%22&x-id=GetObject)

Também é possível utilizar o comando **while** para repetir um bloco de código varias vezes. Ideal para quando não existe um número exato de vezes em que o código deve ser executado, onde o código será executado até acontecer determinada ação.

![download (9).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3d8bd9f0-e52d-40d6-a85b-8fdf1573116d/download_%289%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T004758Z&X-Amz-Expires=86400&X-Amz-Signature=690df31035eb86ac411fdebf6485ae0e6aeba84de94b10f98f570dbc11ebdad1&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%289%29.jpg%22&x-id=GetObject)

Dentro das estruturas de repetição existe a palavra reservada **break** que determina o fim da repetição de um laço infinito ao ser informado um valor especifico. 

Como variação, também podemos usar a palavra reservada **continue** que nos permite pular/desviar de uma situação específica do laço.

## Metodos uteis

### Classe string

Esta classe é famosa em Python por ser rica em métodos e possui uma interface fácil de trabalho.

- Método upper - Converte os caracteres da variável em maiúsculo.
- Método lower - Converte os caracteres da variável em minusculo.
- Método tittle - Converte os caracteres da variável em título deixando somente a primeira letra maiúscula.
    
    ![download (2).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9ca60b8e-51a7-4adc-8670-1715929d7cd9/download_%282%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T004958Z&X-Amz-Expires=86400&X-Amz-Signature=6aa672afacb25a3da2dd2f36c2d86416ad249f86919ff721eeeb2b4c9005338f&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%282%29.jpg%22&x-id=GetObject)
    
- Método strip - Corta os espaços em branco na esqueda e direita da variárel.
- Método lstrip - Corta os espaços em branco na esqueda da variárel.
- Método rstrip -  Corta os espaços em branco na direita da variárel.
    
    ![download (3).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0a2ff3d2-c4e9-4636-a5ee-9ddb64ff6159/download_%283%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005027Z&X-Amz-Expires=86400&X-Amz-Signature=0cea391171548d3b463c734bd9a640e098a9b905a103f268a3add58c81208aeb&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%283%29.jpg%22&x-id=GetObject)
    
- Método center - Centraliza a variável centro do número de caracteres determinados, podendo informar um caracter para ocupar os espaços em branco.
- Método join - Adiciona um caracter entre as letras, faz uma junção(join).
    
    ![download (1).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0f92cd07-5395-4990-a1e0-3e904f328598/download_%281%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005141Z&X-Amz-Expires=86400&X-Amz-Signature=055a4bfd64db51a9a4202fafd060a5d8d584313448c7561e032f37fdafd4b189&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%281%29.jpg%22&x-id=GetObject)
    
    ### Interpolação de variáveis
    
    É o processo de juntar uma string com variáveis, no qual as variáveis serão adicionadas em espaços reservados dentro da string. 
    
    Existem 3 formas de interpolar váriaveis em strings:
    
    - **Usando %** - Utiliza o sinal de %, pouco utilizado por diminuir a capacidade de manutenção do código.
        
        ![download (5).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b0c3e75d-346b-426a-acbd-7fdd583f69de/download_%285%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005351Z&X-Amz-Expires=86400&X-Amz-Signature=ba287cb01d1e033be4a7bf548d7df5b2fb68effa794eecff73db475a2f18dd93&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%285%29.jpg%22&x-id=GetObject)
        
    - **Método format** - Se utiliza {} para concatenar variaveis a uma string. Muito parecido com o %, mas com uma capacidade um pouco maior de customização e elegibilidade.
        
        ![download (4).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0a939ec3-c386-4a50-9df7-42d1e3efaf01/download_%284%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005404Z&X-Amz-Expires=86400&X-Amz-Signature=5d5b7127a14b8aa723e3c80c7135836368171717853571a85a725ba076ec3275&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%284%29.jpg%22&x-id=GetObject)
        
        ![download (6).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/60c16a2b-ebf3-42ca-a5ba-de55b9f265cc/download_%286%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005416Z&X-Amz-Expires=86400&X-Amz-Signature=0b84a4fa56c71f2c3b13b797d2f3484b94effb84ad6a348bf80ab351b301c6df&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%286%29.jpg%22&x-id=GetObject)
        
    - **Usando f strings** - A forma mais utilizadas onde em {} se informa somente o nome da variável sem a necessidade de comandos adicionais. O f também é utilizado para determinar o número de casas em números dentro da string.
        
        ![download (7).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ae2295b0-7e7e-4411-8416-48a738dd9eb6/download_%287%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005439Z&X-Amz-Expires=86400&X-Amz-Signature=e95dd766c1fad3cc75b1263fd8dfeefc2a62986f15a7a1270bc7ce52cfe67397&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%287%29.jpg%22&x-id=GetObject)
        
        ![download (8).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a25f782a-416f-43b7-b81a-056559df21b3/download_%288%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005448Z&X-Amz-Expires=86400&X-Amz-Signature=7c159a21b75564ae6260b050d438ab5aa8a1be7a8d8f7285f634945c6d60c217&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%288%29.jpg%22&x-id=GetObject)
        
    
    ### Fatiamento de string
    
    É uma técnica utilizada para retornar sbstrings (partes da string original), informando inicio (start), fim (stop) e passo (step): **[start: stop: step]**.
    
    ![download (9).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a378490e-1788-4306-a688-a9f3db55ef96/download_%289%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005515Z&X-Amz-Expires=86400&X-Amz-Signature=083f3502eb1743f69b95e4400cc2a1687819f4247a5780c299b84725361524b6&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%289%29.jpg%22&x-id=GetObject)
    
    ### Strings de múltiplas linhas
    
    São definidas informando 3 simples/duplas ou duas durante a atribuição. Elas podem ocupar várias linhas do código e todos os espaços em branco são incluídos na string final. Uso interessante quando será criado um menu um texto maior ao usuário.
    
    ## Listas
    
    É um sequencial que armazena qualquer tipo de objeto. Podemos criar listas utilizando o construtor “list”, a função range ou colando valores separados por virgula dentro de colchetes. 
    
    Para acessar os valores da lista é o **acesso direto**, por ser uma sequencia a lista pode ser acessada utilizando os índices que é contado apartir de zero. 
    
    Sequências suportam indexação negativa, começando em **-1** , ideal para começar a contar o índece de trás para crente ou descrecente.
    
    Por ser um objeto, a lista pode armazenar outras listas, chamada assim de lista aninhada.  O **fatiamento** usado nas strings também pode ser usado nas listas. 
    
    ![download.jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d116eac7-818f-4066-bc7e-714e53f9dd4a/download.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005541Z&X-Amz-Expires=86400&X-Amz-Signature=5bede237b1733b91c384c8aef2175c8a72ceda1e980dcb8f3cf6a62f58ed6c1c&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download.jpg%22&x-id=GetObject)
    
    Para percorrer os valores da lista usamos o comando **for**, podendo ser usado o índice da lista usando o comando **enumerate**.
    
    ![download (1).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/51c25a35-d0e4-4f36-b812-7f0facd8f462/download_%281%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005552Z&X-Amz-Expires=86400&X-Amz-Signature=89be52b36275f2a244b874e75cd548174ff323d50b1ba6081af98cb602641400&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%281%29.jpg%22&x-id=GetObject)
    
     Para criar uma lista com base em valores de uma lista já existe (filtro) ou gerar uma nova lista aplicando modificações nos elementos de ums lista existente podemos usar a sintaxe mais curta de **compreensão de lista**.
    
     Filtro sem a compreensão
    
    ![download (2).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/89de289a-f951-4c34-93bc-2b01a02c590b/download_%282%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005606Z&X-Amz-Expires=86400&X-Amz-Signature=0d41a412d9caf8e1942d82668f3c1009e4758ec003fa9ff2b9851aca768af5fc&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%282%29.jpg%22&x-id=GetObject)
    
    Filtro com a compreensão.
    
    ![download (3).jpg](https://www.notion.so/signed/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F43cb910b-6a53-47d2-9ced-dbd55f84e723%2Fdownload_(3).jpg?id=4c78275a-4900-4588-81ae-59fd745e5b46&table=block&spaceId=47370e3a-ad05-454d-986b-f9ff4d8322d6&name=download%20(3).jpg&userId=bc5e79c9-9cf4-46bf-9ac5-701553559884&cache=v2)
    
    Modificando o valor sem a compreensão.
    
    ![download (4).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2277d799-b8b7-4dfe-b595-0ab63c860054/download_%284%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005630Z&X-Amz-Expires=86400&X-Amz-Signature=75cc9e2924cdddf85e7e25eb978353d2319070954566d083426c5402cc2fe939&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%284%29.jpg%22&x-id=GetObject)
    
    Modificando com a compreensão.
    
    ![download (5).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fa5dfbfd-5a87-4f5c-97d0-495f7c02f155/download_%285%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005645Z&X-Amz-Expires=86400&X-Amz-Signature=8edaf96920d50585039670d596a830c4b8ab3820fa5e04898e0f6c0558f450a7&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%285%29.jpg%22&x-id=GetObject)
    
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
        
        ![download (6).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/23953a80-8448-4657-9770-31c74cc0ea08/download_%286%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005707Z&X-Amz-Expires=86400&X-Amz-Signature=d33cff1a823dbfe33540a973def416be9cf02080dc77ea7b48d56beb8e0519ac&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%286%29.jpg%22&x-id=GetObject)
        
    - **len** : Identificar o tamanho da lista.
    - **sorted** : função usada também para ordenar interaveis, parecido com o [].sort.
        
        ![download (7).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d6b81946-c4d5-40a6-b439-9a663324cc56/download_%287%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005735Z&X-Amz-Expires=86400&X-Amz-Signature=235c8c1e107a85c0c8668a28eb2eb8035baea766a1ab555deae412bfd6a0da03&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%287%29.jpg%22&x-id=GetObject)
        
    - 
    
    ## Tupla
    
    Tuplas diferentes das listas são imutaveis, ou seja, os valores não são alteraveis até o fim da execução do programa como como acontece com as listas sendo esta a unica diferença entre uma tupla e uma lista. Para criar uma tupla podemos usar a classe tuple, ou colocando valores separados por vírgula  de parenteses.
    
    ![download (8).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/757be9e4-9aaf-4d62-bde4-c35cae957e9c/download_%288%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005746Z&X-Amz-Expires=86400&X-Amz-Signature=9fa2f92c48b413d9165299313b9338666654ad99ef56dd081b0e9e512f9f61d1&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%288%29.jpg%22&x-id=GetObject)
    
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
    
    A tericeira forma também é a forma de acessar o dicionário. 
    
    ![download (9).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d51d5aa5-2a50-4f85-bf0c-fb8a5f4f45e7/download_%289%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005905Z&X-Amz-Expires=86400&X-Amz-Signature=0df7e6385491ac439fda4ac149f1a6e73f18f1dd13f451be1bfbab33e2327075&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%289%29.jpg%22&x-id=GetObject)
    
    Exemplo mostrando a criação de 4 dicionários, cada um com seus valores e abaixo o acesso a um desses docionário e o valor.
    
    ![download (10).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/65bdc7c4-44a1-434d-a934-bcff30a7a065/download_%2810%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T005917Z&X-Amz-Expires=86400&X-Amz-Signature=34bd13cf799aa4a2937e4fec1618eaa37161199380b5b763190977b9ff3b938b&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%2810%29.jpg%22&x-id=GetObject)
    
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