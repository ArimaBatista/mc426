import bot_busca_profissional

def comando(text, id):
    if text[1] == "1":
        text =""""Você não está sozinho/a. Há ajuda disponível. Procure apoio e se recupere."

"Você importa. Sua saúde mental é importante. Busque ajuda profissional para superar essa crise."

"Não tenha medo de pedir ajuda. Há pessoas dispostas a apoiar você. Ligue para [número de uma linha de apoio] agora mesmo."

Gostaria de oferecer esses dois videdeos da Psicologa Rosangela e do Dr. Drauzio Varella:

https://youtu.be/UClcL_lsrF4

https://youtu.be/8YG8HABY25w

/voltar"""
    elif text[1] == "2":
        text = bot_busca_profissional.busca_profissional(text)
    elif text[1] == "3":
        text ="""Grupo para quem esta lutando contra as drogas:  https://t.me/+Qu7rRgq9QO8zODEx
Grupo para quem esta lutando contra obesidade: https://t.me/+ZaKk1L5RZ7s1ZDMx
Grupo para quem esta lutando contra depressão e ansiedade: https://t.me/+j1ylkh1QCjhlYjkx
/voltar."""
    elif text[1] == "4":
         text= "em branco"
    elif text[1] == "5":
         text ="""Nós somos um grupo de estudantes que está desenvolvendo um sistema automatizado para auxiliar pessoas em seus tratamentos relacionados à ansiedade, depressão, obesidade e dependência química. Desenvolvemos essa aplicação com a esperança de que ela possa ser útil de alguma forma.
/voltar"""
    else:
            text="""
            Olá, sou um assistente virtual aqui para auxiliá-lo hoje. Por favor, selecione uma das opções abaixo:
            selecione /1 se estiver passando por uma crise
            selecione /2 para encontrar um profissional da saúde
            selecione /3 para encontrar um grupo de apoio
            selecione /4 caso seja um profissional da area da suade
            selecione /5 se quiser saber mais sobre o nosso sistemama
            """
        

    return text