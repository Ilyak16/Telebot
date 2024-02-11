import telebot

Bot = telebot.TeleBot("6347526208:AAGYpTiCyHGZ-jFqfqr0kYp9bb0xdasrT90")
@Bot.message_handler(commands=["start"])
def main(message):
    Bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.username}. Вы начали работу с ботом DST_Guide_Bot")

@Bot.message_handler(commands=["help"])
def main(message):
    Bot.send_message(message.chat.id, "Help info")

@Bot.message_handler()
def main(message):
    if message.text.lower() == "hello":
        Bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.username}. Вы начали работу с ботом DST_Guide_Bot")
    if message.text.lower() == "id":
        Bot.reply_to(message, f"ID: {message.from_user.id}")
Bot.polling(non_stop=True)