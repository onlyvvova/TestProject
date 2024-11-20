import telebot
from telebot import types   
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7295431439:AAG5j42KN6-ajiOQaY_vERBofSnmdg_z5M0")
    
@bot.message_handler(commands=['help', 'start'])
def home(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
@bot.message_handler(func=lambda x: x.text == "1")
def tut(message):
    bot.send_message(message.chat.id, """Works def tut""") 
           
@bot.message_handler(commands=["key"])
def key(message):                                          # Bottoni che quando clicchi fanno il testo
    kb= types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ciao")
    btn2 = types.KeyboardButton("Arrivedrci")
    kb.add(btn1,btn2)
    bot.send_message(message.chat.id, "Ciao", reply_markup=kb)
  
@bot.message_handler(commands=["button"])  
def key(message):
    kb = types.InlineKeyboardMarkup(row_width=2)                            # Bottoni che quando clicchi ti portano ad un sito con url
    btn1 = types.InlineKeyboardButton("gpt", url="https://chatgpt.com/")
    btn2 = types.InlineKeyboardButton("erewhon", url="https://erewhon.com/" )
    kb.add(btn1,btn2)
    bot.send_message(message.chat.id, "Here are some buttons", reply_markup=kb)
    

@bot.message_handler(commands=["car"])
def car(message):
    telebot.util.extract_arguments(message.text) 

    
@bot.message_handler(commands=["test"])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text= "btn1", callback_data="btn1")
    btn2 = types.InlineKeyboardButton(text= "btn2", callback_data="btn2")
    markup.add(btn1,btn2)
    bot.send_message(message.chat.id, "1", reply_markup=markup)
    
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callbackdata(callback):
    if callback.data == "btn1":
         markup = types.InlineKeyboardMarkup()
         btn1 = types.InlineKeyboardButton(text= "btn2", callback_data="btn2")
         btn2 = types.InlineKeyboardButton(text= "btn2", callback_data="btn1")
         markup.add(btn1,btn2)
         bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="ancora", reply_markup=markup) 
        
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()