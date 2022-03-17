import os

def lertudo(complemento="/inform.txt"):

    os.chdir(r'D:\Cel')
    caminho = os.getcwd() + complemento

    arq = open(caminho, 'r')
    info = arq.readlines()
    arq.close()

    return info

def interagir(entrada):
    from chatbot import lertudo

    resposta = "Desculpe, não tenho resposta para isso"

    arq = lertudo()
    inputs = lertudo("/BD/TXT/entrada.txt")
    outputs = lertudo("/BD/TXT/saida.txt")

    n = 0
    for i in inputs:

        if (entrada + "\n" == i):
            resposta = outputs[n]

            return resposta
        n += 1

    return resposta