import speech_recognition as sr
from Fala import dizer_escrito


# Função que reconhecer o audio do pc.
def reconhecer(texto):

    r = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        with mic as fonte:
            r.adjust_for_ambient_noise(fonte)
            dizer_escrito(texto)
            audio = r.listen(fonte)

            try:
                text = r.recognize_google(audio, language="pt-BR")
                texto_mini = str(text).lower()
                if texto_mini != '':
                    break

            except:
                dizer_escrito("Desculpa, não entendi o que você disse, pode repetir?")

    return texto_mini
