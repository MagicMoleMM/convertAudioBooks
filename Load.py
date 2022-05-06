import requests
from moviepy.editor import *

urls = [

'https://m3.audioknigi.xyz/a/z/d95d3b1b479aa2fb/mobile/01-ledi-drakon-fakultet-oborotnichestva.mp3', 'https://m3.audioknigi.xyz/a/z/d95d3b1b479aa2fb/mobile/02-ledi-drakon-fakultet-oborotnichestva.mp3', 'https://m3.audioknigi.xyz/a/z/d95d3b1b479aa2fb/mobile/03-ledi-drakon-fakultet-oborotnichestva.mp3', 'https://m3.audioknigi.xyz/a/z/d95d3b1b479aa2fb/mobile/04-ledi-drakon-fakultet-oborotnichestva.mp3', 'https://m3.audioknigi.xyz/a/z/d95d3b1b479aa2fb/mobile/05-ledi-drakon-fakultet-oborotnichestva.mp3', 'https://m3.audioknigi.xyz/a/z/d95d3b1b479aa2fb/mobile/06-ledi-drakon-fakultet-oborotnichestva.mp3', 'https://m3.audioknigi.xyz/a/z/d95d3b1b479aa2fb/mobile/07-ledi-drakon-fakultet-oborotnichestva.mp3', 'https://m3.audioknigi.xyz/a/z/d95d3b1b479aa2fb/mobile/08-ledi-drakon-fakultet-oborotnichestva.mp3', 'https://m3.audioknigi.xyz/a/z/d95d3b1b479aa2fb/mobile/09-ledi-drakon-fakultet-oborotnichestva.mp3', 'https://m3.audioknigi.xyz/a/z/d95d3b1b479aa2fb/mobile/10-ledi-drakon-fakultet-oborotnichestva.mp3', 'https://m3.audioknigi.xyz/a/z/d95d3b1b479aa2fb/mobile/11-ledi-drakon-fakultet-oborotnichestva.mp3', 'https://m3.audioknigi.xyz/a/z/d95d3b1b479aa2fb/mobile/12-ledi-drakon-fakultet-oborotnichestva.mp3',

'https://cdn.eksmo.ru/v2/ITD000000000633781/COVER/cover1__w820.jpg',
    ]

for url in urls:
    m = requests.get(url)
    with open(url.split('/')[-1], 'wb') as f:
        f.write(m.content)

print(len(urls)-1)

for i in range(0, len(urls)-2, 2):

    audioclip_0 = AudioFileClip(str(urls[i].split('/')[-1]))
    audioclip_1 = AudioFileClip(str(urls[i+1].split('/')[-1]))
    # audioclip_2 = AudioFileClip(str(urls[i+2].split('/')[-1]))
    # audioclip_3 = AudioFileClip(str(urls[i+3].split('/')[-1]))
    # audioclip_4 = AudioFileClip(str(urls[i+4].split('/')[-1]))
    # audioclip_5 = AudioFileClip(str(urls[i+5].split('/')[-1]))
    # audioclip_6 = AudioFileClip(str(urls[i+6].split('/')[-1]))

    audioclip = concatenate_audioclips([audioclip_0,
                                        audioclip_1,
                                        # audioclip_2,
                                        # audioclip_3,
                                        # # audioclip_4,
                                        # audioclip_5,
                                        # audioclip_6,
                                        ])

    videoclip = ImageClip(urls[-1].split('/')[-1]).set_duration(str(audioclip.duration))
    videoclip2 = videoclip.set_audio(audioclip)
    videoclip2.write_videofile("Ольга Пашнина. Драконьи Авиалинии(3). Леди-дракон. Факультет оборотничества. Часть " + str(i) + ".mp4", fps=30)
