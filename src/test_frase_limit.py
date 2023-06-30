import bot_comando

def test_frase1():
    text = bot_comando.comando("/8frasecc/10", 13)
    assert text == "frase alterada com sucesso"


def test_frase2():
    text = bot_comando.comando("/8frasecc/11.", 13)
    assert text == "maximo tamanho permitido é de 10 caracteres"