from gtts import gTTS
import os

def text_to_speech(text, filename):
    tts = gTTS(text, lang='ru')
    tts.save(filename)

text = "Ты грязный свин, тебе никогда не победить меня великого злого мага!"
filename = "output.mp3"
text_to_speech(text, filename)