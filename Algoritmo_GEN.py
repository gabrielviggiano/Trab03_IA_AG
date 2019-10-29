import random
import math

###### Autores: Gabriel Marchezi e Gabriel Viggiano ######

#Inicializa a população com valores aleatórios
def InicializarPopulação (numPop):
	listaPop = []
	individuo = 0
	while (numPop > 0):
		individuo = random.randint(0,1024)
		listaPop.append(DecToBin(individuo))
		numPop = numPop - 1
	return listaPop


def Torneio(populacao):
	lista_torneio = []
	for i in range(len(populacao)):
		pai1 = populacao[random.randint(0,len(populacao)-1)]
		pai2 = populacao[random.randint(0,len(populacao)-1)]
		while (pai1 == pai2):
			pai2 = populacao[random.randint(0, len(populacao)-1)]
		if Avalia_Individuo(pai1) < Avalia_Individuo(pai2):
			lista_torneio.append(pai1)
		else:
			lista_torneio.append(pai2)
	return lista_torneio


def Crossover(lst_pais, taxa):
	lst_filhos = []
	for i in range(0,len(lst_pais),2):
		if(random.randint(1,100) <= taxa):
			ponto = random.randint(0,len(lst_pais[i])-1)
			filho1 = lst_pais[i][:ponto] + lst_pais[i+1][ponto:]
			filho2 = lst_pais[i][ponto:] + lst_pais[i+1][:ponto]
		else:
			filho1 = lst_pais[i]
			filho2 = lst_pais[i+1]
		lst_filhos.append(filho1)
		lst_filhos.append(filho2)
	return lst_filhos

def Mutacao (lst_filhos, taxa):
	lst_mutada = []
	for filho in lst_filhos:
		for bit in filho:
			if(random.randint(1,80) <= taxa):
				if(bit == '1'):
					bit = '0'
				else:
					bit = '1'
		lst_mutada.append(filho)
	return lst_mutada

#Recebe uma lista de individuos e retorna uma lista com os individuos com melhor e pior aptidão
def Melhor_Pior (lst_ind):
	lista = []
	melhor = lst_ind[0]
	pior = lst_ind[0]
	for individuo in lst_ind:
		if (Avalia_Individuo(individuo) < Avalia_Individuo(melhor)):
			melhor = individuo
		if(Avalia_Individuo(individuo) > Avalia_Individuo(pior)):
			pior = individuo
	lista.append(melhor)
	lista.append(pior)
	return lista


def Algo_Gen(iteracoes ,populacao):
	lista = []
	contador = 0
	otimo = 0
	while(cont<iteracoes and otimo == 0):
		
		cont += cont
	return 0

# Converte um número decimal para um número binário de 10 bits
def DecToBin(dec):
	b1n = bin(dec)[2:]
	while (len(b1n) < 10):
		b1n = '0' + b1n
	return b1n

# Convente um número binário para um número decimal
def BinToDec(b1n):
	i = 0
	while (b1n[i] =='0'):
		i += 1
	b1n = '0b' + b1n[i:]
	dec = int(b1n,2)
	return dec


# Avalia a aptidão do invidíduo
def Avalia_Individuo(individuo):
	x = (40/1024)*BinToDec(individuo)-20
	resultado = round(math.cos(x)*x+2,2)
	return resultado


def main():
	populacao = []
	populacao = InicializarPopulação(10)
	print(populacao)
	#Algo_Gen(populacao)
	lista = []
	lista = Torneio(populacao)
	print(lista)
	print("--------------------------------------------------------------------------")
	lista2 = Melhor_Pior(populacao)
	print(lista2)	
	print("--------------------------------------------------------------------------")
	lista3 = Melhor_Pior(lista)
	print(lista3)
	print("--------------------------------------------------------------------------")
	lista4 = Crossover(lista,75)
	print(lista4)
	print("--------------------------------------------------------------------------")
	lista5 = Mutacao(lista4,80)
	print(lista5)


if __name__ == '__main__':
	main()