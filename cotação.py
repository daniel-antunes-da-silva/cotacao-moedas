import requests
from datetime import datetime

print('     SISTEMA DE COTAÇÃO DE MOEDAS')
data_atual = str(datetime.today())
print(f'Data atual: {data_atual}')
print('='*40)

requisicao = requests.get(
      'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL').json()

print(f'Dólar: ')
print(f'Cotação: {requisicao["USDBRL"]["bid"]}')
print('Flutuação diária:')
print(f'Mínima: {requisicao["USDBRL"]["low"]}\n'
      f'Máxima: {requisicao["USDBRL"]["high"]}')
print('='*40)
print('Euro: ')
print(f'Cotação: {requisicao["EURBRL"]["bid"]}')
print('Flutuação diária:')
print(f'Mínima: {requisicao["EURBRL"]["low"]}')
print(f'Máxima: {requisicao["EURBRL"]["high"]}')













'''verif = str(input('Quer ver sobre um período específico? [s/n]')).lower()
if verif == 's':
      ano = int(input('Ano: '))
      mes = int(input('Mês: '))
      dia = 
'''

