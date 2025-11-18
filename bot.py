import telebot
from telebot.types import Message

BOT_TOKEN = "8214147862:AAFMbLvhl4oBStxvNjIv1GyWQ0h47Wm_g9U"
OWNER_ID = 7683386917

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

WELCOME_TEXT = """💐Hello, Nice to meet you ! I am a receptionist !

For verification Please Provide!

Payment Code :
WhatsApp number:
"""

@bot.message_handler(content_types=['new_chat_members'])
def greet_new_member(message):
    bot.send_message(message.chat.id, WELCOME_TEXT)

@bot.message_handler(func=lambda m: m.chat.type in ['group', 'supergroup'])
def forward_group_messages(message):
    try:
        bot.forward_message(OWNER_ID, message.chat.id, message.message_id)
    except:
        pass

@bot.message_handler(func=lambda m: m.chat.type == "private")
def forward_private(message: Message):
    bot.forward_message(OWNER_ID, message.chat.id, message.message_id)

@bot.message_handler(func=lambda m: m.reply_to_message and m.chat.id == OWNER_ID)
def owner_reply(message: Message):
    try:
        original_user = message.reply_to_message.forward_from.id
        bot.send_message(original_user, message.text)
    except:
        bot.send_message(OWNER_ID, "❌ Reply user tak nahi pahucha.")

bot.polling()
