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
    formula = (opcao['volume'] / opcao['prazo_vencimento']) * (1 - opcao['spread']) * opcao['preco_exercicio']
    qualificacoes.append((formula, opcao))
    #print(f'Qualificações geradas aleatoriamente: {formula:.2f}')

inicio_temp = time()

inicio_insertion = 10

def insertion_sort(qualificacoes, inicio, fim):
    for posicao_atual in range(inicio + 1, fim + 1):
        numero_atual = qualificacoes[posicao_atual]
        posicao_anterior = posicao_atual - 1
        while posicao_anterior >= inicio and qualificacoes[posicao_anterior][0] < numero_atual[0]:
            qualificacoes[posicao_anterior + 1] = qualificacoes[posicao_anterior]
            posicao_anterior -= 1
        qualificacoes[posicao_anterior + 1] = numero_atual

def divisao_qualificacoes(qualificacoes, inicio, fim):
    if fim - inicio + 1 <= inicio_insertion:
        insertion_sort(qualificacoes, inicio, fim)
    elif inicio < fim:
        meio = (inicio + fim) // 2
        divisao_qualificacoes(qualificacoes, inicio, meio)
        divisao_qualificacoes(qualificacoes, meio + 1, fim)
        merge(qualificacoes, inicio, meio, fim)

def merge(qualificacoes, inicio, meio, fim):
    esquerda = qualificacoes[inicio:meio + 1]
    direita = qualificacoes[meio + 1:fim + 1]

    e = d = q = 0

    while e < len(esquerda) and d < len(direita):
        if esquerda[e][0] >= direita[d][0]:
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

divisao_qualificacoes(qualificacoes, 0, len(qualificacoes) - 1)

fim_temp = time()

print("- Transações ordenadas por atratividade:")
for lista_final, (formula, opcao) in enumerate(qualificacoes, start=1):
    print(f"{lista_final}. Qualificação: {formula:.2f}")
print(f'- Tempo total: {fim_temp - inicio_temp:.5f} segundos')