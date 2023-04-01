import pandas as pd

dt = pd.read_csv('/Users/magicmole/Desktop/res/yoga_combine_tithivar.csv', delimiter=';')

data = pd.DataFrame({
    'datetime': dt['datetime'],
    'tithi': dt['tithi'],
    'var': dt['var'],
    'tithi_name': dt['tithi_name'],
})

tithi_yogas = [
    #1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
    2, 7, 12, 17, 22, 27
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
tithi_result = []
var_result = []

for tithi_yoga in tithi_yogas:
    for var_yoga in var_yogas:
        for i in range(len(data['datetime'])):
            if (data['tithi'][i] == tithi_yoga and data['var'][i] == var_yoga):
                
                date_on = date_on + [data['datetime'][i]]
                date_off = date_off + [data['datetime'][i + 1]]
                tithi_result = tithi_result + [data['tithi_name'][i]]
                var_result = var_result + [data['var'][i]]

dt_pd = pd.DataFrame({
        "date_on": date_on,
        "date_off": date_off,
        "tithi_result": tithi_result,
        "var_result": var_result,
    }) 

print(dt_pd)
dt_pd.to_csv('./Сиддха-йога.csv')

'''
Тип титхи	Титхи	Сиддха йога	                   Мритью йога
Нанда	1, 6, 11, 16, 21, 26	пятница	         вторник, воскресенье
Бхадра	2, 7, 12, 17, 22, 27	среда	         пятница, понедельник
Джайа	3, 8, 13, 18, 23, 28	вторник	         среда
Риктха	4, 9, 14, 19, 24, 29	суббота	         четверг
Пурна	5, 10, 15, 20, 25, 30	четверг	         суббота
'''