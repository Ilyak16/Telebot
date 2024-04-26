import telebot
from telebot import types

Bot = telebot.TeleBot("6347526208:AAGYpTiCyHGZ-jFqfqr0kYp9bb0xdasrT90")
@Bot.message_handler(commands=["start"])
def main(message):
    button_surprise = types.InlineKeyboardMarkup()
    button_surprise.add(types.InlineKeyboardButton("Сюрприз", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
    Bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.username}. Вы начали работу с ботом DST_Guide_Bot", reply_markup=button_surprise)

@Bot.message_handler(commands=["help"])
def main(message):
    Bot.send_message(message.chat.id, "Help info")

@Bot.message_handler()
def main(message):
    if message.text.lower() == "hello":
        Bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.username}. Вы начали работу с ботом DST_Guide_Bot")
    if message.text.lower() == "id":
        Bot.reply_to(message, f"ID: {message.from_user.id}")
@Bot.message_handler(content_types=['photo'])
def get_photo(message):
    Bot.reply_to(message, "Какое красивое фото ;)")

Bot.polling(non_stop=True)