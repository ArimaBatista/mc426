import bot_comando
import banco
def test_limit0():
    banco.deleta_id(7)
    text = bot_comando.comando("cadastro jose sampa 100000000000 medico", 7)
    assert text == "provavelmente digitou numero a mais"

def test_limit1():
    banco.deleta_id(7)
    text = bot_comando.comando("cadastro jose sampa 9999999999 medico", 7)
    assert text == "provavelmente digitou um digito a menos"

def test_limit2():
    banco.deleta_id(7)
    text = bot_comando.comando("cadastro jose sampa 99999999999 medico", 7)
    assert text == "o numero aceito"

def test_limit3():
    banco.deleta_id(7)
    text = bot_comando.comando("cadastro jose sampa wakwak medico", 7)
    assert text == "numero invalido"

def test_limit2():
    banco.deleta_id(7)
    text = bot_comando.comando("cadastro jose sampa 10000000000 medico", 7)
    assert text == "o numero aceito"

