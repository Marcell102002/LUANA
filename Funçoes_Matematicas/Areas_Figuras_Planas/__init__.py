from Escuta import reconhecer
from Fala import dizer_escrito


def conta_Areas():
    re = reconhecer('A figura que vocÊ quer calcular a área')
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
    lado1 = int(reconhecer('Primeiro Lado'))
    print(f'VocÊ: {lado1}')
    lado2 = int(reconhecer('Segundo lado'))
    print(f'VocÊ: {lado2}')
    area = lado2 * lado1
    dizer_escrito(f'A área é {area}')


def circulo():
    raio = int(reconhecer('Qual é o raio'))
    print(f'VocÊ: {raio}')
    area = (raio*raio)*3.14
    dizer_escrito(f'A área é {area}')


def triangulo():
    base = int(reconhecer('Qual é a base '))
    print(f'VocÊ: {base}')
    altura = int(reconhecer('Qual é a altura'))
    print(f'VocÊ: {altura}')
    area = (base * altura) / 2
    dizer_escrito(f'A área é {area}')


def retangulo():
    base = int(reconhecer('Qual é a base '))
    print(f'VocÊ: {base}')
    altura = int(reconhecer('Qual é a altura'))
    print(f'VocÊ: {altura}')
    area = base * altura
    dizer_escrito(f'A área é {area}')


def losango():
    diagonal_maior = int(reconhecer('Qual é a diagonal maior'))
    print(f'VocÊ: {diagonal_maior}')
    diagonal_menor = int(reconhecer('Qual é a diagonal menor'))
    print(f'VocÊ: {diagonal_menor}')
    area = (diagonal_menor * diagonal_maior) / 2
    dizer_escrito(f'A área é {area}')


def trapezio():
    base_maior = int(reconhecer('Qual é a base maior'))
    print(f'VocÊ: {base_maior}')
    base_menor = int(reconhecer('Qual é a base menor'))
    print(f'VocÊ: {base_menor}')
    altura = int(reconhecer('Qual é a altura'))
    print(f'VocÊ: {altura}')
    area = ((base_maior+base_menor)*altura)/2
    dizer_escrito(f'A área é {area}')

