from Escuta import reconhecer
from Fala import dizer_escrito


def conta_perimetro():
    re = reconhecer('Qual figura vai calcular?')
    print(f'VocÊ: {re}')

    if 'quadrado' in re:
        quadrado()
    elif 'círculo' in re:
        circulo()
    elif 'triângulo' in re:
        triangulo()
    elif 'retângulo' in re:
        retangulo()
    elif 'losango' in re:
        losango()
    elif 'trapézio' in re:
        trapezio()


def quadrado():
    lado = int(reconhecer('Um Lado'))
    print(f'VocÊ: {lado}')
    perimetro = lado * 4
    dizer_escrito(f'O perimetro é {perimetro}')


def circulo():
    raio = int(reconhecer('O raio'))
    print(f'VocÊ: {raio}')
    perimetro = 2 * 3, 14 * raio
    print(f'Cel: {perimetro}')
    dizer_escrito(f'O perimetro é {perimetro}')


def triangulo():
    lado = int(reconhecer('Um Lado'))
    print(f'VocÊ: {lado}')
    perimetro = lado * 3
    print(f'Cel: {perimetro}')
    dizer_escrito(f'O perimetro é {perimetro}')


def retangulo():
    base = int(reconhecer('A base'))
    print(f'VocÊ: {base}')
    altura = int(reconhecer('A altura'))
    print(f'VocÊ: {base}')
    perimetro = 2 * (base + altura)
    print(f'Cel: {perimetro}')
    dizer_escrito(f'O perimetro é {perimetro}')


def losango():
    lado = int(reconhecer('Um Lado'))
    print(f'VocÊ: {lado}')
    perimetro = lado * 4
    print(f'Cel: {perimetro}')
    dizer_escrito(f'O perimetro é {perimetro}')


def trapezio():
    base_maior = int(reconhecer('Qual é a base maior'))
    print(f'VocÊ: {base_maior}')
    base_menor = int(reconhecer('Qual é a base menor'))
    print(f'VocÊ: {base_menor}')
    lado1 = int(reconhecer('Primeiro Lado'))
    print(f'VocÊ: {lado1}')
    lado2 = int(reconhecer('Segundo lado'))
    print(f'VocÊ: {lado2}')
    perimetro = base_maior + base_menor + lado2 + lado1
    print(f'Cel: {perimetro}')
    dizer_escrito(f'O perimetro é {perimetro}')
