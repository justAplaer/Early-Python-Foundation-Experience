from flask import Flask, render_template,request, redirect
#Подключение библиотеки баз данных
from flask_sqlalchemy import SQLAlchemy
import speech_recognition as speech_recog
import pyaudio
from random import choice, randint
from speach import speach
import time
levels = {
"easy": ["dairy", "mouse", "computer"],
"medium": ["programming", "algorithm", "developer"],
"hard": ["neural network", "machine learning", "artificial intelligence"] 
}
def play_game(level):
    words = levels.get(level, []) # Выбираем слова в зависимости от уровня сложности
    if not words:
        print("Некорректный уровень сложности.")
        return
    score = 0
    num_attempts = 3 # Количество попыток на каждое слово
    for _ in range(len(words)):
        random_word = choice(words)
        print(f"Произнесите слово {random_word}")
        recog_word = speach()
        print(recog_word)
        if random_word == recog_word:
            print("Абсолютно верно!")
            score += 1
        else:
            print(f"Что-то не получилось. Правильное слово: {random_word}")
        time.sleep(2) # Пауза между словами
    print(f"Игра завершена! Ваш счет: {score}/{len(words)}")
selected_level = input("Выберите уровень сложности (easy/medium/hard): ").lower() 
play_game(selected_level)