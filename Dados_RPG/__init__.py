from random import randint
from Escuta import reconhecer
from Fala import dizer_escrito


'''def reconhecerdado():
    re = reconhecer('fale algo')
    if 'dado rpg' or 'role um dado' or 'dados rpg' in re:
        dado_rpg()'''


def dado_rpg():
    while True:

        try:
            lados = int(reconhecer('Quantos lados tem o dado?'))
            print(f'VocÊ: {lados}')
            valor_elatorio = randint(1, lados)
        except (ValueError):
            dizer_escrito('Por favor fale um número inteiro.')
        else:
            dizer_escrito(f'O resultado é {valor_elatorio}')
            continuar = reconhecer('Pretende continuar jogando dados?')
            print(f'VocÊ: {continuar}')
            if 'não' in continuar:
                break
            else:
                dizer_escrito('ok!')
