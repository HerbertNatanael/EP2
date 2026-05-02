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

#calcula_pontos_sequencia_baixa (exercicio 6)
def calcula_pontos_sequencia_baixa(dados):
    dados_unicos = sorted(set(dados))

    for i in range(len(dados_unicos) - 3):
        if (dados_unicos[i] + 1 == dados_unicos[i + 1] and
            dados_unicos[i] + 2 == dados_unicos[i + 2] and
            dados_unicos[i] + 3 == dados_unicos[i + 3]):
            return 15

    return 0

# teste/
#from funcoes import calcula_pontos_sequencia_baixa

#print(calcula_pontos_sequencia_baixa([5, 3, 4, 2, 2]))  # 15
#print(calcula_pontos_sequencia_baixa([2, 3, 4, 6, 2]))  # 0

# calcula_pontos_sequencia_alta (exercicio 7)
def calcula_pontos_sequencia_alta(dados):
    dados_unicos = sorted(set(dados))

    for i in range(len(dados_unicos) - 4):
        if (dados_unicos[i] + 1 == dados_unicos[i + 1] and
            dados_unicos[i] + 2 == dados_unicos[i + 2] and
            dados_unicos[i] + 3 == dados_unicos[i + 3] and
            dados_unicos[i] + 4 == dados_unicos[i + 4]):
            return 30

    return 0

# teste
#from funcoes import calcula_pontos_sequencia_alta

#print(calcula_pontos_sequencia_alta([5, 4, 1, 3, 2, 1]))  # 30
#print(calcula_pontos_sequencia_alta([2, 3, 4, 6, 2]))    # 0

# Exercício 8 - calcula_pontos_full_house
def calcula_pontos_full_house(dados):
    for valor in set(dados):
        if dados.count(valor) == 3:
            for outro in set(dados):
                if outro != valor and dados.count(outro) == 2:
                    
                    soma = 0
                    for d in dados:
                        soma += d
                    
                    return soma
    return 0

# Exercício 9 - calcula_pontos_quadra
def calcula_pontos_quadra(dados):
    for valor in set(dados):
        if dados.count(valor) >= 4:
            soma = 0
            for d in dados:
                soma += d
            return soma
    return 0