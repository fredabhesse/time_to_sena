import random

# criando listas para definir as váriaveis de acordo com a quantidade de números escolhidos
valores_jogos = [5, 35, 140, 420, 1050, 2310, 4620, 8580, 15015, 25025, 40040, 61880, 92820, 135660, 193800] # valores das apostas
multi_sena = [[1, 1, 1], [1, 6, 1], [1, 12, 15], [1, 18, 45], [1, 24, 90], [1, 30, 150], [1, 36, 225], [1, 42, 315], [1, 48, 420], [1, 54, 540], [1, 60, 675], [1, 66, 825], [1, 72, 990], [1, 78, 1170], [1, 84, 1365]] # multiplicadores para acerto da sena
multi_quina = [[1, 1], [2, 5], [3, 15], [4, 30], [5, 50], [6, 75], [7, 105], [8, 140], [9, 180], [10, 225], [11, 275], [12, 330], [13, 390], [14, 455], [15, 525]] # multiplicadores para acerto da quina
multi_quadra = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120] # multiplicadores para acerto da quadra

# valores médios do prêmio por tipo de acerto nos últimos 36 meses
rateio_sena = 10279529
rateio_quina = 51239
rateio_quadra = 998

def criar_jogo ():
    """
    Cria um jogo com as escolha de x números entre 1 e 60
    
    Retorna:
        list: lista de números escolhida pelo usuário
    """
    numeros_escolhidos = []

    while True:
        try:
            quantidade_numeros = int(input('Informe a quantidade de números que quer jogar (entre 6 e 20): '))
            if 6<= quantidade_numeros <=20:
                break
            else:
                print('Quantidade de números inválida, insira um número entre 6 e 20: ')
        except ValueError:
            print('Valor inválido, informe um número inteiro entre 6 e 20: ')
            
    for _ in range(quantidade_numeros):
        while True:
            try:
                numero = int(input('Escolha um número entre 1 e 60: '))
                if 1<= numero <= 60 and numero not in numeros_escolhidos:
                    numeros_escolhidos.append(numero)
                    print(f'Números selecionados no jogo: {numeros_escolhidos}')
                    break
                else:
                    print(f'Valor inválido, escolha um número entre 1 e 60 e que não esteja selecionado no jogo ainda. Números no jogo:{numeros_escolhidos}.')                                       
            except ValueError:
                print('Número inválido, informe um número inteiro entre 1 e 60: ') 
    return numeros_escolhidos, quantidade_numeros

def criar_sorteio ():
    """
    Realiza um sorteio aleatório com 6 dezenas entre 1 e 60
    
    Retorna:
        numeros_sorteado: lista de números gerados no jogo
    """        
    numeros_sorteados = []
    while len(numeros_sorteados) < 6:
        numero_aleatorio = random.randint(1, 60)
        if numero_aleatorio not in numeros_sorteados:
            numeros_sorteados.append(numero_aleatorio)        
    return sorted(list(numeros_sorteados))

def contar_acertos (lista1, lista2):
    """
    Conta a quantidade de acertos nas duas listas
    
    Args:
    lista1: primeira lista
    lista2: segunda lista
    
    Returns:
    acertos: número de elementos em comum
    """
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    quantidade_acertos = conjunto1.intersection(conjunto2)
    acertos = len(quantidade_acertos)    
    return acertos

def resultado_esperado():
    """
    Define se quer que os sorteios parem após determinado resultado
    
    Returns:
    ponto_de_parada: qual o resultado que irá interromper os sorteios    
    """
    
    while True:
        try:
            ponto_de_parada = str(input('Escolha em qual resultado quer para os sorteios, escolha entre quadra, quina, sena:'))
            if ponto_de_parada == 'quadra' or ponto_de_parada == 'quina' or ponto_de_parada == 'sena':
                print(f'O jogo irá encerrar quando você acertar a primeira {ponto_de_parada}')
            else:
                print('Valor selecionado é inválido, preencha novamente escolhendo um valor conforme está escrito: quadra, quina, sena')
        except:
            print('Valor selecionado é inválido, preencha novamente escolhendo um valor conforme está escrito: quadra, quina, sena')
        return ponto_de_parada

def vitoria():
    """
    Exibe o resultado do jogo após acertar o resultado esperado
    """
    total_gasto = float(repeticao*valor_aposta)
    total_quadra, total_quina, total_sena = [0,0,0]
    print(f'Os números sorteados no concurso {repeticao} foram: {sorteio} - Você acertou {acertos} números - Seu histórico de acertos são:  {sena}, senas | {quina} quinas | {quadra} quadras - Se passaram {int(repeticao/123.33)} anos!')
    print(f'\nSua cartela {jogo} foi premiada! PARABÉNS!')
    print(f'Você apostou em {repeticao} jogos com {len(jogo)} números e precisou de apenas {int(repeticao/114.5)} anos até ser sorteado! Yay!')
    if ponto_de_parada == 'quadra':
        total_quadra = float(rateio_quadra*multi_quadra[index_qt])
        print(f'Pelo seu jogo com {qt_num} números, você recebeu {multi_quadra[index_qt]} vezes o prêmio da quadra, em um total de R$ {total_quadra:,.2f}\n')
    elif ponto_de_parada == 'quina':
        total_quadra = float(rateio_quadra*multi_quina[index_qt][1]*quadra)
        total_quina = float(rateio_quina*multi_quina[index_qt][0]*quina)
        print(f'\nNesse período, com seu jogo com {qt_num} números, você:\nAcertou {quadra} quadras e multiplicou {multi_quina[index_qt][1]} vezes o prêmio, em um total de R$ {total_quadra:,.2f}\nAcertou {quina} quinas e multiplicou {multi_quina[index_qt][0]} vezes o prêmio da quina, em um total de R$ {total_quina:,.2f}\n')
    elif ponto_de_parada == 'sena':
        total_quadra = float(rateio_quadra*multi_sena[index_qt][2]*quadra)
        total_quina = float(rateio_quina*multi_sena[index_qt][1]*quina)
        total_sena = rateio_sena
        print(f'\nNesse período, com seu jogo com {qt_num} números, você:\nAcertou {quadra} quadras e multiplicou {multi_sena[index_qt][2]} vezes o prêmio, em um total de R$ {total_quadra:,.2f}\nAcertou {quina} quinas e multiplicou {multi_sena[index_qt][1]} vezes o prêmio da quina, em um total de R$ {total_quina:,.2f}\nAcertou a sena, em um total de R$ {rateio_sena:,.2f}\n')
    print(f'Seu gasto total foi de:  R$ {total_gasto:,.2f}')
    print(f'Seu prêmio total foi de: R$ {total_quadra + total_quina + total_sena:,.2f}\n')

if __name__ == '__main__':
    repeticao = 1
    quadra, quina, sena = [0,0,0]
    sorteio = []
    jogo, qt_num = criar_jogo()
    index_qt = qt_num-6
    valor_aposta = valores_jogos[index_qt]
    jogo.sort()
    print(f'\nOs números que você selecionou para o sorteio são: {jogo}\nCada Jogo vai custar R${valor_aposta:,.2f}\n')
    ponto_de_parada = resultado_esperado()
    while jogo != sorteio:
        sorteio = criar_sorteio()
        acertos = contar_acertos(sorteio, jogo)
        if acertos == 4:
            quadra += 1
            if ponto_de_parada == 'quadra':
                vitoria()
                break
        elif acertos == 5:
            quina += 1
            if ponto_de_parada == 'quina':
                vitoria()
                break
        elif acertos == 6:
            sena += 1
            if ponto_de_parada == 'sena':
                vitoria()
                break    
        print(f'Os números sorteados no concurso {repeticao} foram: {sorteio} - Você acertou {acertos} números - Seu histórico de acertos são:  {sena}, senas | {quina} quinas | {quadra} quadras - Se passaram {int(repeticao/123.33)} anos!')
        repeticao += 1