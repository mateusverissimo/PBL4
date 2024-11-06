import random
from time import time

qualificacoes = []
for acao in range(1, 100001):
    opcao = {
        'preco_exercicio': random.randint(50, 500),
        'prazo_vencimento': random.randint(7, 365),
        'volume': random.randint(10000, 100000),
        'spread': random.randint(1, 5) / 100
    }
    formula = (opcao['volume'] / opcao['prazo_vencimento']) * (1 - opcao['spread']) * opcao['preço_exercicio']
    qualificacoes.append((formula, opcao))
    #print(f'Qualificações geradas aleatoriamente: {formula:.2f}')

inicio_temp = time()

def divisao_qualificacoes(qualificacoes):
    if len(qualificacoes) > 1:
        meio = len(qualificacoes) // 2
        esquerda = qualificacoes[:meio]
        direita = qualificacoes[meio:]

        divisao_qualificacoes(esquerda)
        divisao_qualificacoes(direita)

        e = d = q = 0 

        while e < len(esquerda) and d < len(direita):
            if esquerda[e][0] > direita[d][0]:  
                qualificacoes[q] = esquerda[e]
                e += 1
            else:
                qualificacoes[q] = direita[d]
                d += 1
            q += 1

        while e < len(esquerda):
            qualificacoes[q] = esquerda[e]
            e += 1
            q += 1

        while d < len(direita):
            qualificacoes[q] = direita[d]
            d += 1
            q += 1

divisao_qualificacoes(qualificacoes)

fim_temp = time()

print("- Transações ordenadas por atratividade: ")
for lista_final, (formula, opcao) in enumerate(qualificacoes, start=1):
    print(f"{lista_final}. Qualificação: {formula:.2f}")
print(f'- Tempo total: {fim_temp - inicio_temp:.5f} segundos')