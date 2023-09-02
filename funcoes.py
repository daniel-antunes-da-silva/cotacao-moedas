def leiadinheiro(mensagem):
    while True:
        valor = input(mensagem)
        if ',' in valor:
            valor = valor.replace(',', '.')
        qtd_pontos = valor.count('.')
        if (qtd_pontos == 0 or qtd_pontos == 1) and valor.replace('.', '').isnumeric():
            valor = float(valor)
            break
        else:
            print(f'"{valor}" é um valor incorreto! ')
    return valor


def dinheiro_formatado(n):
    try:
        n = float(n)
    except:
        return None
    else:
        return f'{n:.2f}'.replace('.', ',')
