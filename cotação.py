import requests
from datetime import datetime
from funcoes_e_classes import leiadinheiro, dinheiro_formatado, enviar_email_simplificado

print('[ SISTEMA DE COTAÇÃO DE MOEDAS ]')
data_atual = datetime.strftime(datetime.now(), '%d/%m/%Y')
print(f'Data atual: {data_atual}')
print('=' * 35)

requisicao = requests.get(
    'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BRL-USD,BRL-EUR,USD-EUR,EUR-USD').json()
# print(requisicao)

lista_de_moedas = ['USDBRL', 'EURBRL']
dic_moedas = {1: 'USD', 2: 'BRL', 3: 'EUR'}
contatos = ['rafa.enfo@hotmail.com', 'nutricao.eciencia1@gmail.com', 'gabrielendeoliveira@gmail.com']
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
                                            '[3] - Voltar\n'
                                            'Sua escolha: '))
                print('-' * 50)
                if escolha_cotacao == 3:
                    break
                elif escolha_cotacao not in (1, 2):
                    print('Opção inválida.')
                else:
                    # Pega a cotação da moeda escolhida
                    moeda = lista_de_moedas[escolha_cotacao - 1]
                    mensagem_exibida = f'Hoje, {data_atual}, R$1,00 representa:\n'\
                                       f'Cotação {moeda}: {dinheiro_formatado(requisicao[f"{moeda}"]["bid"])}\n'\
                                       f'Flutuação diária:\n'\
                                       f'Mínima: {dinheiro_formatado(requisicao[moeda]["low"])}\n'\
                                       f'Máxima: {dinheiro_formatado(requisicao[moeda]["high"])}\n'

                    print(mensagem_exibida)
                    verif_envio_email = str(input(f'Deseja enviar email com o conteúdo acima'
                                             f' para {contatos}? [S/N]')).upper()
                    if verif_envio_email not in ('Ss' or 'Nn'):
                        print('Opção errada, e-mail não enviado.')
                    elif verif_envio_email == 'S':
                        enviar_email_simplificado(mensagem_exibida, contatos)
                        print('E-mail enviado!')
                    elif verif_envio_email == 'N':
                        print('Email não enviado!')

            except (ValueError, TypeError):
                print('Erro no tipo ou valor.')
            except Exception as erro:
                print(f'Erro: {erro.__cause__}')
            print('-' * 50)
    elif escolha_usuario == '2':
        while True:
            try:
                valor = leiadinheiro('Digite um valor de dinheiro: ')
                while True:
                    print('-' * 50)
                    moeda_inicial = int(input('Moeda inicial:\n'
                                              '[1] - Dólar\n'
                                              '[2] - Real\n'
                                              '[3] - Euro\n'
                                              'Sua escolha: '))
                    if moeda_inicial not in (1, 2, 3):
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
                                             'Sua escolha: '))
                    if moeda_cambio not in (1, 2, 3):
                        print('Moeda de câmbio inválida.')
                    else:
                        # Pega a sigla da moeda de câmbio escolhida, de acordo com o dicionário de moedas..
                        moeda_cambio = dic_moedas[moeda_cambio]
                        # print(moeda_cambio)
                        break
                # concatenação das siglas da moeda inicial + moeda de câmbio, na posição "bid" (cotação), * o valor
                # escolhido pelo usuário.
                conversao = float(requisicao[moeda_inicial+moeda_cambio]["bid"]) * valor
                print(f'A conversão de {dinheiro_formatado(valor)} {moeda_inicial} para '
                      f'{moeda_cambio} é: {dinheiro_formatado(conversao)}')
                break
            except (ValueError, TypeError):
                print('Erro no tipo ou valor.')
            except Exception as causa:
                print(f'Ocorreu algum erro: {causa.__cause__}. Talvez não seja uma combinação válida.')
    elif escolha_usuario == '3':
        print('Encerrado.')
        break
    else:
        print('Valor errado.')
