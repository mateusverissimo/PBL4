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
    formula = (opcao['volume'] / opcao['prazo_vencimento']) * \
        (1 - opcao['spread']) * opcao['preco_exercicio']
    opcao['qualificacao'] = formula
    qualificacoes.append(opcao)
    #print(f"Qualificações geradas aleatoriamente: {formula:.2f}")

inicio_temp = time()

def divisao_qualificacoes(lista, inicio, fim):
    if inicio < fim:
        pivo = partition(lista, inicio, fim)
        divisao_qualificacoes(lista, inicio, pivo - 1)
        divisao_qualificacoes(lista, pivo + 1, fim)


def partition(lista, inicio, fim):
    pivo = lista[fim]['qualificacao']
    indice_apos_pivo = inicio - 1
    for troca_pos_ant in range(inicio, fim):
        if lista[troca_pos_ant]['qualificacao'] > pivo:
            indice_apos_pivo += 1
            lista[indice_apos_pivo], lista[troca_pos_ant] = lista[troca_pos_ant], lista[indice_apos_pivo]
    lista[indice_apos_pivo + 1], lista[fim] = lista[fim], lista[indice_apos_pivo + 1]
    return indice_apos_pivo + 1

divisao_qualificacoes(qualificacoes, 0, len(qualificacoes) - 1)

fim_temp = time()

print("- Transações ordenadas por atratividade:")
for lista_final, opçao in enumerate(qualificacoes, start=1):
    print(f"{lista_final}. Qualificação: {opçao['qualificacao']:.2f}")
print(f'Tempo total: {fim_temp - inicio_temp:.4f} segundos')