from moviepy.editor import *

audioclip_0 = AudioFileClip("71.mp3")
audioclip_1 = AudioFileClip("72.mp3")
audioclip_2 = AudioFileClip("73.mp3")
audioclip_3 = AudioFileClip("74.mp3")
audioclip_4 = AudioFileClip("75.mp3")
audioclip_5 = AudioFileClip("76.mp3")

audioclip = concatenate_audioclips([
                            audioclip_0,
                            audioclip_1,
                            audioclip_2,
                            audioclip_3,
                            audioclip_4,
                            audioclip_5,
                                    ])

print("duration moviepy: " + str(audioclip.duration))

videoclip = ImageClip("big.jpg").set_duration(str(audioclip.duration))

videoclip2 = videoclip.set_audio(audioclip)

# videoclip_1 = VideoFileClip("Елена Звёздная. Город драконов. Книга вторая. Части 54,55,56.mp4")
# videoclip_2 = VideoFileClip("Елена Звёздная. Город драконов. Книга вторая. Части 0.mp4")
# # videoclip_3 = VideoFileClip("Елена Звёздная. Город драконов. Книга вторая. Части 51,52,53.mp4")
#
# videoclip2 = concatenate_videoclips([videoclip_1,
#                                      videoclip_2,
#                                      # videoclip_3
#                                      ])

videoclip2.write_videofile("Елена Звездная. Я твой монстр(2). Часть last.mp4", fps=30)
