import requests
from moviepy.editor import *

urls = [

'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-00-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-01-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-02-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-03-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-04-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-05-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-06-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-07-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-08-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-09-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-10-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-11-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-12-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-13-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-14-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-15-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-16-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-17-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-18-.mp3', 'https://a3.akniga.cc/uploads/z/10de1aef59b140f2/mp3/fakultet-neprijatnostejj-19-.mp3',

'https://shop.kp.ru/catalog/media/kplitres/f/9/5f77651d757f9.jpg',
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
    videoclip2.write_videofile("Ольга Шерстобитова. Факультет неприятностей(1). Часть " + str(i) + ".mp4", fps=30)
