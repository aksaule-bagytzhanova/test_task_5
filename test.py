import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import random
import datetime


yes_words = ['да говорите',
            'да',
            'слушаю',
            'да дальше',
            'дальше']

hello_no = ['нет',
       'не хочу',
       'не интересует']

hello_repeat = ['не слышно',
           'можете повторить',
           'повторите']

offer_yes = ['ага', 'ладно', 'да', 'хорошо', 'давайте']

offer_3 = ['Выходите на линию сегодня или завтра, да',
           'Инспользуем с вами такую возможность, да?',
           'Уже выходите на линию, да?',
           'Жду вас на линии, хорошо?']

neg = ['Я вас понял. Извините за беспокойство. Всего вам доброго',
       'Хорошо, поняла вас. Спасибо за уделенное время. Всего доброго',
       'Я вас поняла. Извините, пожалуйста, за беспокойство. Всего вам доброго.']

none_say = ['Извините, вас плохо слышно, будет лучше, если я перезвоню',
            'Хорошо, я перезвоню вам позже, до свидания!']

def robot_say_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def robot_hear_human():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Human say something")
        audio = r.listen(source)
    query = r.recognize_google(audio, language="ru-RU")
    return query.lower()


def hello_null():
    just_say = 'Алло, вас не слышно, вам удобно сейчас говорить?'
    robot_say_text(just_say)


def hello_repeat():
    repeate_w = 'Это компания Быстрое такси, разговор займет буквально минуту'
    robot_say_text(repeate_w)


def hello_one_minute():
    quick = 'Это займет всего минуту'
    robot_say_text(quick)


def offer_null():
    offers = ['Алло, вас что-то не слышно, вы могли бы повторить?',
              'Извините, возможно что-то со связью, повторите, пожалуйста, еще раз']

    robot_say_text(random.choice(offers))


def offer_default():
    offer = '''ну смотрите, у вас есть очень крутая возможность заработать 
    просто так сверху 10 000 тенге в день, и эта возмонзжость только неделю! 
    Если будете делать по 7 заказов в день а 7 заказов в день это вообще мало 
    на самом джеле за 7 заказов мы платим 1500 бонусов. '''
    robot_say_text(offer)


def offer_street():
    text = '''Нужно как можно быстрее встать на линию, и все бонусные 
    деньги вам выплатит таксопарк вместе с остальными деньгами'''
    robot_say_text(text)


def hello_main():
    hello1 = "Здравствуйте, компания Быстрое такси, меня зовут Берик. Вам удобно сейчас говорить?"
    robot_say_text(hello1)
    if robot_hear_human() in yes_words:
        yes = 'Спасибо большое!'
        robot_say_text(yes)
    elif robot_hear_human() in hello_repeat:
        hello_repeat()
    elif robot_hear_human() in hello_no:
        hello_one_minute()
    else:
        hello_null()


def offer_main():
    offer1 = "Вас давно не видно на линии, звоню уточнить, когда планируете выходить и знаете ли о нашей акции?"
    robot_say_text(offer1)
    if robot_hear_human() in yes_words or robot_hear_human() in offer_yes:
        offer_street()
        if robot_hear_human() in offer_yes:
            robot_say_text('Спасибо за ваше время, будем ждать вашего выхода')
        elif robot_hear_human() == 'что нужно сделать для этого':
            offer_street()
            if robot_hear_human() in offer_yes:
                robot_say_text("Спасибо за ваше время, будем ждать вашего выхода")
            elif robot_hear_human() in hello_no:
                robot_say_text(random.choice(neg))
            else:
                robot_say_text(random.choice(none_say))
        elif robot_hear_human() in hello_no:
            robot_say_text(random.choice(neg))
        else:
            robot_say_text(random.choice(none_say))

    elif robot_hear_human() in hello_no:
        offer_default()
        if robot_hear_human() in offer_yes:
            offer_street()
            if robot_hear_human() in offer_yes:
                robot_say_text("Спасибо за ваше время, будем ждать вашего выхода")
            elif robot_hear_human() in hello_no:
                robot_say_text(random.choice(neg))
            else:
                robot_say_text(random.choice(none_say))
        elif robot_hear_human() == 'что нужно сделать для этого':
            offer_street()
            if robot_hear_human() in offer_yes:
                robot_say_text("Спасибо за ваше время, будем ждать вашего выхода")
            elif robot_hear_human() in hello_no:
                robot_say_text(random.choice(neg))
            else:
                robot_say_text(random.choice(none_say))
        elif robot_hear_human() in hello_no:
            robot_say_text(random.choice(neg))
        else:
            robot_say_text(random.choice(none_say))


if __name__ == "__main__":
    hello_main()
    offer_main()
