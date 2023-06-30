import bot_busca_profissional
import banco
frase_dia = "bom dia"

def comando(text, id):
    global frase_dia
    dado=banco.pesquisa_id(id)
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
        text= "digite cadastrar nome cidade telefone  profissao"
    elif text[:3] == "cad":
        palavra = text.split()
        temp = anl_tel(palavra[3])
        if temp[1] =="o":
            banco.inserir_pessoa(id, palavra[1], palavra[2], palavra[3], palavra[4])
            text="cadastrado"
        else:
            text = temp
    elif text[1] == "5":
         text ="""Nós somos um grupo de estudantes que está desenvolvendo um sistema automatizado para auxiliar pessoas em seus tratamentos relacionados à ansiedade, depressão, obesidade e dependência química. Desenvolvemos essa aplicação com a esperança de que ela possa ser útil de alguma forma.
/voltar"""
    elif text[1] == "7":
         text = frase_dia
    elif text[1] == "8":
        if dado != None:
            text = text[3:]
            n = len(text)
            if n < 10:
                frase_dia = text
                text = "frase alterada com sucesso"
            else:
                text ="maximo tamanho permitido é de 10 caracteres"
        else: text = "erro"
    elif text[1] == "6":
        if dado != None:
            texto="escolha /editar_nome /editar_profissao /editar_telefone /editar_localidade seus dadois atuais são"
            text = texto + dado
        else: text = "erro"
    elif text == "/editar_telefone":
        if dado != None:
            text="digite novo_telefone(xx)xxxxx-xxxx"
        else: text = "erro"   
    else:
        if dado != None:
            text="""Olá, sou um assistente virtual aqui para auxiliá-lo hoje. Por favor, selecione uma das opções abaixo:
selecione /1 se estiver passando por uma crise
selecione /2 para encontrar um profissional da saúde
selecione /3 para encontrar um grupo de apoio
selecione /6 para editar seus dados
selecione /5 se quiser saber mais sobre o nosso sistemama
selecione /8+frase para alterar a frase do dia"""
        else:
            text="""Olá, sou um assistente virtual aqui para auxiliá-lo hoje. Por favor, selecione uma das opções abaixo:
selecione /1 se estiver passando por uma crise
selecione /2 para encontrar um profissional da saúde
selecione /3 para encontrar um grupo de apoio
selecione /4 caso seja um profissional da area da suade
selecione /5 se quiser saber mais sobre o nosso sistemama
selecione /7 para ver a frase do dia"""
        

    return text
def anl_tel(numero):
    try:
        n = int(numero)
        print("nen")
        if n >= 100000000000:
            numero = "provavelmente digitou numero a mais"
        elif n <=9999999999:
            numero = "provavelmente digitou um digito a menos"
        else:
            numero = "o numero aceito"
    except:
        numero="numero invalido"
    return numero