from chatbot import interagir
from Escuta import reconhecer
from Interface.Codigo_Interface import *
from Fala import dizer_escrito
from Funçoes_Matematicas.Areas_Figuras_Planas import conta_Areas
from Funçoes_Matematicas.Operçoes_Simples import conta
from Dados_RPG import dado_rpg
from Funçoes_Matematicas.Perimetro_Figuras_Planas import conta_perimetro
import Wikepedia


# Programa principal

'''dizer_escrito('Por favor digite a senha que meu criador lhe deu')

while True:
    senha = str(input('Senha: '))
    if senha == '31102002':
        break
    else:
        dizer_escrito('Senha Incorreta')



tela_inicial()
dizer_escrito('Muito bem, só pela curiosidade essa é a data do aniversário do meu criador')
dizer_escrito('Seja bem vindo, meu nome é Cel, sou uma assistente virtual criada para ajudar vocÊ, parabÊns por ser a primeira pessoa a testar')
dizer_escrito('Caso queira ver o que posso fazer basta dizer precisso de ajuda e mostrarei os comandos')'''
while True:
    sair = ["sair", "encerrar", "fechar programa", "cessar funções motoras"]
    entrada = str(reconhecer('O que posso ajudar'))
    for i in sair:
        if (entrada in i):
            dizer_escrito("Programa encerrado")
            print("Programa encerrado")
            exit()

    if 'dado' in entrada :
        print(f'VocÊ: {entrada}')
        dado_rpg()
    elif 'ajuda' in entrada:
        print(f'VocÊ: {entrada}')
        tela_ajuda()
    elif 'figuras planas' in entrada:
        print(f'VocÊ: {entrada}')
        conta_Areas()
    elif 'calculadora' in entrada:
        print(f'VocÊ: {entrada}')
        conta()
    elif 'perímetro' in entrada:
        print(f'VocÊ: {entrada}')
        conta_perimetro()
    elif 'pesquisa' in entrada:
        print(f'VocÊ: {entrada}')
        texto = entrada.replace('pesquisa', '')
        Wikepedia.modulopesquisa(texto)

    else:
        saida = interagir(entrada)
        print("VocÊ:" + entrada)
        print("Cel:" + saida)
        dizer_escrito(saida)




