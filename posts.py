import requests
import telegram
import instabot

# set up Telegram bot
bot = telegram.Bot("YOUR_TELEGRAM_BOT_TOKEN")
chat_id = "YOUR_TELEGRAM_CHAT_ID"

# set up Instagram API
bot = instabot.Bot()
bot.login(username="YOUR_INSTAGRAM_USERNAME", password="YOUR_INSTAGRAM_PASSWORD")

# post to Telegram
bot.send_message(chat_id=chat_id, text="Your message here")

# post to Instagram
bot.upload_photo("your_photo.jpg", caption="Your caption here")

# post to website
url = "YOUR_WEBSITE_URL"
data = {"post_text": "Your post text here"}
response = requests.post(url, data=data)
print(response.text)

