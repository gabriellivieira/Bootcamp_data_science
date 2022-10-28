# Python para Cientistas de Dados

## Tipos de dados

Os tipos definem as caracteristicas e comportamentos de um valor (objeto) para o interpretador. Os tipos subdividem o que pode ser feito com aquele dado especifico e espaço que ira ocupar na memória.

- Números Inteiros : Números pela clase **int**. Ex: 1, 10, 50, -1, -100.
- Números de ponto flutuante: Números racionais representados pela classe **float**. Ex: 1,5,-10,54 … 999278.002
- Booleano: representa verdadeio e falso na classe **bool**. Em Python booleano é uma sub classe de int, onde qualquer número diferente de 0 representa verdadeiro e o 0 é faso.
- Strings: Usados para representar valores alfanúmericos, na classe **str**.

![download (1).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/48c938c3-4ec1-40fa-bd04-ce13a3cb1889/download_%281%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221028T005659Z&X-Amz-Expires=86400&X-Amz-Signature=a0057f86df22f7f55ed63c1eff7a606e5f44b361f3845a98a483f84c7833a2fa&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%281%29.jpg%22&x-id=GetObject)

## Variáveis e constantes

Variaveis são usadas quando o valor de um objeto pode sofrer alterações durante a execução o programa, enquanto que as constantes são valores fixos e não altera durante a execução do programa.

Diferentes de outras linguagens que possuem uma palavra reservada para determinar se uma variavel é ou não constante, no Python não existe e para determinar se uma variavel é constante basta escrever ela em MAIÚSCULO, de acordo com convernsão.

### Boas Práticas

- O padrão de nome deve ser em snake case: em nomes onde existe espaço deve ser usado um _ . EX: Total de compras > Total_de_compras
- Escolher nomes sugestivos;
- Nome de constantes todo em maiúsculo.

## Funções de entrada e saída

### Função imput

Função builtin (padrão/nativa) input é usada quando queremos ler dados de entrada padrão (teclado). ela recebe um argumento do tipo string, que é exibido na saída padrão(tela) ao usuário.

### Função print

Função builtin print é usada quando queremos apresentar dados na saída padrão. Ela recebe argumentos obrigatórios do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados em set e terminados por end.

## Operadores

[Operadores Aritméticos e Operadores Lógicos em Python](https://pythonacademy.com.br/blog/operadores-aritmeticos-e-logicos-em-python)

### Operadores artméticos

Eles executam operações matemáticas, como adição (+), subtração ( - ), multiplicação ( * ), divisão ( / ) e divisão inteira ( // ).

**Módulo** é um operador que mostra o resto da operação. 

E a **exponenciação** se usa ** .

Para as operações o Python segue a ordem da matemática para os calculos. 

![download (2).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e1a7de23-9eaf-4e4e-8fba-410e3272380d/download_%282%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221028T005721Z&X-Amz-Expires=86400&X-Amz-Signature=7c613d83ff8e10691b197bcaf8e89b8377ea27c4f6bff0f746ab72ba01ed3a95&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%282%29.jpg%22&x-id=GetObject)

### Operadores de comparação

Utilizados para comparar dois valores, se ele é igual ( == ), maior ( > ), maior ou igual ( > =), menor ( < ), menor ou igual ( < = ) ou diferente ( != ).

### Operadores de atribuição

São utilizados para definir um valor inicial ou redefinir o valor de uma variavel ( = ). Também é possível adicionar e somar um valor usando ( += ) e assim por diante com as demais operações aritméticas.

### Operadores lógicos

São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica.  Assim, quando um operadore de comparação é usado o resultadora será um booleano.

| and | Retorna True se ambas as afirmações forem verdadeiras |
| --- | --- |
| or | Retorna True se uma das afirmações for verdadeira |
| not | Retorna Falso se o resultado for verdadeiro |

### Operadores de identidade

São utilizados para comparar se os mesmos objeto testados ocupam o mesmo espaço/região de memória.

![download (3).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f1917183-726d-400a-b8b5-74de85c04e72/download_%283%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221028T005755Z&X-Amz-Expires=86400&X-Amz-Signature=52edcbf9bc14baa8ed6542fa15b26b795bd7e367062395a6265be22619f18598&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%283%29.jpg%22&x-id=GetObject)

### Operadores de associação

Usado para verificar se um objeto esta presente na sequência.

![download (4).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8428976b-6b4d-4188-be4a-0fceb792fdff/download_%284%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221028T005814Z&X-Amz-Expires=86400&X-Amz-Signature=adc0640c5babea5425f19a036be142cfe5ce42258cca7db30a2162fb1f29d8c0&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%284%29.jpg%22&x-id=GetObject)

## Estruturas condicionais e de repetição

### Indentação e blocos

Identar código é uma forma de manter o código fonte mais legível e manutenível, mas em Python ela exerce a função de determinar onde um bloco de comando inicia com ( : ) mas onde termina é determinado pela identação, diferente de outras  linguagens onde existe caracteres que fazem essa delimitação.

Em Java por exemplo, é usado as chaves para identificar o fim de cada bloco.

![download (5).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/909f74d8-3fb9-4f13-8221-daf1250737fc/download_%285%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221028T005828Z&X-Amz-Expires=86400&X-Amz-Signature=0965ffe3b37083ab671e9b6c0e7fc2f60c15e74a53668df51d61eda91485ea46&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%285%29.jpg%22&x-id=GetObject)

Mas em Python, existe uma convensão de boas praticas onde é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

![download (6).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/64b799ce-d946-4fd9-961d-e374af2549a0/download_%286%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221028T005857Z&X-Amz-Expires=86400&X-Amz-Signature=d83eee167f03243c056de05ad6eed8e97a00f2bf2d953b3ca3e46260346576ae&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%286%29.jpg%22&x-id=GetObject)

### Estruturas condicionais

Permite um desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas, que são: if, if-else e elif, if aninhado e if ternário.

- **if** : Usado para um unico desvio onde ele irá testar a expressão lógica e em caso de retorno verdadeiro as ações no bloco de código if serão executadas.
- **if-else** :  Usada quando existe dois desvios, onde se a expressãp lógica testada no if for verdadeira o bloco de código será executada, casp contrário o bloco de código do else será executada.
- **elif** : Usado quando existe mais de dois desvio, não existe um número máximo de utilização do elif, porém evite criar grandes estruturas condicionais para nçai aumentar a complexidade do código.
- **if aninhado** : Para criar essa estrutura basta usar if/elif/else dentro de um bloco de código de estruturas if/elif/else.
- **if ternário** : Permite escrever a condição em uma unica linha. Ele é comporto por três parte, sendo: retorno caso a expressão retorno verdadeiro; a expressão lógica; retorno caso a expressão não seja atendida. Para condições simples.

 

### Estrutura de repetição

São utilizadas para repetir um trecho do código um determinado número de vezes, que pode ser previamente conhecido ou determinado atrávez de uma expressão lógica.

Estrutura de repetição exemplo (não esta na sintase usada pelo Python).

![download (7).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/94c6de29-4135-4995-a0a7-b4433bea7b30/download_%287%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221028T005915Z&X-Amz-Expires=86400&X-Amz-Signature=ea46e169c7a3eb1608d2b9388de6b3654a5c0e7e3c3e2baba57417cb5dfe0f8a&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%287%29.jpg%22&x-id=GetObject)

Para fazer essa repetição pode ser usado o comando **for** em momento onde sabemos o número exato de vezes que o bloco de código deve ser executado, ou quando queremos percorrer um objeto interável.

Também é possível utilizar a função **built-in range**, usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo), isso significa que em um range de 0 à 10 o 10 não será incluso. 

Se usarmos range (i, j) será produzido: i, i+1, i+2, i+3, …, j-1. Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step (opcional).

![download (8).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1512b437-9d3e-4909-866f-108cc4b3d9f3/download_%288%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221028T005927Z&X-Amz-Expires=86400&X-Amz-Signature=ad1345213efb60e730316c8fe382ec11068bad7f2c857ad61c3d27fed8fd2825&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%288%29.jpg%22&x-id=GetObject)

Também é possível utilizar o comenado **while** para repetir um bloco de código varias vezes. Ideal para quando não existe um número exato de vezes em que o código deve ser executado, onde o código será executado até acontecer determinada ação.

![download (9).jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3d8bd9f0-e52d-40d6-a85b-8fdf1573116d/download_%289%29.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221028T005938Z&X-Amz-Expires=86400&X-Amz-Signature=b9dddfc63d40ab4811ea89096d35f69e6cd14fb0d2a93ae1a72a6d4b4c1268af&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22download%2520%289%29.jpg%22&x-id=GetObject)

Dentro das estruturas de repetição existe a palavra reservada **break** que determina o fim da repetição de um laço infinito ao ser informado um valor especifico. 

Como variação, também podemos usar a palavra reservada **continue** que nos permite pular/desviar de uma situação especifica do laço.