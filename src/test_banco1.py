import banco


def test_1():
    banco.deleta_id(1)
    banco.inserir_pessoa(1,"joão","sampa","sabado domingo","medico")
    dado=banco.pesquisa_id(1)
    assert dado == (1, 'joão', 'sampa', 'sabado domingo', 'medico')
    banco.deleta_id(1)

def test_2():
    banco.deleta_id(2)
    banco.inserir_pessoa(2,"mira","roberto","tercao sabado","psicologo")
    dado=banco.pesquisa_id(2)
    assert dado == (2, 'mira', 'roberto', 'tercao sabado', 'psicologo')
    banco.deleta_id(2)
    

def test_3():
    banco.deleta_id(3)
    banco.inserir_pessoa(3,"kira","brasilia","terca domingo","psiquiatra")
    dado=banco.pesquisa_id(3)
    assert dado == (3, 'kira', 'brasilia', 'terca domingo', 'psiquiatra')
    banco.deleta_id(3)