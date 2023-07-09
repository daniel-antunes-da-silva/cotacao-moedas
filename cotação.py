import requests
from datetime import datetime

print('     SISTEMA DE COTAÇÃO DE MOEDAS')
data_atual = str(datetime.today())
print(f'Data atual: {data_atual}')
print('=' * 50)

requisicao = requests.get(
    'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BRL-USD,BRL-EUR,USD-EUR,EUR-USD,JPY-BRL,BRL-JPY').json()
# print(requisicao)
lista_de_moedas = ['USDBRL', 'EURBRL', 'JPYBRL']
dic_moedas = {1: 'USD', 2: 'BRL', 3: 'EUR', 4: 'JPY'}
while True:
    print('Escolha uma opção: ')
    escolha_usuario = str(input('[1] - Ver cotação de alguma moeda\n'
                                '[2] - Converter moeda\n'
                                '[3] - Encerrar\n'
                                'Sua escolha: '))
    print('-' * 50)
    if escolha_usuario == '1':
        while True:
            try:
                escolha_cotacao = int(input('Quer ver a cotação de qual moeda?\n'
                                            '[1] - Dólar\n'
                                            '[2] - Euro\n'
                                            '[3] - Iene japonês\n'
                                            '[4] - Encerrar\n'
                                            'Sua escolha: '))
                print('-' * 50)
                if escolha_cotacao == 4:
                    break
                elif escolha_cotacao not in (1, 2, 3):
                    print('Opção inválida.')
                else:
                    # Pega a cotação da moeda escolhida
                    moeda = lista_de_moedas[escolha_cotacao - 1]
                    print('1 real representa: ')
                    print(f'Cotação {moeda}: {requisicao[f"{moeda}"]["bid"]}')
                    print('Flutuação diária:')
                    print(f'Mínima: {requisicao[moeda]["low"]}\n'
                          f'Máxima: {requisicao[moeda]["high"]}')
            except (ValueError, TypeError):
                print('Erro no tipo ou valor.')
            except Exception as erro:
                print(f'Erro: {erro.__cause__}')
            print('-' * 50)
    elif escolha_usuario == '2':
        while True:
            try:
                valor = float(input('Digite um valor de dinheiro: '))
                while True:
                    print('-' * 50)
                    moeda_inicial = int(input('Moeda inicial:\n'
                                              '[1] - Dólar\n'
                                              '[2] - Real\n'
                                              '[3] - Euro\n'
                                              '[4] - Iene japonês\n'
                                              'Sua escolha: '))
                    if moeda_inicial not in (1, 2, 3, 4):
                        print('Moeda inicial inválida.')
                    else:
                        # Pega a sigla da moeda inicial escolhida, de acordo com o dicionário de moedas.
                        moeda_inicial = dic_moedas[moeda_inicial]
                        # print(moeda_inicial)
                        break
                while True:
                    print('-' * 50)
                    moeda_cambio = int(input('Moeda de câmbio:\n'
                                             '[1] - Dólar\n'
                                             '[2] - Real\n'
                                             '[3] - Euro\n'
                                             '[4] - Iene japonês\n'
                                             'Sua escolha: '))
                    if moeda_cambio not in (1, 2, 3, 4):
                        print('Moeda de câmbio inválida.')
                    else:
                        # Pega a sigla da moeda de câmbio escolhida, de acordo com o dicionário de moedas..
                        moeda_cambio = dic_moedas[moeda_cambio]
                        # print(moeda_cambio)
                        break
                # concatenação das siglas da moeda inicial + moeda de câmbio, na posição "bid" (cotação), * o valor
                # escolhido pelo usuário.
                conversao = float(requisicao[moeda_inicial+moeda_cambio]["bid"]) * valor
                print(f'A conversão de {valor} {moeda_inicial} para {moeda_cambio} é: {conversao:.2f}')
                break
            except (ValueError, TypeError):
                print('Erro no tipo ou valor.')
            except Exception as causa:
                print(f'Ocorreu algum erro: {causa.__cause__}')
    elif escolha_usuario == '3':
        print('Encerrado.')
        break
    else:
        print('Valor errado.')
