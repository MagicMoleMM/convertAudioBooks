import pandas as pd

dt = pd.read_csv('/Users/magicmole/Desktop/res/yoga_combine.csv', delimiter=';')

data = pd.DataFrame({
    'datetime': dt['datetime'],
    'tithi': dt['tithi'],
    'nackshatra': dt['nackshatra'],
    'var': dt['var'],
    'tithi_name': dt['tithi_name'],
})

tithi_yogas = [
    #1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
    2,7,12,17,22,27,3,8,13,18,23,28,
]

nackshatra_yogas = [
    #'Bharani',
    #'Krittika',
    'Rohini',
    'Mrigasira',
    'Ardra',
    #'Punarvasu',
    #'Pushya',
    #'Ashlesha',
    #'Magha',
    #'Poorva Phalg.',
    'Uttara Phalg.',
    #'Hasta',
    #'Chitra',
    #'Swati',
    #'Vishakha',
    'Anuradha',
    #'Jyeshtha',
    #'Moola',
    #'Poorvashadha',
    'Uttarashadha',
    #'Shravana',
    #'Dhanishta',
    #'Shatabhishak',
    #'Poorvabhadra',
    #'Uttarabhadra',
    #'Revati',
    #'Ashwini',
]

var_yogas = [
    #'Sunday',
    #'Monday',
    #'Tuesday',
    'Wednesday',
    #'Thursday',
    #'Friday',
    #'Saturday',
]

date_on = []
date_off = []
nackshatra_result = []
tithi_result = []
var_result = []

for tithi_yoga in tithi_yogas:
    for nackshatra_yoga in nackshatra_yogas:
        for var_yoga in var_yogas:
            for i in range(len(data['datetime'])):
                if (data['tithi'][i] == tithi_yoga and data['nackshatra'][i] == nackshatra_yoga and data['var'][i] == var_yoga):
                    
                    date_on = date_on + [data['datetime'][i]]
                    date_off = date_off + [data['datetime'][i + 1]]
                    nackshatra_result = nackshatra_result + [data['nackshatra'][i]]
                    tithi_result = tithi_result + [data['tithi_name'][i]]
                    var_result = var_result + [data['var'][i]]

dt_pd = pd.DataFrame({
        "date_on": date_on,
        "date_off": date_off,
        "nackshatra_result": nackshatra_result,
        "tithi_result": tithi_result,
        "var_result": var_result,
    }) 

print(dt_pd)
dt_pd.to_csv('./Сиддха-йога(особые благоприятные йоги).csv')

'''
Сиддха-йога (особые благоприятные йоги)
1. Воскресенье, совпадающее с 1-м, 4-м, 6-м, 7-м или 12-м титхи и с накшатрой Пушья, Хаста, Уттара-Пхалгуни, Уттара-Ашадха, Мула, Шравана или Уттара-Бхадра, образует Сиддха-Йогу.
2. Понедельник, совпадающий со 2-м, 7-м или 12-м титхи и с накшатрой Рохини, Мригашира, Пунарвасу, Читра, Шравана, Сатабхиша, Дхаништха или Пурва-Бхадра, дает такую же Йогу.
3. Если вторник попадает на день с накшатрой Ашвини, Мригашира, Читра, Анурадха, Мула, Уттара-Пхалгуни, Дхаништха или Пурва-Бхадра, то формируется Сиддха-Йога.
4. Среда совпадает с титхи Бхадра (2, 7 или 12) или Джая (3, 8 или 13) и с накшатрой Рохини, Мригашира, Ардра, Уттара-Пхалгуни, Уттара-Ашадха или Анурадха и образует Сиддха-Йогу.
5. Четверг, совпадающий с 4-м, 5-м, 7-м, 9-м, 13-м или 14-м титхи и с накшатрой Магха, Пушйа, Пунарвасу, Свати, Пурва-Ашадха, Пурва-Бхадра, Ревати или Ашвини, даёт Сиддха-Йогу.
6. Пятница при накшатре Ашвини, Бхарани, Ардра, Уттара-Пхалгуни, Читра, Свати, Пурва-Ашадха или Ревати и титхи Нанда (1, 6 или 11) или Бхадра (2, 7 или 12) формирует эту же благоприятную Йогу.
7. Суббота, попадающая на накшатру Свати, Рохини, Вишакха, Анурадха, Дхаништха или Сатабхиша и титхи Бхадра (2, 7 или 12) или Рикта (4, 9 или 14), образует такую же благоприятную Йогу.

Dwipushkar Yoga
1.Бхадра титхи - 2,7,12 – мудрец в соединении с 
2.Дни недели управляемые малефиками – воскресенье, вторник, суббота в соединении с 
3.Накшатры Дхаништха, Читра, Мригашира.

Tripushkar Yoga
1.Бхадра титхи – 2, 7, 12 – «мудрец» в соединении с
2.Воскресенье, вторник, суббота в соединении с
3.Накшатры Криттика, Пунарвасу, Уттарапхалгуни, Вишакха, Уттарашадха, Уттарабхадрапада.


'''