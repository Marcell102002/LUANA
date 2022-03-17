import wikipedia
from Fala import dizer_escrito
from time import sleep

wikipedia.set_lang("pt")

def modulopesquisa(text):
    try:
        dizer_escrito('Execultando pesquisa')
        pesquisa = wikipedia.summary(text)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print()
    except:
        dizer_escrito('Pesquisa não achada')
    else:
        dizer_escrito(pesquisa)