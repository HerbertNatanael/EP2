import random

# função para rolar os dados (exercicio 1)
def rolar_dados(qtd):
    dados = []
    for _ in range(qtd):
        dados.append(random.randint(1, 6))
    return dados

#from funcoes import rolar_dados (adicionar no arquivo final)

# print(rolar_dados(5)) teste da função rolar_dados

# função para guardar um dado (exercicio 2)
def guardar_dado(dados_rolados, dados_no_estoque, indice):
    dado = dados_rolados.pop(indice)
    dados_no_estoque.append(dado)
    return [dados_rolados, dados_no_estoque]