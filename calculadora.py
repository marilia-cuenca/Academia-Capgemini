# -*- coding: utf-8 -*-
"""calculadora

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H94HO0J1t8zHLiT0Z1xaEcOF__nK_3lM
"""

'''
a cada 100 pessoas que visualizam o anúncio 12 clicam nele.
30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.
a cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.
cada compartilhamento nas redes sociais gera 40 novas visualizações.
o mesmo anúncio é compartilhado no máximo 4 vezes em sequência
'''
#30/3.6 == 12% clicam no anúncio -> 15% de 12% compartilha -> * 40 novas visualizações -> 12% das 40 novas visualiazações, clicam no anúncio -> ciclo
#visualizacao = (100*20)/12 == 166 (enquanto 166 pessoas vizualizam, 20 delas clicam no anúncio.)
#cliques = (12/100)*30 == 3.6 (12% das pessoas clicam no anúncio após visualizarem, e 30 pessoas visualizam o anúncio original)
#compartilhamento = (15/100)*3.6 == 0.54 (15% das pessoas compartilham nas redes sociais após clicarem no anúncio)

from math import ceil
investimento = float(input('Qual é o valor investido para o anúncio? R$ '))
original = investimento * 30 + (((30 / 3.6) * 0.54) * 40)
primeiro = (original - (investimento * 30)) * (40 * 0.12) * 0.15
segundo = primeiro * (40 * 0.12) * 0.15
terceiro = segundo * (40 * 0.12) * 0.15
projecao = ceil(original + primeiro + segundo + terceiro)
print('A projeção da quantidade máxima de pessoas que visualizarão o mesmo anúncio é de: {:.0f}'.format(projecao))