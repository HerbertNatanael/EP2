import random

# função para rolar os dados (exercicio 1)
def rolar_dados(qtd):
    dados = []
    for _ in range(qtd):
        dados.append(random.randint(1, 6))
    return dados

# teste
#from funcoes import rolar_dados (adicionar no arquivo final)
# print(rolar_dados(5)) teste da função rolar_dados

# função para guardar um dado (exercicio 2)
def guardar_dado(dados_rolados, dados_no_estoque, indice):
    dado = dados_rolados.pop(indice)
    dados_no_estoque.append(dado)
    return [dados_rolados, dados_no_estoque]

# remover um dado do estoque (exercicio 3)
def remover_dado(dados_rolados, dados_no_estoque, indice):
    dado = dados_no_estoque.pop(indice)
    dados_rolados.append(dado)
    return [dados_rolados, dados_no_estoque]

#teste
#from funcoes import remover_dado
#print(remover_dado([2, 2, 2, 2], [1], 0))

# funcçãp calcula_pontos_regra_simples (exercicio 4)
def calcula_pontos_regra_simples(dados):
    pontuacao = {}

    for valor in range(1, 7):
        soma = 0
        for dado in dados:
            if dado == valor:
                soma += dado
        pontuacao[valor] = soma

    return pontuacao

# teste
#from funcoes import calcula_pontos_regra_simples
#print(calcula_pontos_regra_simples([2, 3, 4, 5, 2]))

# função calcula_pontos_soma (exercicio 5)
def calcula_pontos_soma(dados):
    soma = 0
    for dado in dados:
        soma += dado
    return soma

#from funcoes import calcula_pontos_soma

#print(calcula_pontos_soma([2, 3, 4, 5, 2]))
