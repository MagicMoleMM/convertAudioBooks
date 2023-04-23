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
caption = "Your caption here"
bot.send_photo(chat_id=chat_id, photo=open("your_photo.jpg", "rb"), caption=caption)

# post to Instagram
caption = "Your caption here"
bot.upload_photo("your_photo.jpg", caption=caption)

# post to website
url = "YOUR_WEBSITE_URL"
data = {"post_text": "Your post text here", "photo": open("your_photo.jpg", "rb")}
response = requests.post(url, files=data)
print(response.text)

