# Algoritmo Genético
Trabalho 3 referente a disciplina de Inteligência Artificial.

### Alunos: 
Gabriel Pontes Marchezi e Gabriel Viggiano Fonseca

# Explicação Teórica
Algoritmos Genéticos (AG) são implementados como uma simulação de computador em que uma população de representações abstratas de solução é selecionada em busca de soluções melhores. A evolução geralmente se inicia a partir de um conjunto de soluções criado aleatoriamente e é realizada por meio de gerações. A cada geração, a adaptação de cada solução na população é avaliada, alguns indivíduos são selecionados para a próxima geração, e recombinados ou mutados para formar uma nova população. A nova população então é utilizada como entrada para a próxima iteração do algoritmo. 

Algoritmos genéticos diferem dos algoritmos tradicionais de otimização em basicamente quatro aspectos: 
1. Baseiam-se em uma codificação do conjunto das soluções possíveis, e não nos parâmetros da otimização em si;
2. os resultados são apresentados como uma população de soluções e não como uma solução única;
3. não necessitam de nenhum conhecimento derivado do problema, apenas de uma forma de avaliação do resultado;
4. usam transições probabilísticas e não regras determinísticas.

# Problema Proposto
O problema proposto é realizar a implementação do algoritmo genético a fim de minimizar a função abaixo.

![Alt text](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/funcao2.png?raw=true "funcao algoritmo genetico")<br>

Vale ressaltar que para o modo de seleção, iremos utilizar o "Torneio".
A taxa de Crossover será de 60%, a taxa de mutação de 1% e executaremos o algoritmo com 10 e 20 iterações.
# Implementação
Para a implementação do Algoritmo Genético, foi utilizada a linguagem de programação Python, essa que vem ganhando bastante popularidade na área de de Inteligência Artificial, por ser uma linguagem de fácil aprendizado e com alto nível de produtividade. E também pelo fato de podermos gerar gráficos através da biblioteca Matplotlib, visto que para esse trabalho, os resultados são de extrema importância.
Dito isso, vamos ao código:



## Trechos mais Importantes


### Função InicializarPopulação
#### Recebe como parâmetro o número de indivíduos que irá compor a população. Em loop vai criando os indivíduos, composto por um gene binário de 10 bits, e adicionando-os em um lista que representa a população. 
![Img inic](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_inicializar.JPG?raw=true)
### Funções de conversão para Decimal-Binário e Binário-Decimal
#### Funções auxiliares responsáveis pela conversão entre as bases binária e decimal
![Img BinárioDec](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_BtDDtB.JPG?raw=true)
### Função Melhor_Pior
#### Recebe como parâmetro um lista de população e retorna o indivíduo com melhor e pior aptidão
![Img melhor](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_melhor_pior.JPG?raw=true)
### Função Torneio
#### Recebe como parâmetro uma lista de população e retorna uma lista de pais selecionados do mesmo tamanho da população recebida como parâmetro. Os possíveis pais são selecionados aleatoriamente de 2 em 2 e o que possuir a melhor aptidão é escolhido como pai
![Img torneio](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_torneio.JPG?raw=true)
### Função Crossover
#### Responsável por gerar uma nova população. Recebe como parametro a lista de pais escolhidos no torneio e se o corte dos genes dos pais será uniforme (ao meio) ou aleatório, de 2 em 2 os pais são selecionados, é aplicada uma taxa de crossover e caso a taxa seja satisfeita os filhos são gerados através da mistura dos genes dos pais, caso contrário os filhos serão cópias dos seus pais.
![Img crossover](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_crossover.JPG?raw=true)
### Função Mutacao
#### Recebe como parâmetro uma taxa de mutação, percorre os genes dos indivíduos e caso a taxa satisfaça a condição, inverte o bit do indivíduo
![Img mutacao](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_mutacao.JPG?raw=true)
### Função Algo_Gen
#### Recebe como parâmetro a população inicial,o número de iterações, a taxa de mutação, taxa de crossover e se o corte dos genes no crossover será uniforme. A função faz apenas uma execucação do algoritmo genético, em um loop definido pelo número de iterações aplica as funções previamente definidas. Retorna uma lista contendo os indivíduos de cada iteração.
![Img Algoritmo](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_algogen.JPG?raw=true)
### Função principal parte 1
#### Recebe os dados do usuário, o algoritmo genético será executado N vezes em um loop e será gerada uma lista de execuções 
![Img main1](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_main1.JPG?raw=true)
### Função principal parte 2
#### Percorre a lista de execuções e para cada iteração de cada execução é encontrado e armazenado em uma lista o melhor resultado. Inicia a lista de dos valores das médias das iterações preenchendo com zero
![Img main2](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_main2.JPG?raw=true)
### Função principal parte 3
#### Percorre a lista de melhores valores de cada iteração em cada execução e vai somando o valor na lista de valores médios afim de encontrar as média das iterações. Encontra e armazena os valores da execução com a melhor aptidão.
![Img main3](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_main3.JPG?raw=true)


# Resultados
### Gráfico de 10 execuções do algoritmo genético com 10 iterações e populações de 10 indivíduos
![img grafico10](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/Grafico_10.png?raw=true)
### Gráfico de 10 execuções do algoritmo genético com 20 iterações e populações de 10 indivíduos
![Img grafico20](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/Grafico_20.png?raw=true)

# Bibliografia

https://pt.wikipedia.org/wiki/Algoritmo_genético
Slides do AVA.

