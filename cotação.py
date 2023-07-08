import requests
from datetime import datetime

print('     SISTEMA DE COTAÇÃO DE MOEDAS')
data_atual = str(datetime.today())
print(f'Data atual: {data_atual}')
print('=' * 40)

requisicao = requests.get(
    'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BRL-USD,BRL-EUR,USD-EUR,EUR-USD,JPY-BRL,BRL-JPY').json()
print(requisicao)
lista_de_moedas = ['USDBRL', 'EURBRL', 'BRLUSD', 'BRLEUR', 'USDEUR', 'EURUSD']
dic_moedas = {1: 'USD', 2: 'BRL', 3: 'EUR', 4: 'JPY'}
while True:
    print('Escolha uma opção: ')
    escolha_usuario = str(input('[1] - Ver cotação de alguma moeda\n'
                                '[2] - Converter moeda\n'
                                '[3] - Encerrar\n'
                                'Sua escolha: '))
    if escolha_usuario == '1':
        while True:
            try:
                escolha_cotacao = int(input('Quer ver a cotação de qual moeda?\n'
                                            '[1] - Dólar\n'
                                            '[2] - Euro\n'
                                            '[3] - Encerrar\n'
                                            'Sua escolha: '))
                if escolha_cotacao == 3:
                    break
                elif escolha_cotacao != 1 and escolha_cotacao != 2:
                    print('Opção inválida.')
                else:
                    moeda = lista_de_moedas[escolha_cotacao - 1]
                    print(f'Cotação {moeda}: {requisicao[f"{moeda}"]["bid"]}')
                    print('Flutuação diária:')
                    print(f'Mínima: {requisicao[moeda]["low"]}\n'
                          f'Máxima: {requisicao[moeda]["high"]}')
            except (ValueError, TypeError):
                print('Erro no tipo ou valor.')
            except Exception as erro:
                print(f'Erro: {erro.__cause__}')
            print('-' * 40)
    elif escolha_usuario == '2':
        while True:
            valor = float(input('Digite um valor de dinheiro: '))
            while True:
                moeda_inicial = int(input('Moeda inicial:\n'
                                          '[1] - Dólar\n'
                                          '[2] - Real\n'
                                          '[3] - Euro\n'
                                          '[4] - Iene japonês\n'
                                          'Sua escolha: '))
                if moeda_inicial not in (1, 2, 3, 4):
                    print('Moeda inicial inválida.')
                else:
                    moeda_inicial = dic_moedas[moeda_inicial]
                    print(moeda_inicial)
                    break
            while True:
                moeda_cambio = int(input('Moeda de câmbio:\n'
                                         '[1] - Dólar\n'
                                         '[2] - Real\n'
                                         '[3] - Euro\n'
                                         '[4] - Iene japonês\n'
                                         'Sua escolha: '))
                if moeda_cambio not in (1, 2, 3, 4):
                    print('Moeda de câmbio inválida.')
                else:
                    moeda_cambio = dic_moedas[moeda_cambio]
                    print(moeda_cambio)
                    break
            conversao = float(requisicao[moeda_inicial+moeda_cambio]["bid"]) * valor
            print(f'A conversão de {moeda_inicial} para {moeda_cambio} é: {conversao:.2f}')
            break
    elif escolha_usuario == '3':
        print('Encerrado.')
        break
    else:
        print('Valor errado.')
