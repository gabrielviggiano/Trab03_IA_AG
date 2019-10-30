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



### Trechos mais Importantes

![Img inic](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_inicializar.JPG?raw=true)
![Alt text](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_BtDDtB.JPG?raw=true)
![Img melhor](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_melhor_pior.JPG?raw=true)
![Img torneio](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_torneio.JPG?raw=true)
![Img crossover](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_crossover.JPG?raw=true)
![Img mutacao](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_mutacao.JPG?raw=true)
![Img Algoritmo](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_algogen.JPG?raw=true)
![Img main1](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_main1.JPG?raw=true)
![Img main2](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_main2.JPG?raw=true)
![Img main3](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/img_main3.JPG?raw=true)


# Resultados e Análise

![img grafico10](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/Grafico_10.png?raw=true)
![Img grafico20](https://github.com/gabrielviggiano/Trab03_IA_AG/blob/master/Imagens/Grafico_20.png?raw=true)

# Bibliografia
https://pt.wikipedia.org/wiki/Algoritmo_genético

