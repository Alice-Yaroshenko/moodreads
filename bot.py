from g4f.client import Client
import telebot

TOKEN = ('7399868268:AAE2kX0my75vFLlsrk8O1eGyvbc2TWUnrCU')  
bot = telebot.TeleBot(TOKEN)
client = Client()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f"Привет, {message.from_user.first_name}! Напиши жанр, и я подберу тебе интересные книги.")


@bot.message_handler(content_types=['text'])
def recommend_books(message):
    genre = message.text.strip()

    prompt = f"Посоветуй 5 популярных и интересных книг в жанре: {genre}. Кратко опиши каждую."

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
        )

        reply = response.choices[0].message.content

        bot.send_message(message.chat.id, reply)

    except Exception as e:
        bot.send_message(message.chat.id, "Произошла ошибка при получении рекомендаций. Попробуй ещё раз позже.")


bot.polling(none_stop=True)
