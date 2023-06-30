import telebot
import bot_credencial
import bot_comando


bot = bot_credencial.bot
meu_bot_handler = bot.message_handler 


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    
    mensagem_texto = mensagem.text
    texto= bot_comando.comando(mensagem_texto,mensagem.chat.id)
    bot.reply_to(mensagem, texto)
bot.polling()