import pyttsx3
engine = pyttsx3.init()


# Funçao que fala o que esta escito


def dizer_escrito(fala):
    engine.say(fala)
    print(f'Cel: {fala}')
    engine.runAndWait()
    engine.stop()
