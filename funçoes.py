from Fala import dizer_escrito
import os
from Escuta import reconhecer

# Aqui estarao todas as funçoes do chatbot


# Função de fala primaria do chatbot
def LeiaValor(msg):
    # Função que verfica se a opção escolhida esta no ideal
    while True:
        try:
            n = int(msg)
        except (ValueError, TypeError):
            print("ERROR! Digite um número inteiro válido!")
            continue
        except KeyboardInterrupt:
            print("ERROR! O usuário não preferiu digitar esse número!")
            return 0
        else:
            return n


def execulta_programas():
    programa = reconhecer()
    dizer_escrito(f'Execultando {programa}')
    if programa == 'bloco de notas':
        os.startfile('notepad.exe')
    elif programa == 'navegador':
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.LNK')





