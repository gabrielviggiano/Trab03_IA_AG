import matplotlib.pyplot
#10 Iterações ---->>> Melhor : -16.88
iteracoes10 = [1,2,3,4,5,6,7,8,9,10]
valoresmedia10 = [-13.30, -14.06, -14.863, -14.96, -15.32, -15.45, -15.45, -15.95, -15.96, -16.03]
melhor10 = [-10.22, -13.17, -16.34, -16.34, -16.34, -16.34, -16.34, -16.88, -16.88, -16.88]

#20 Iterações ---->>> Melhor: -16.88
iteracoes20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
valoresmedia20 = [-11.59, -12.65, -13.23, -13.29, -13.79, -13.858, -14.27, -14.387, -14.42, -14.51, -14.51, -14.51, -14.8, -14.81, -14.88, -14.894, -14.894, -14.894, -14.95, -15.02]
melhor20 = [-13.17, -13.17, -13.17, -13.17, -16.88, -16.88, -16.88, -16.88, -16.88, -16.88, -16.88, -16.88, -16.88, -16.88, -16.88, -16.88, -16.88, -16.88, -16.88, -16.88]



tipo = int(input("GRAFICO DE 10 ou 20 ITERAÇÕES?? (Digite 10 ou 20): "))

if(tipo == 10):
	matplotlib.pyplot.plot(iteracoes10, valoresmedia10, label ="Média 10 execuções")
	matplotlib.pyplot.plot(iteracoes10, melhor10, label = "Iteração com o melhor resultado")
	matplotlib.pyplot.title("10 Iterações")
	matplotlib.pyplot.xlabel("Iterações")
	matplotlib.pyplot.ylabel("Média")
	matplotlib.pyplot.legend()
	matplotlib.pyplot.xlim(1, 10)
	matplotlib.pyplot.ylim(-17.00,-13.00)
	matplotlib.pyplot.show()
else:
	matplotlib.pyplot.plot(iteracoes20, valoresmedia20, label ="Média 10 execuções")
	matplotlib.pyplot.plot(iteracoes20, melhor20, label="Iteração com o melhor resultado")
	matplotlib.pyplot.title("20 Iterações")
	matplotlib.pyplot.xlabel("Iterações")
	matplotlib.pyplot.ylabel("Média")
	matplotlib.pyplot.legend()
	matplotlib.pyplot.xlim(1,20)
	matplotlib.pyplot.ylim(-17,-12)
	matplotlib.pyplot.show()