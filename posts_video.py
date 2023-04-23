import os
import google.auth
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import telegram
import instabot
from moviepy.editor import VideoFileClip

# set up Telegram bot
bot = telegram.Bot("YOUR_TELEGRAM_BOT_TOKEN")
chat_id = "YOUR_TELEGRAM_CHAT_ID"

# set up Instagram API
bot = instabot.Bot()
bot.login(username="YOUR_INSTAGRAM_USERNAME", password="YOUR_INSTAGRAM_PASSWORD")

# set up YouTube API
credentials = None
if os.path.exists("token.json"):
    credentials = Credentials.from_authorized_user_file("token.json")
if not credentials or not credentials.valid:
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    credentials = google.auth.default(scopes=scopes)[0]
    credentials = credentials.refresh(google.auth.transport.requests.Request())
    with open("token.json", "w") as token:
        token.write(credentials.to_json())
youtube = build("youtube", "v3", credentials=credentials)

# upload video to YouTube
video_path = "your_video.mp4"
video = VideoFileClip(video_path)
thumbnail_path = "your_thumbnail.jpg"
thumbnail = VideoFileClip(thumbnail_path)
request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "Your video title",
            "description": "Your video description",
            "tags": ["tag1", "tag2"],
            "categoryId": "22",
        },
        "status": {"privacyStatus": "public"},
    },
    media_body=video.write_videofile("temp_video.mp4"),
)
response = None
while response is None:
    status = request.next_chunk()["status"]
    print(f"Upload {int(status.progress() * 100)}%")
    if status.progress() == 1:
        response = request.execute()
os.remove("temp_video.mp4")
video.close()
os.remove(thumbnail_path)

# post to Telegram
caption = "Your caption here"
bot.send_video(chat_id=chat_id, video=open(video_path, "rb"), caption=caption)

# post to Instagram
caption = "Your caption here"
bot.upload_video(video_path, thumbnail_path=thumbnail_path, caption=caption)

print("Video uploaded to YouTube with ID: ", response["id"])
