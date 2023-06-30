import bot_comando

def test_esquiva1():
    text = bot_comando.comando("da",1)
    assert text =="""Olá, sou um assistente virtual aqui para auxiliá-lo hoje. Por favor, selecione uma das opções abaixo:
selecione /1 se estiver passando por uma crise
selecione /2 para encontrar um profissional da saúde
selecione /3 para encontrar um grupo de apoio
selecione /4 caso seja um profissional da area da suade
selecione /5 se quiser saber mais sobre o nosso sistemama"""

def test_esquiva2():
    text = bot_comando.comando("da",13)
    assert text =="""Olá, sou um assistente virtual aqui para auxiliá-lo hoje. Por favor, selecione uma das opções abaixo:
selecione /1 se estiver passando por uma crise
selecione /2 para encontrar um profissional da saúde
selecione /3 para encontrar um grupo de apoio
selecione /6 para editar seus dados
selecione /5 se quiser saber mais sobre o nosso sistemama"""


def test_esquiva4():
    text = bot_comando.comando("/6",1)
    assert text == "erro"

def test_esquiva5():
    text = bot_comando.comando("/editar_telefone",12)
    assert text == "erro"

def test_esquiva6():
    text = bot_comando.comando("/editar_telefone",24)
    assert text == "digite novo_telefone(xx)xxxxx-xxxx"
