from Fala import dizer_escrito
from Escuta import reconhecer


def conta():
    re = reconhecer('Sua conta')
    print(f'VocÊ: {re}')
    if '+' in re:
        res = re.replace('+', '')
        soma(res)
    elif '-' in re:
        res = re.replace('-', '')
        menos(res)
    elif 'x' in re:
        res = re.replace('x', '')
        multiplicar(res)
    elif '/' in re:
        res = re.replace('/', '')
        dividir(res)


def soma(re):
    reso = re.split()
    lista = len(reso)
    soma1 = 0
    for i in range(0, lista):
        soma1 += int(reso[i])
    print(f'Cel: {soma1}')
    dizer_escrito(soma1)


def menos(re):
    reso = re.split()
    menos1 = int(reso[0]) - int(reso[1])
    print(f'Cel: {menos1}')
    dizer_escrito(menos1)


def multiplicar(re):
    reso = re.split()
    lista = len(reso)
    multi = 1
    for i in range(0, lista):
        multi *= int(reso[i])
    print(f'Cel: {multi}')
    dizer_escrito(soma)


def dividir(re):
    reso = re.split()
    dividido = int(reso[0]) / int(reso[1])
    print(f'Cel: {dividido}')
    dizer_escrito(dividido)
